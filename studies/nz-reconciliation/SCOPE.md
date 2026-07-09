# NZ RuleSpec vs OpenFisca Aotearoa — scope

Track: `nz_reconciliation_20260707`

## Goal

Cross-engine reconciliation of NZ personal income tax, ACC earners levy, and KiwiSaver contribution calculations between:

- `TheAxiomFoundation/rulespec-nz` (Axiom RuleSpec)
- `ServiceInnovationLab/openfisca-aotearoa` (OpenFisca country package)

using PIC-aligned fixtures and deterministic comparison (decimal strings for money).

## Phase 1 deliverables (scaffolding)

- Case inventory (≥15 cases) under `fixtures/case-inventory.json`
- Deterministic comparison runner under `runner/src/nz_reconciliation/`
- Unit tests for inventory filters and comparison logic

## Phase 2 (not yet)

- Live RuleSpec compile/run for runnable slices
- OpenFisca Aotearoa simulation mapping and runs
- Divergence reports under `results/`

## Known blockers

- KiwiSaver RuleSpec module fails `axiom-rules-engine compile` (YAML `values` sequence vs map). Tracked upstream: https://github.com/TheAxiomFoundation/rulespec-nz/issues/79
- OpenFisca Aotearoa has income-tax and ACC variables; KiwiSaver coverage is not present as named modules in the local checkout — map carefully or mark `engine_gap`.

## Local checkouts

- `.external-repos/rulespec-nz` @ `3c6436b2ecf82dd7a7f7810a406a2695a64af33a` (pinned in inventory)
- `.external-repos/openfisca-aotearoa` (shallow clone of ServiceInnovationLab/openfisca-aotearoa)
