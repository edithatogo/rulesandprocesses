# Plan: external_adoption_20260711

## Phase 1 - Evidence refresh

- [x] Task: Refresh all seven PR branches, checks, reviews, and issue linkages
- [x] Task: Reproduce each contributor-controlled test surface and record versions
- [x] Task: Conductor - Automated Review and Checkpoint 'Evidence refresh' (Protocol in workflow.md)

> CHECKPOINT (2026-07-11): All seven PRs remain open and mergeable. PolicyEngine #515-#517 have no upstream check rollup and require maintainer workflow approval. OpenFisca #1382, Alaveteli #9356, and OpenFisca Aotearoa #200 remain review-required with empty check rollups. RuleSpec NZ #80 is mergeable; quality/roadmap/shard checks pass but validation fails because the changed KiwiSaver source lacks a signed generated manifest. Local branch evidence and upstream URLs are recorded in `external/UPSTREAM_PR_AUDIT.md` and `external/MAINTAINER_MONITORING.md`.

## Phase 2 - Review response

- [x] Task: Apply actionable maintainer feedback with focused regression tests
- [x] Task: Resolve contributor-controlled CI failures and conflicts
- [ ] Task: [HUMAN] Supply or request maintainer-only workflow approvals, signing, and merge decisions
- [ ] Task: Conductor - Automated Review and Checkpoint 'Review response' (Protocol in workflow.md)

> BLOCKED (2026-07-11): Remaining work requires upstream maintainer workflow approval/review and an Axiom signing key. No contributor-controlled fix can clear these external gates.

## Phase 3 - Adoption closeout

- [ ] Task: Record merged, declined, superseded, or externally blocked disposition for every contribution
- [ ] Task: Update Project 19 and repository ledgers from URL evidence
- [ ] Task: Conductor - Automated Review and Checkpoint 'Adoption closeout' (Protocol in workflow.md)
