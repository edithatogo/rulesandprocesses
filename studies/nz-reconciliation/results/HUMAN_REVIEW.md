# [HUMAN] NZ reconciliation Phase 2 review package

Track: `nz_reconciliation_20260707`  
Prepared: 2026-07-09

## What to review

1. **`studies/nz-reconciliation/results/DIVERGENCE_REPORT.md`** — canonical divergence report (coverage finding).
2. **`studies/nz-reconciliation/results/openfisca-aotearoa-static-probe.json`** — static parameter/variable probe.
3. **JSONL evidence**
   - `rulespec-candidate-results.jsonl` — 14/17 RuleSpec companion-oracle rows `ok`; 3 KiwiSaver `compile_blocked` (#79).
   - `openfisca-aotearoa-candidate-results.jsonl` — 17/17 `engine_gap`.
   - `comparison-candidate-results.jsonl` — all classified `engine_gap` (0 numeric agreements).
4. **Inventory mapping** — `fixtures/case-inventory.json` `openfiscaAotearoa` blocks updated from `pending_mapping` → `engine_gap` with evidence notes.

## Certification questions for Dylan

1. Accept the finding that **openfisca-aotearoa is not a viable numeric comparator** for these three RuleSpec slices (income tax liability, ACC earners levy, KiwiSaver)?
2. Prefer follow-up as:
   - **A)** open an upstream issue/PR on openfisca-aotearoa proposing the missing formulas; or
   - **B)** select a different NZ comparator for a new comparative track; or
   - **C)** close this track as completed with a documented engine-gap result?
3. KiwiSaver remains blocked on RuleSpec compile ([rulespec-nz#79](https://github.com/TheAxiomFoundation/rulespec-nz/issues/79)) — any change to that upstream status since last check?

## What agents will not do

- Will not invent OpenFisca formulas to force a numeric comparison.
- Will not mark numeric agreement where only one engine ran.
- Will not open upstream issues without this human gate.
