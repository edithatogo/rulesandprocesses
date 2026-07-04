from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_manifest(manifest_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[2]
    schema_path = repo_root / "schemas" / "manifest.schema.json"
    schema = load_json(schema_path)
    manifest = load_json(manifest_path)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(manifest), key=lambda e: list(e.path))
    if errors:
        lines = []
        for error in errors:
            where = ".".join(str(p) for p in error.path) or "<root>"
            lines.append(f"{where}: {error.message}")
        raise SystemExit("RaCX manifest validation failed:\n" + "\n".join(lines))
    print(f"OK: {manifest_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a RaCX manifest")
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    validate_manifest(args.manifest)


if __name__ == "__main__":
    main()
