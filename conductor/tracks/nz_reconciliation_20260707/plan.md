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
- [x] Task: Run comparative cross-engine simulations
    - [x] Materialise RuleSpec companion oracles for all inventory cases.
    - [x] Statically probe OpenFisca Aotearoa parameters/variables; record runtime install blockers.
    - [x] Write paired JSONL results + comparison rows under `studies/nz-reconciliation/results/`.
    - **Acceptance:** suite runs via `python -m nz_reconciliation.run_suite` and tests pass.
- [x] Task: Document any divergence or discrepancies found
    - [x] Publish `results/DIVERGENCE_REPORT.md` / `REPORT.md` with per-domain classifications.
    - [x] Classify gaps (engine coverage / compile block) distinctly from numeric disagreement.
    - **Acceptance:** report names evidence files and recommended next steps.
- [ ] Task: [HUMAN] Review and certify divergence reports
    - [ ] Present report packet to Dylan.
    - [ ] Record certification or requested follow-up scope change.
    - **Acceptance:** human decision recorded (accept findings, narrow scope, or spawn follow-up).

> CHECKPOINT (2026-07-09): Phase 2 agent execution complete.
> - 17/17 cases compared; **0 numeric agreements** (expected while OF outputs are empty gaps).
> - RuleSpec: 14 companion-oracle ok, 3 KiwiSaver compile-blocked (#79).
> - OpenFisca Aotearoa: 17/17 `engine_gap` — no schedule tax payable formula, rate params end `2010-10-01`, no earners levy, no KiwiSaver vars; core 41.x / 44.x runtime blocked in this environment.
> - Report: `studies/nz-reconciliation/results/DIVERGENCE_REPORT.md`.
> - Unit tests: 16 passed (`make nz-recon-test`).
>
> Remaining: human certification of the divergence packet.
