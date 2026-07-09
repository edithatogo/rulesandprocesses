# Spec: Publication and demo closeout

## Overview

Close the remaining *optional* recommendations from the completed next-generation roadmap: a real Docassemble interview package for the OIA clock seam, arXiv-ready submission packets for the coupling and SNAP papers, and a refreshed external monitoring ledger. Does not invent new upstream proposals or promote golden fixtures.

## Scope

1. **Docassemble OIA clock package** under `demos/docassemble-oia-clock/` — interview YAML + pure-Python helper callable without a live Docassemble server; unit-tested against the staged `foi-o` `oia_rules` module.
2. **arXiv submission packets** for `papers/coupling/paper.md` and `studies/snap-divergence/paper/paper.md` — metadata, checklist, and `[HUMAN]` submit steps.
3. **Monitoring refresh** — `external/MAINTAINER_MONITORING.md` reflects open PRs and CI blockers.

## Out of scope

- Uploading to arXiv or choosing a journal venue (`[HUMAN]`).
- Promoting additional SNAP fixtures (already promoted 2026-07-06).
- Opening new PE/OF/Alaveteli/Axiom proposals while existing PRs are open.
- Forcing `fyi-cli` integration (deferred by design).
- Inventing OpenFisca formulas beyond already-opened PRs.

## Acceptance criteria

- Docassemble package has README, interview YAML, helper module, and green unit tests wired into `make check`.
- Both papers have an `ARXIV_SUBMISSION.md` packet with title, authors, abstract, categories, and a clear `[HUMAN]` submit checklist.
- Monitoring table lists every open upstream PR with current next action.
- Track archived after Phase 2 `[HUMAN]` packet is prepared (submission itself remains Dylan's gate).
