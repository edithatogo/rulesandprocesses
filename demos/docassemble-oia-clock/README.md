# Docassemble OIA clock interview (local package)

Smallest credible Docassemble-shaped demo from `external/docassemble/ASSESSMENT.md`: ask for a request receipt date, call the isolated OIA rules module, show the response deadline and a statutory trace.

## What this is

| Piece | Path | Role |
|---|---|---|
| Interview YAML | `docassemble/oia_clock/data/questions/oia_clock.yml` | Docassemble interview source (install into a Docassemble playground/package) |
| Helper | `src/oia_clock_demo/evaluate.py` | Pure Python wrapper around `foi_o_nz.oia_rules` (CI-testable without Docassemble) |
| Tests | `tests/` | Deterministic unit tests against staged `external/foi-o` |

## What this is not

- Not a deployed Docassemble server.
- Not legal advice; clocks are indicative only.
- Does not change `foi-o` process certification boundaries.

## Run tests (no Docassemble install)

Uses the staged `external/foi-o` `oia_rules` module plus the local working-day stub
from `demos/service-boundaries/src/foi_o_nz/dates.py` (same path as the service-boundary demos).

```sh
make docassemble-oia-clock-test
```

## Use inside Docassemble (optional)

1. Install or vendor `foi-o-nz` so `from foi_o_nz.oia_rules import …` works in the Docassemble Python environment.
2. Copy `docassemble/oia_clock/` into a Docassemble package named `docassemble.oia_clock` (or symlink this tree).
3. Start interview: `docassemble.oia_clock:data/questions/oia_clock.yml`.

The interview `code` blocks call the same helper API exercised by the unit tests.
