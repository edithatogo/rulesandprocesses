"""Command-line placeholder for PIC parameter diffs."""

from __future__ import annotations

import argparse
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Diff PIC parameter files")
    parser.add_argument("before")
    parser.add_argument("after")
    args = parser.parse_args(argv)
    for value in (args.before, args.after):
        path = Path(value)
        if not path.exists():
            parser.error(f"path does not exist: {path}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

