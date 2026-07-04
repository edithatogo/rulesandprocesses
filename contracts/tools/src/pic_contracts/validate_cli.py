"""Command-line placeholder for PIC validation.

The full validator is implemented in Track 1 phase 4. Until then this command
exists so the scaffold can be installed and `make check` can run.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate PIC artifacts")
    parser.add_argument(
        "path",
        nargs="?",
        default="contracts",
        help="file or directory to validate",
    )
    args = parser.parse_args(argv)
    path = Path(args.path)
    if not path.exists():
        parser.error(f"path does not exist: {path}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
