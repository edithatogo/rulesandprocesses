#!/usr/bin/env python3
"""Validate the paper programme's version and citation/mirror register."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "papers/zenodo/foi-programme-mirror-manifest.json"
REPOSITORIES = {
    "foi-o": Path("/Volumes/PortableSSD/GitHub/foi-o"),
    "fyi-cli": Path("/Volumes/PortableSSD/GitHub/fyi-cli"),
    "fyi-archive": Path("/Volumes/PortableSSD/GitHub/fyi-archive"),
    "nlp-policy-nz": Path("/Volumes/PortableSSD/GitHub/nlp-policy-nz"),
    "legislation": Path("/Volumes/PortableSSD/GitHub/legislation"),
    "rac-conformance": ROOT,
}

def main() -> int:
    data = json.loads(MANIFEST.read_text())
    assert data["schema_version"] == "1.0"
    expected = {"foi-o", "fyi-cli", "fyi-archive", "nlp-policy-nz", "legislation", "rac-conformance", "alaveteli"}
    assert {item["id"] for item in data["artifacts"]} == expected
    for item in data["artifacts"]:
        if item["zenodo_status"] == "verified_published_version":
            assert item["zenodo_doi"], item["id"]
        if item["zenodo_status"] == "published_record_version_mismatch":
            assert item["zenodo_doi"], item["id"]
            assert item["zenodo_record_version"] != item["version"], item["id"]
        if item["kind"] != "upstream_workflow_intelligence":
            assert (REPOSITORIES[item["id"]] / item["citation_file"]).is_file(), item["id"]
            assert item["version"] and item["tag"], item["id"]
    print(f"validated {len(data['artifacts'])} programme artefacts")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
