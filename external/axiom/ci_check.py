from __future__ import annotations

import sys
from pathlib import Path
from sys import stderr

sys.path.insert(0, str(Path(__file__).resolve().parent))

from run_rulespec_nz_live_suite import main as run_live_suite


REQUIRED_PATHS = [
    Path(".external-repos/axiom-rules-engine/target/debug/axiom-rules-engine"),
    Path("/tmp/rulespec-nz-gst.compiled.json"),
    Path("/tmp/rulespec-nz-acc-earners-levy.compiled.json"),
    Path("/tmp/rulespec-nz-individual-income-tax.compiled.json"),
    Path("/tmp/rulespec-nz-new-zealand-superannuation-core.compiled.json"),
    Path("/tmp/rulespec-nz-new-zealand-superannuation-special-rates.compiled.json"),
]


def main() -> int:
    missing = [path for path in REQUIRED_PATHS if not path.exists()]
    if missing:
        print(
            "SKIP: external Axiom engine artifacts are unavailable for CI smoke checks.",
            file=stderr,
        )
        for path in missing:
            print(f"SKIP: missing {path}", file=stderr)
        return 0
    return run_live_suite()


if __name__ == "__main__":
    raise SystemExit(main())
