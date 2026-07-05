"""Generate a human fixture-promotion review packet."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from snap_divergence.comparison import load_jsonl

DEFAULT_CANDIDATES = Path("studies/snap-divergence/fixtures/candidates/snap-fy2026-candidates.json")
DEFAULT_CLASSIFIED_RESULTS = Path("studies/snap-divergence/results/classified-candidate-divergences.jsonl")
DEFAULT_PACKET = Path("studies/snap-divergence/fixtures/FIXTURE_PROMOTION_REVIEW.md")


def load_candidates(path: Path) -> dict[str, dict[str, Any]]:
    data = json.loads(path.read_text())
    return {case["caseId"]: case for case in data["cases"]}


def build_promotion_rows(
    candidates: dict[str, dict[str, Any]],
    comparisons: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    rows = []
    for comparison in comparisons:
        candidate = candidates[comparison["caseId"]]
        household = candidate.get("entities", {}).get("household", {})
        rows.append(
            {
                "caseId": comparison["caseId"],
                "description": candidate["description"],
                "state": household.get("state", ""),
                "fixtureClass": household.get("fixtureClass", ""),
                "recommendation": "promote" if comparison["agreement"] else "hold",
                "classification": comparison["classification"],
                "decisionRelevant": comparison["decisionRelevant"],
                "policyengineEligible": comparison["policyengine"]["eligible"],
                "policyengineAllotment": comparison["policyengine"]["allotment"],
                "prdEligible": comparison["prd"]["eligible"],
                "prdAllotment": comparison["prd"]["allotment"],
                "allotmentDifference": comparison["allotmentDifference"],
            },
        )
    return rows


def summarize_rows(rows: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "total": len(rows),
        "recommended": sum(1 for row in rows if row["recommendation"] == "promote"),
        "held": sum(1 for row in rows if row["recommendation"] == "hold"),
        "decisionRelevantHeld": sum(
            1 for row in rows if row["recommendation"] == "hold" and row["decisionRelevant"]
        ),
    }


def write_packet(path: Path, rows: list[dict[str, Any]]) -> None:
    summary = summarize_rows(rows)
    recommended = [row for row in rows if row["recommendation"] == "promote"]
    held = [row for row in rows if row["recommendation"] == "hold"]
    lines = [
        "# SNAP Fixture Promotion Review",
        "",
        "Track: `divergence_study_20260704`",
        "",
        "This packet is generated from candidate fixture comparisons. It is a review aid only; fixture promotion still requires Dylan approval because the candidate corpus was AI-proposed.",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Candidate cases | {summary['total']} |",
        f"| Recommended for promotion | {summary['recommended']} |",
        f"| Held for divergence analysis | {summary['held']} |",
        f"| Decision-relevant held cases | {summary['decisionRelevantHeld']} |",
        "",
        "## Recommendation",
        "",
        "Promote the agreement cases below as the first human-approved golden fixture set after Dylan confirms the fixture inputs and outputs. Keep the held cases as analysis candidates until Phase 4 source-level investigation resolves whether the difference is expected modeling scope, parameter vintage, implementation error, or legal interpretation.",
        "",
        "## Recommended Promotion Cases",
        "",
        "| Case | State | Class | PolicyEngine | PRD | Diff |",
        "|---|---|---|---:|---:|---:|",
    ]
    for row in recommended:
        lines.append(
            f"| `{row['caseId']}` | {row['state']} | {row['fixtureClass']} | "
            f"{_output(row['policyengineEligible'], row['policyengineAllotment'])} | "
            f"{_output(row['prdEligible'], row['prdAllotment'])} | {row['allotmentDifference']} |",
        )
    lines.extend(
        [
            "",
            "## Held Cases",
            "",
            "| Case | State | Classification | Decision-relevant | PolicyEngine | PRD | Diff |",
            "|---|---|---|---|---:|---:|---:|",
        ],
    )
    for row in held:
        lines.append(
            f"| `{row['caseId']}` | {row['state']} | {row['classification']} | "
            f"{str(row['decisionRelevant']).lower()} | "
            f"{_output(row['policyengineEligible'], row['policyengineAllotment'])} | "
            f"{_output(row['prdEligible'], row['prdAllotment'])} | {row['allotmentDifference']} |",
        )
    lines.extend(
        [
            "",
            "## Evidence",
            "",
            "- Candidate fixtures: `studies/snap-divergence/fixtures/candidates/snap-fy2026-candidates.json`",
            "- PolicyEngine outputs: `studies/snap-divergence/results/policyengine-candidate-results.jsonl`",
            "- PRD outputs: `studies/snap-divergence/results/prd-candidate-results.jsonl`",
            "- Classified comparison rows: `studies/snap-divergence/results/classified-candidate-divergences.jsonl`",
        ],
    )
    path.write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--classified", type=Path, default=DEFAULT_CLASSIFIED_RESULTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_PACKET)
    args = parser.parse_args(argv)

    rows = build_promotion_rows(load_candidates(args.candidates), load_jsonl(args.classified))
    write_packet(args.output, rows)
    return 0


def _output(eligible: bool, allotment: str) -> str:
    return f"{'eligible' if eligible else 'ineligible'} / {allotment}"


if __name__ == "__main__":
    raise SystemExit(main())
