# Plan: NZ RuleSpec vs OpenFisca Aotearoa Reconciliation

## Phase 1 - Scaffolding
- [x] Task: Create reconciliation runner script
    - [x] Add deterministic comparison module under `studies/nz-reconciliation/runner/`.
    - [x] Add inventory CLI scaffold (`run_inventory.py`).
    - [x] Wire `make nz-recon-lint` / `make nz-recon-test` into `make check`.
    - **Acceptance:** unit tests pass; runner exits cleanly without live engines.
- [x] Task: Set up test case inventory
    - [x] Extract ≥15 companion-test cases for income tax, ACC earners levy, and KiwiSaver from pinned `rulespec-nz`.
    - [x] Record OpenFisca Aotearoa mapping status and known compile blockers.
    - **Acceptance:** `fixtures/case-inventory.json` has ≥15 cases across all three domains.

> CHECKPOINT (2026-07-09): Phase 1 scaffolding is complete. Inventory has 17 cases (5 income tax, 9 ACC, 3 KiwiSaver) from `rulespec-nz` @ `3c6436b2`. Comparison and inventory unit tests pass. KiwiSaver RuleSpec compile remains blocked (upstream issue #79). OpenFisca Aotearoa checkout is available under `.external-repos/openfisca-aotearoa` for Phase 2 mapping.

## Phase 2 - Execution & Reconciliation
- [ ] Task: Run comparative cross-engine simulations
- [ ] Task: Document any divergence or discrepancies found
- [ ] Task: [HUMAN] Review and certify divergence reports
