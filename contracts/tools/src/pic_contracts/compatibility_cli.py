"""Command-line interface for offline FOI-O compatibility bundles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from pic_contracts.compatibility import validate_offline_bundle


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an offline FOI-O/PIC bundle")
    parser.add_argument("bundle", help="directory containing manifest.json and artifacts/")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args(argv)
    report = validate_offline_bundle(Path(args.bundle))
    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    elif report.ok:
        print(f"OK: {args.bundle}")
    else:
        for issue in report.issues:
            print(f"{issue.code}: {issue.path}: {issue.message}")
    return 0 if report.ok else 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
