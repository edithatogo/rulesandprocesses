import copy
import json

from tools.independent_status import GOVERNING_ISSUE, build_ledger, validate


def test_committed_independent_status_is_synchronized() -> None:
    assert validate() == []


def test_generated_ledger_preserves_candidates_without_claiming_adoption() -> None:
    registry = {
        "candidates": [
            {
                "id": "candidate",
                "organisation": "External Org",
                "status": "awaiting-response",
                "outreachUrl": "https://example.org/outreach",
            }
        ]
    }
    snapshot = {"asOf": "2026-07-18", "gate": "blocked_pending_external_evidence"}
    ledger = build_ledger(registry, snapshot)
    assert ledger["governingIssue"] == GOVERNING_ISSUE
    assert ledger["qualifyingConsumers"] == []
    assert ledger["candidates"][0]["id"] == "candidate"


def test_ledger_generation_is_deterministic() -> None:
    registry = {"candidates": []}
    snapshot = {"asOf": "2026-07-18", "gate": "blocked_pending_external_evidence"}
    first = build_ledger(copy.deepcopy(registry), copy.deepcopy(snapshot))
    second = build_ledger(copy.deepcopy(registry), copy.deepcopy(snapshot))
    assert json.dumps(first, sort_keys=True) == json.dumps(second, sort_keys=True)
