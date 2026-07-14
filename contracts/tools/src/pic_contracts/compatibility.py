"""Offline verification for content-addressed FOI-O compatibility bundles."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from pic_contracts.validation import ValidationIssue, ValidationReport, validate_file


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def validate_offline_bundle(bundle: Path) -> ValidationReport:
    """Validate a manifest and its content-addressed PIC artifacts without network access."""
    manifest_path = bundle / "manifest.json"
    if not manifest_path.is_file():
        report = ValidationReport()
        report.add(ValidationIssue(str(manifest_path), "bundle manifest is missing", "input"))
        return report

    report = validate_file(manifest_path)
    if not report.ok:
        return report
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for index, artifact in enumerate(manifest["picArtifacts"]):
        digest = artifact["sha256"]
        artifact_path = bundle / "artifacts" / digest
        location = f"{manifest_path}:picArtifacts/{index}"
        if not artifact_path.is_file():
            report.add(
                ValidationIssue(
                    location,
                    f"content-addressed artifact is missing: {digest}",
                    "input",
                )
            )
            continue
        content = artifact_path.read_bytes()
        if sha256_bytes(content) != digest:
            report.add(ValidationIssue(location, "artifact digest mismatch", "digest"))
            continue
        try:
            document: Any = json.loads(content)
        except json.JSONDecodeError:
            report.add(ValidationIssue(location, "artifact is not valid JSON", "json"))
            continue
        if not isinstance(document, dict) or document.get("conformsTo") != artifact["contract"]:
            report.add(
                ValidationIssue(location, "artifact contract does not match wrapper", "reference")
            )
    return report
