# Plan: Publication and demo closeout

## Phase 1 — Docassemble package + monitoring

- [x] Task: Add Docassemble OIA clock interview package under `demos/docassemble-oia-clock/`
    - [x] Interview YAML (receipt date → deadline + trace)
    - [x] Pure-Python helper wrapping `foi_o_nz.oia_rules`
    - [x] Unit tests + Makefile targets included in `make check`
    - **Acceptance:** `make service-boundaries-test` and new docassemble tests green; README documents install/run limits (no live Docassemble required for CI).
- [x] Task: Refresh `external/MAINTAINER_MONITORING.md` with open PR URLs and CI blockers
    - **Acceptance:** table matches live GitHub state for rulespec-nz#80, PE#515–517, OF#1382, Alaveteli#9356, OF-aotearoa#200.
- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 1' (Protocol in workflow.md)

> CHECKPOINT (2026-07-09): Phase 1 complete. Docassemble package tests green (`make docassemble-oia-clock-test`); monitoring table refreshed with open PR URLs.

## Phase 2 — arXiv packets + [HUMAN] gate

- [x] Task: Write `papers/coupling/ARXIV_SUBMISSION.md`
- [x] Task: Write `studies/snap-divergence/paper/ARXIV_SUBMISSION.md`
- [ ] Task: [HUMAN] Review packets; submit to arXiv and/or choose venue
    - [ ] Present packets to Dylan.
    - [ ] Record submit URL or deferral in packet / release status.
    - **Acceptance:** human decision recorded (submitted | deferred | venue TBD).
- [ ] Task: Conductor - Automated Review and Checkpoint 'Phase 2' (Protocol in workflow.md)
