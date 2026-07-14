"""Deterministic source triangulation for adverse-incident candidates."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Disposition:
    mapping_id: str
    label: str
    exception_reasons: tuple[str, ...]
    human_review_required: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "mappingId": self.mapping_id,
            "proposedDisposition": self.label,
            "exceptionReasons": list(self.exception_reasons),
            "humanReviewRequired": self.human_review_required,
        }


def resolve(assertions_path: Path, mappings_path: Path) -> list[Disposition]:
    """Resolve candidates using assertion fields, never mapping names."""

    assertions = _load(assertions_path)["assertions"]
    mappings = _load(mappings_path)["mappings"]
    by_id = {assertion["id"]: assertion for assertion in assertions}
    results: list[Disposition] = []
    for mapping in mappings:
        selected = [by_id[ref] for ref in mapping["sourceAssertionIds"] if ref in by_id]
        reasons: list[str] = []
        if not mapping["sourceAssertionIds"]:
            reasons.append("fixture assumption underspecified")
        if len(selected) != len(mapping["sourceAssertionIds"]):
            reasons.append("missing source assertion")
        jurisdictions = {assertion["jurisdiction"] for assertion in selected}
        if jurisdictions and any(jurisdiction != mapping["jurisdiction"] for jurisdiction in jurisdictions):
            reasons.append("conflicting jurisdictional authority")
        if any(assertion["sourceStatus"] in {"blocked", "unavailable", "conflicting"} for assertion in selected):
            reasons.append("blocked official source")
        if any(assertion["effectiveDateStatus"] != "verified" for assertion in selected):
            reasons.append("missing effective date")
        if selected and all(assertion["authorityClass"] == "secondary" for assertion in selected):
            reasons.append("secondary-source-only evidence")
        if reasons:
            label = "needs_more_source_review"
        elif mapping["kind"] == "jurisdictional-overlay":
            label = "expected_jurisdictional_difference"
        else:
            label = "candidate_supported"
        results.append(
            Disposition(mapping["id"], label, tuple(sorted(set(reasons))), True)
        )
    return results


def write_results(
    assertions_path: Path, mappings_path: Path, output_path: Path
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = {
        "profileId": "adverse-incidents/open-disclosure",
        "method": "deterministic-source-triangulation",
        "results": [result.to_dict() for result in resolve(assertions_path, mappings_path)],
    }
    output_path.write_text(
        json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def _load(path: Path) -> dict:
    document = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise ValueError(f"expected JSON object: {path}")
    return document


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("assertions", type=Path)
    parser.add_argument("mappings", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    write_results(args.assertions, args.mappings, args.output)


if __name__ == "__main__":
    main()
