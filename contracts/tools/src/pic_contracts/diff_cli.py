"""Command-line interface for PIC parameter diffs."""

from __future__ import annotations

import argparse
from pathlib import Path

from pic_contracts.diff import changes_to_json, changes_to_markdown, diff_files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Diff PIC parameter files")
    parser.add_argument("before")
    parser.add_argument("after")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of Markdown")
    args = parser.parse_args(argv)
    for value in (args.before, args.after):
        path = Path(value)
        if not path.exists():
            parser.error(f"path does not exist: {path}")
    changes = diff_files(Path(args.before), Path(args.after))
    if args.json:
        print(changes_to_json(changes))
    else:
        print(changes_to_markdown(changes), end="")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
