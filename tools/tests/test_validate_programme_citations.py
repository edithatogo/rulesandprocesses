import json
from pathlib import Path

import pytest

from tools.validate_programme_citations import validate_commit_pin

ROOT = Path(__file__).resolve().parents[2]


def test_integration_release_requires_full_commit_pin() -> None:
    validate_commit_pin(
        {
            "id": "integration",
            "kind": "software_and_integration",
            "commit": "a" * 40,
        },
    )

    for commit in (None, "a" * 39, "g" * 40):
        with pytest.raises(AssertionError):
            validate_commit_pin(
                {
                    "id": "integration",
                    "kind": "software_and_integration",
                    "commit": commit,
                },
            )


def test_other_artifact_kinds_do_not_require_commit_pin() -> None:
    validate_commit_pin({"id": "software", "kind": "software"})


def test_rac_zenodo_packet_matches_manifest() -> None:
    manifest = json.loads(
        (ROOT / "papers/zenodo/foi-programme-mirror-manifest.json").read_text(),
    )
    packet = json.loads(
        (ROOT / "papers/zenodo/RAC_CONFORMANCE_V0.2.0_ARCHIVE.json").read_text(),
    )
    row = next(item for item in manifest["artifacts"] if item["id"] == "rac-conformance")
    assert row["commit"] == packet["release_commit"]
    assert row["github_archive_sha256"] == packet["archive_sha256"]
    assert packet["zenodo_status"] == "pending_human_deposit"
