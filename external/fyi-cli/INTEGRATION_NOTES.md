# fyi-cli ↔ foi-o `oia_rules` — deferred integration notes

**Status:** deferred (2026-07-09) — **no PR opened**  
**Assessed repo:** [edithatogo/fyi-cli](https://github.com/edithatogo/fyi-cli) (clone: `/Volumes/PortableSSD/GitHub/fyi-cli`, `master` @ `9c3133c`)  
**Related upstream (rules source):** [edithatogo/foi-o](https://github.com/edithatogo/foi-o) — `oia_rules` merged via [PR #20](https://github.com/edithatogo/foi-o/pull/20) (`d2f5dbd`)

## Decision

**Do not force a code integration PR into `fyi-cli` at this time.**

There is adjacent clock *metadata* and a coarse working-day helper, but **no low-risk, natural consumer surface** for the isolated `foi_o_nz.oia_rules` module or for hard-wiring a `foi-o-nz` dependency. A minimal “hook it up” PR would either:

1. fight the project’s Rust-first direction, or  
2. invent a fragile language/process boundary, or  
3. silently change multi-jurisdiction deadline math.

None of those meet the “low-risk and clearly in edithatogo/fyi-cli” bar.

## What fyi-cli actually has today

### Architecture

| Layer | Path | Role for clocks |
| --- | --- | --- |
| **Active core** | Rust workspace `crates/fyi-core`, `fyi-cli`, `fyi-mcp` | Recommended path; new work goes here. |
| **Legacy Python** | `src/fyi_system/` (PyPI `fyi-cli`) | Still installable; README states it is **not being extended** with new features. |
| **Dashboard** | Next.js under `dashboard/` | UI copy mentions “Past statutory deadline”; no legal calendar engine. |

`foi-o` is **not** a dependency of either the Rust workspace or the Python package (`pyproject.toml` has no `foi-o-nz`).

### Clock-adjacent surfaces (not OIA-accurate)

1. **Instance metadata** — `crates/fyi-core/instances.toml`  
   NZ instance `nz-fyi` declares `statutory_deadline_days = 20` under `foi_law`. Same pattern for AU/UK/etc. with different day counts. This is catalog metadata for drafting/labels, not a holiday-aware legal engine.

2. **Weekend-only working-day helper** — `crates/fyi-core/src/i18n.rs`  
   `LocalizationEngine::add_working_days` / `deadline_for_instance` advance calendar days while skipping Saturday/Sunday only. No public holidays, no OIA s 2 summer exclusion (25 Dec–15 Jan), no transfer/extension/deemed-refusal decisions.

3. **Drafting copy** — `crates/fyi-core/src/drafting.rs`  
   Mentions the statutory day count from instance metadata when scaffolding a letter. Not a deadline calculator for case tracking.

4. **Python legacy** — `src/fyi_system/`  
   “Deadline” strings appear only as follow-up *tone* strategies (`firm_deadline_check` in `reporting.py`). No working-day arithmetic, no import of `foi_o_nz`.

### Explicit non-goals of fyi-cli (from its own README)

- Multi-jurisdiction Alaveteli client (NZ, AU, UK, DE, …).  
- Capture, local DB, sync, archive, monitoring, MCP for operators.  
- **Not** an NZ OIA process/ontology workbench (that role is assigned to `foi-o` in the foi-o README ecosystem table).

## What foi-o provides (operator / library paths)

### CLI (indicative clock annotation)

From [foi-o README](https://github.com/edithatogo/foi-o):

```bash
uv run foi-o-nz clock 2026-12-23
# or, once installed: foi-o-nz clock 2026-12-23
```

Upstream CLI implementation (`foi_o_nz.cli:app` command `clock`) calls `foi_o_nz.dates.calculate_indicative_clock` and prints JSON with explicit warnings such as indicative-only / not legal advice. This is the supported **operator** surface for “what does the machine think the response clock looks like?”

**Note:** the `clock` CLI path is the dates/LegalClock helper, not a thin wrapper around every `oia_rules` decision ID. Use the library API below when you need PIC-shaped rule invocations (response/transfer deadline, extension validity, deemed refusal, urgency discretion).

### Library (`oia_rules` on foi-o `main`)

```python
from datetime import date
from foi_o_nz.oia_rules import (
    RuleInvocation,
    ValueObject,
    evaluate_invocation,
    evaluate_response_deadline,
    nz_working_days,
)

# Typed invocation (PIC-oriented)
result = evaluate_invocation(
    RuleInvocation(
        decision_id="nz-oia/decision.response_deadline",
        inputs={
            "nz-oia/variable.receipt_date": ValueObject(
                value="2026-12-23",
                valueState="known",
            ),
        },
        parameter_set="0.1.0",
        invoked_by="operator-notebook",
    ),
    holidays=None,  # supply regional/public holidays when known
)
deadline = result.outputs["nz-oia/decision.response_deadline"]
print(deadline.value, deadline.valueState)

# Direct pure helpers
due = evaluate_response_deadline(
    ValueObject(value="2026-12-23", valueState="known")
)
print(nz_working_days(date(2026, 12, 23), 20))
```

Package constraints relevant to any future fyi-cli coupling:

- PyPI/project name: `foi-o-nz`  
- `requires-python = ">=3.12"` (fyi-cli Python package still claims `>=3.10`)  
- Rules re-use `foi_o_nz.dates.add_working_days` (holidays + OIA summer exclusion)

Staged copy for offline PIC validation also lives in this monorepo under `external/foi-o/src/foi_o_nz/oia_rules/`.

## Why integration was deferred (risk register)

| Risk | Severity | Detail |
| --- | --- | --- |
| Language / stack mismatch | High | Active fyi-cli path is **Rust**. `oia_rules` is **Python**. Native dependency is impossible without reimplementation or IPC. |
| Legacy Python freeze | High | README: Python package is reference-only and not extended. Adding `foi-o-nz` there contradicts project direction. |
| Python version gap | Medium | `foi-o-nz` ≥3.12 vs fyi-cli Python ≥3.10. |
| Multi-jurisdiction semantics | High | `LocalizationEngine::add_working_days` is shared for all locales. Swapping NZ holidays/summer rules into that helper without jurisdiction branching would mis-serve AU/UK/DE instances. |
| Behavioural change without product surface | Medium | Dashboard/list UIs do not currently drive case deadlines from the Rust helper in a certified way; wiring OIA rules needs a designed UX + “indicative only” labeling (foi-o’s stance). |
| Scope creep of oia_rules | Medium | Full module covers transfer, extension validity, deemed refusal, urgency discretion points. fyi-cli has no process model for those inputs. |
| Subprocess optional dependency | Medium | Shelling out to `foi-o-nz clock` from Rust is possible but is ops glue, not a clean library boundary; fails closed when binary missing; hard to test in CI without vendoring foi-o. |
| Duplicate legal logic in Rust | High | Porting OIA s 2/14/15/15A clocks into Rust duplicates `foi-o` and breaks the “single rules module” extraction goal of PR #20. |

## Recommended operator workflow (no fyi-cli changes)

1. Track requests in `fyi-cli` (local DB, Alaveteli sync, drafts, archive).  
2. When an NZ response clock is needed, use **foi-o** separately:
   - `foi-o-nz clock <receipt-date>` for indicative JSON, or  
   - a small notebook/script importing `foi_o_nz.oia_rules`.  
3. Treat all machine clocks as **indicative** until a human certifies against the Act, official holiday calendars, and agency receipt records (same boundary as foi-o).  
4. For platform-level statutory-clock *metadata hooks* on Alaveteli states, see the separate Alaveteli work (`external/alaveteli/`), not fyi-cli.

## Future integration options (if a track re-opens this)

Only pursue if a conductor track names a concrete user story and acceptance tests. Prefer order:

1. **Document-only (done here)** — operator dual-tool workflow; no code.  
2. **Optional external command adapter (Rust)** — e.g. `fyi-cli oia-clock --receipt 2026-12-23` that invokes `foi-o-nz clock` when present, else prints install instructions. No compile-time dependency on Python.  
3. **Jurisdiction-pluggable clock trait (Rust)** — replace weekend-only helper with a `StatutoryClock` trait; default weekend skip for non-NZ; NZ implementation either IPC to foi-o or a carefully vendored pure calendar port *fed by fixtures from* `oia_rules` (never AI-promoted goldens).  
4. **Do not** add a hard `foi-o-nz` dependency to the legacy Python package or re-implement full `oia_rules` inside fyi-cli without a named consumer for extension/deemed-refusal inputs.

## Assessment evidence (paths)

| Item | Location |
| --- | --- |
| Rust weekend clock | `/Volumes/PortableSSD/GitHub/fyi-cli/crates/fyi-core/src/i18n.rs` (`add_working_days`, `deadline_for_instance`) |
| NZ 20-day metadata | `/Volumes/PortableSSD/GitHub/fyi-cli/crates/fyi-core/instances.toml` (`nz-fyi`) |
| Instance law struct | `/Volumes/PortableSSD/GitHub/fyi-cli/crates/fyi-core/src/jurisdiction.rs` (`FoiLaw.statutory_deadline_days`) |
| Python package freeze note | `/Volumes/PortableSSD/GitHub/fyi-cli/README.md` |
| No foi-o dependency | `/Volumes/PortableSSD/GitHub/fyi-cli/pyproject.toml`, `Cargo.toml` workspace |
| Staged oia_rules API | `external/foi-o/src/foi_o_nz/oia_rules/` |
| Upstream oia_rules merge | `external/foi-o/SUBMISSION.md`, `external/ADOPTION_STATUS.md` |

## PR / submission

- **PR URL:** none (intentionally not opened).  
- **Staging path for these notes:** `external/fyi-cli/INTEGRATION_NOTES.md`  
- Agents must not open third-party PRs; any future optional adapter remains a `[HUMAN]` or authorized-maintainer gate after a track names the surface.
