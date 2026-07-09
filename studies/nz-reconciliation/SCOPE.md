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

## Phase 2 (executed 2026-07-09)

- Live RuleSpec compile/run for income-tax and ACC earners-levy slices (14/17 `exact_match`; 3 KiwiSaver blocked).
- OpenFisca Aotearoa mapping: all 17 cases classified `engine_gap` after static source inspection (no progressive tax liability, no earners levy, no KiwiSaver).
- Divergence report under `results/REPORT.md` (+ JSONL evidence). Awaiting `[HUMAN]` certification in `results/HUMAN_REVIEW.md`.

## Known blockers

- KiwiSaver RuleSpec module fails `axiom-rules-engine compile` (YAML `values` sequence vs map). Tracked upstream: https://github.com/TheAxiomFoundation/rulespec-nz/issues/79
- OpenFisca Aotearoa does not encode the overlapping calculations for this study's domains → study outcome is a **coverage/engine_gap finding**, not a numeric disagreement.
- Local OpenFisca Simulation could not be executed here (`openfisca-core` metaclass conflict with available NumPy); mapping is from checkout source inspection.

## Local checkouts

- `.external-repos/rulespec-nz` @ `3c6436b2ecf82dd7a7f7810a406a2695a64af33a` (pinned in inventory)
- `.external-repos/openfisca-aotearoa` (shallow clone of ServiceInnovationLab/openfisca-aotearoa)
- `.external-repos/axiom-rules-engine` (debug binary used for compile/run)
