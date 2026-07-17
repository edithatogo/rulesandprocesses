import hashlib
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).parents[2] / "contracts/tools/src"))

from pic_contracts.schema_utils import load_json
from pic_contracts.validation import validate_file


ROOT = Path(__file__).parents[2]
CHAIN = ROOT / "conductor/tracks/core_model_demonstrator_20260717/FOI_DEMONSTRATOR_CHAIN.json"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_foi_demonstrator_chain_is_pinned_and_fail_closed() -> None:
    chain = json.loads(CHAIN.read_text(encoding="utf-8"))
    assert chain["status"] == "candidate-human-certification-required"
    assert chain["equivalenceClaim"] == "none"
    assert chain["profile"]["promotionStatus"] == "not-promoted"
    assert chain["executionEvidence"]["assertionStatus"] == "inferred"

    candidate = ROOT / chain["profile"]["path"]
    assert _sha256(candidate) == chain["profile"]["sha256"]
    assert validate_file(candidate).ok

    pic_trace = ROOT / chain["picTraceEvidence"]["path"]
    assert _sha256(pic_trace) == chain["picTraceEvidence"]["sha256"]
    assert validate_file(pic_trace).ok

    execution = ROOT / chain["executionEvidence"]["tracePath"]
    execution_schema = load_json(ROOT / "external/foi-process/schemas/portable/conformance-trace.schema.json")
    Draft202012Validator(execution_schema).validate(load_json(execution))
    assert _sha256(execution) == chain["executionEvidence"]["traceSha256"]

    replay = ROOT / chain["executionEvidence"]["replaySnapshotPath"]
    assert _sha256(replay) == chain["executionEvidence"]["replaySnapshotSha256"]
