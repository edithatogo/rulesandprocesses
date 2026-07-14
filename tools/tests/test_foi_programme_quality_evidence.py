"""Validate the cross-repository FOI quality evidence register."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_quality_evidence_register_is_pinned_and_explicit() -> None:
    register = json.loads(
        (ROOT / "papers/foi-programme-quality-evidence.json").read_text(encoding="utf-8")
    )

    assert register["schema_version"] == "1.0"
    assert {row["id"] for row in register["repositories"]} == {
        "foi-o",
        "fyi-archive",
        "nlp-policy-nz",
    }
    assert all(len(row["head"]) == 40 for row in register["repositories"])
    assert register["release_gates"]["cross_repository_extraction_contract"] == (
        "deferred_pending_re_extraction"
    )
    assert "not a claim" in register["manuscript_boundary"]
