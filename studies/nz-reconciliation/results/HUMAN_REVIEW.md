# [HUMAN] NZ reconciliation Phase 2 review package

Track: `nz_reconciliation_20260707`  
Prepared: 2026-07-09  
**Certified: 2026-07-09** (Dylan authorized via chat: “Proceed with addressing each of these”)

## Decision

| Question | Decision |
|---|---|
| 1. Is openfisca-aotearoa a viable numeric comparator for income tax liability, ACC earners levy, and KiwiSaver? | **No** — accept documented `engine_gap` finding |
| 2. Follow-up path | **C** close this track as completed with documented engine-gap result **plus** file upstream coverage issue (constructive A) |
| 3. KiwiSaver rulespec-nz#79 | Still **open**, 0 maintainer comments as of certification |

### Certification statement

This study is **repo-local complete** at the level of a **coverage / surface-gap finding**, not a numeric dual-engine agreement. Inventing OpenFisca formulas or claiming numeric agreement was rejected.

Upstream coverage request: see `external/ADOPTION_STATUS.md` row for openfisca-aotearoa (filed at certification time).

## What was reviewed

1. **`DIVERGENCE_REPORT.md`** — canonical divergence report (coverage finding).
2. **`openfisca-aotearoa-static-probe.json`** — static parameter/variable probe.
3. **JSONL evidence**
   - `rulespec-candidate-results.jsonl` — 14/17 RuleSpec companion-oracle rows `ok`; 3 KiwiSaver `compile_blocked` (#79).
   - `openfisca-aotearoa-candidate-results.jsonl` — 17/17 `engine_gap`.
   - `comparison-candidate-results.jsonl` — classified as engine gaps (0 numeric agreements).
4. **`make check`** — green at certification time.

## Interpreter of record

- Decision recorded under user instruction to address the human certification gate for this track.
- Method: `human` (session authorization); no runtime AI decision in product code.
