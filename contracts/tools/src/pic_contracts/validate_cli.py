"""Command-line interface for PIC validation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from pic_contracts.validation import validate_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate PIC artifacts")
    parser.add_argument(
        "path",
        nargs="?",
        default="contracts",
        help="file or directory to validate",
    )
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--no-references",
        action="store_true",
        help="skip directory-level referential-integrity checks",
    )
    args = parser.parse_args(argv)
    path = Path(args.path)
    if not path.exists():
        parser.error(f"path does not exist: {path}")
    report = validate_path(path, check_references=not args.no_references)
    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    elif report.ok:
        print(f"OK: {path}")
    else:
        for issue in report.issues:
            print(f"{issue.code}: {issue.path}: {issue.message}")
    return 0 if report.ok else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
