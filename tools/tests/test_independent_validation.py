import json
from pathlib import Path
import subprocess
import sys

from tools.independent_validation import verify


ROOT = Path(__file__).parents[2]
KIT = ROOT / "independent/kit"


def test_canonical_kit_is_unique_and_bundle_matches_contract() -> None:
    assert not (ROOT / "conductor/tracks/v1_independent_validation_20260714/kit").exists()
    manifest = json.loads((KIT / "manifest.json").read_text())
    for artifact in manifest["artifacts"]:
        bundled = KIT / artifact["path"]
        canonical = ROOT / "contracts/pic-semantics/0.1.0" / bundled.relative_to(
            KIT / "bundle/pic-semantics-0.1.0"
        )
        assert bundled.read_bytes() == canonical.read_bytes()


def test_reference_runner_is_self_contained(tmp_path: Path) -> None:
    output = tmp_path / "results.json"
    completed = subprocess.run(
        [sys.executable, "run_reference.py", "--output", str(output)],
        cwd=KIT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    result = json.loads(output.read_text())
    assert result["status"] == "pass"
    assert result["kitVersion"] == "independent-kit/0.2.0"
    assert result["results"]


def test_example_result_cannot_qualify() -> None:
    report = verify(KIT, KIT / "example-result.json")
    assert not report["ok"]
    assert "implementation is maintainer-controlled" in report["diagnostics"]


def test_verifier_accepts_structurally_complete_independent_result(tmp_path: Path) -> None:
    result = json.loads((KIT / "example-result.json").read_text())
    result["implementation"].update({"maintainerControlled": False, "revision": "abcdef1234567", "repository": "external/example"})
    result["oracle"].update({"independent": True, "method": "independent-reference"})
    result["outcome"] = "qualifying"
    result["evidence"]["acknowledged"] = True
    path = tmp_path / "result.json"
    path.write_text(json.dumps(result))
    assert verify(KIT, path)["ok"]


def test_verifier_rejects_qualifying_result_without_acknowledgement(tmp_path: Path) -> None:
    result = json.loads((KIT / "example-result.json").read_text())
    result["implementation"].update({"maintainerControlled": False, "revision": "abcdef1234567", "repository": "external/example"})
    result["oracle"]["independent"] = True
    result["outcome"] = "qualifying"
    path = tmp_path / "result.json"
    path.write_text(json.dumps(result))
    report = verify(KIT, path)
    assert "qualifying result lacks maintainer acknowledgement" in report["diagnostics"]
