import copy
import json
from pathlib import Path

from pic_contracts.compatibility import sha256_bytes, validate_offline_bundle
from pic_contracts.compatibility_cli import main
from pic_contracts.schema_utils import CONTRACTS_ROOT, load_json

EXAMPLE = (
    CONTRACTS_ROOT
    / "pic-foio-compatibility"
    / "0.1.0"
    / "examples"
    / "valid"
    / "nz-release.json"
)


def _write_bundle(bundle: Path) -> dict:
    manifest = copy.deepcopy(load_json(EXAMPLE))
    artifacts = {
        "fixture": load_json(
            CONTRACTS_ROOT / "pic-fixtures/0.1.0/examples/valid/plain.json"
        ),
        "parameters": load_json(
            CONTRACTS_ROOT
            / "pic-parameters/0.2.0/examples/valid/parameters-v02-exclusions.json"
        ),
        "trace": load_json(
            CONTRACTS_ROOT / "pic-traces/0.2.0/examples/valid/trace-v02-missingness.json"
        ),
    }
    for wrapper in manifest["picArtifacts"]:
        content = json.dumps(artifacts[wrapper["kind"]], sort_keys=True).encode()
        digest = sha256_bytes(content)
        wrapper["sha256"] = digest
        wrapper["artifactUri"] = f"urn:sha256:{digest}"
        path = bundle / "artifacts" / digest
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    (bundle / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return manifest


def test_offline_bundle_validates_content_addressed_artifacts(tmp_path: Path) -> None:
    _write_bundle(tmp_path)
    assert validate_offline_bundle(tmp_path).ok
    assert main([str(tmp_path), "--json"]) == 0


def test_offline_bundle_rejects_digest_mismatch(tmp_path: Path) -> None:
    manifest = _write_bundle(tmp_path)
    digest = manifest["picArtifacts"][0]["sha256"]
    (tmp_path / "artifacts" / digest).write_text("{}", encoding="utf-8")
    report = validate_offline_bundle(tmp_path)
    assert not report.ok
    assert any(issue.code == "digest" for issue in report.issues)


def test_offline_bundle_rejects_contract_mismatch(tmp_path: Path) -> None:
    manifest = _write_bundle(tmp_path)
    wrapper = manifest["picArtifacts"][1]
    content = json.dumps({"conformsTo": "pic-traces/0.2.0"}, sort_keys=True).encode()
    replacement_digest = sha256_bytes(content)
    old_path = tmp_path / "artifacts" / wrapper["sha256"]
    old_path.unlink()
    wrapper["sha256"] = replacement_digest
    wrapper["artifactUri"] = f"urn:sha256:{replacement_digest}"
    (tmp_path / "artifacts" / replacement_digest).write_bytes(content)
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    report = validate_offline_bundle(tmp_path)
    assert not report.ok
    assert any(issue.code == "reference" for issue in report.issues)


def test_offline_bundle_rejects_invalid_wrapped_pic_artifact(tmp_path: Path) -> None:
    manifest = _write_bundle(tmp_path)
    wrapper = manifest["picArtifacts"][0]
    content = json.dumps({"conformsTo": "pic-fixtures/0.1.0"}, sort_keys=True).encode()
    replacement_digest = sha256_bytes(content)
    (tmp_path / "artifacts" / wrapper["sha256"]).unlink()
    wrapper["sha256"] = replacement_digest
    wrapper["artifactUri"] = f"urn:sha256:{replacement_digest}"
    (tmp_path / "artifacts" / replacement_digest).write_bytes(content)
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    report = validate_offline_bundle(tmp_path)
    assert not report.ok
    assert any("failed PIC validation" in issue.message for issue in report.issues)
