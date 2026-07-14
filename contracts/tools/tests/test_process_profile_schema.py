from __future__ import annotations

import json
from pathlib import Path

import pytest

from pic_contracts.schema_utils import validator_for
from pic_contracts.validation import validate_file

ROOT = Path(__file__).parents[2] / "process-profile" / "0.1.0" / "examples"


def _errors(path: Path) -> list[str]:
    document = json.loads(path.read_text(encoding="utf-8"))
    return [error.message for error in validator_for("process-profile").iter_errors(document)]


def test_valid_process_profile_examples() -> None:
    for path in sorted((ROOT / "valid").glob("*.json")):
        assert _errors(path) == [], path
        assert validate_file(path).ok, path


@pytest.mark.parametrize("path", sorted((ROOT / "invalid").glob("*.json")))
def test_invalid_process_profile_examples(path: Path) -> None:
    assert _errors(path) or not validate_file(path).ok, path


def test_foi_profile_preserves_existing_pic_identifiers() -> None:
    document = json.loads((ROOT / "valid" / "foi-oia.json").read_text(encoding="utf-8"))

    assert document["ruleInvocations"][0]["decisionId"] == "nz-oia/decision.response_deadline"
    assert document["ruleInvocations"][0]["traceConformsTo"] == "pic-traces/0.1.0"
    assert document["ruleInvocations"][0]["parameterIds"] == ["nz-oia/parameter.working_day_limit"]
