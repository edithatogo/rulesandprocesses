# Implementation Plan

Depends on: `repo_boundaries_20260706` Phase 1. Use `conductor/edithatogo-repo-boundaries.md` before touching any external repo.
Also depends on `roadmap_release_20260706` Phase 1 for GitHub issue/project synchronization.

## Phase 1 - Adoption Inventory

- [x] Task: Build adoption ledger
    - [x] Read every `external/*/SUBMISSION*.md`, `external/dbn/LOG.md`, and archived plan checkpoint that mentions upstream submission.
    - [x] Create `external/ADOPTION_STATUS.md` with target, artifact, status, URL, CI state, owner, and next action columns.
    - [x] Mark unknown external status as `needs_verification`, not complete.
    - **Acceptance:** every staged external artifact has one ledger row.
- [x] Task: Link adoption ledger to GitHub roadmap issue hierarchy
    - [x] Read `conductor/github-planning.md`.
    - [x] Add GitHub issue/project URL columns where useful.
    - [x] Ensure external-gate and human-gate labels are applied to relevant track issues.
    - **Acceptance:** adoption rows can be traced to GitHub issues or explicit non-GitHub contacts.
- [x] Task: Verify live external state
    - [x] Use GitHub CLI/API for issue/PR state where available.
    - [x] Check DBN log and any available mailbox/thread evidence only when the relevant connector/tool is available and authorized.
    - [x] Record exact URLs or "not found / not accessible".
    - **Acceptance:** no row remains uninspected unless access is blocked and logged.
- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 1 - Adoption Inventory' (Protocol in workflow.md)


## Phase 2 - Patch-Ready External Bundles

- [x] Task: Prepare `foi-o` PR bundle
    - [x] Confirm local `foi-o` branch status before editing.
    - [x] Apply the staged OIA rules module into the `foi-o` checkout or refresh the patch bundle, respecting existing user changes.
    - [x] Run `foi-o` tests relevant to the rules module.
    - [x] Commit in the external repo only if changes are authorized and scoped. No external commit was needed because the bundle was already present and verified locally.
    - **Acceptance:** PR-ready branch or patch bundle exists; CI/test command output is logged.
    > CHECKPOINT (2026-07-06): `foi-o` checkout is clean on `main`, the staged OIA rules module already exists under `external/foi-o/`, and `uv run pytest tests/test_oia_rules.py` plus coverage passed in the external repo. The bundle is ready for Dylan's human submission step.
- [x] Task: Prepare PolicyEngine/OpenFisca issue and PR follow-through
    - [x] Verify whether trace, missingness, and converter submissions are already open.
    - [x] If not open, prepare final issue/PR text and mark `[HUMAN]` submission gate.
    - [x] If open, monitor responses and apply requested documentation/code fixes in this repo or external repo as appropriate.
    - **Acceptance:** every PolicyEngine/OpenFisca artifact has live URL, human gate, or blocked reason.
    > CHECKPOINT (2026-07-06): No matching upstream PolicyEngine/OpenFisca issues were found. The draft issue/PR texts are already staged under `external/policyengine/` and `external/openfisca/`, and the remaining step is Dylan's human submission gate.
- [x] Task: Prepare Alaveteli follow-through
    - [x] Verify whether the Alaveteli state-taxonomy discussion/issue exists.
    - [x] If not, prepare final discussion text and mark `[HUMAN]` submission gate.
    - [x] If open, record response and next action.
    - **Acceptance:** Alaveteli status is not ambiguous.
    > CHECKPOINT (2026-07-06): No matching upstream Alaveteli issue/discussion was found. The staged proposal text is already present in `external/alaveteli/SUBMISSION.md`, and the remaining step is Dylan's human submission gate.
- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 2 - Patch-Ready External Bundles' (Protocol in workflow.md)

> CHECKPOINT (2026-07-06): The `foi-o` bundle is verified in a clean external checkout with passing tests and coverage. PolicyEngine/OpenFisca converter, trace, and missingness drafts are staged locally, and Alaveteli's request-state proposal is staged locally. No matching upstream issue was open for those drafts at verification time, so the remaining work is Dylan's human submission gate.

## Phase 3 - CI, Review, And Merge Closure

- [x] Task: Monitor active PRs and GitHub Actions
    - [x] For every live PR, record latest commit SHA, required checks, pass/fail state, and reviewer state.
    - [x] Apply fixes for agent-addressable failures where the agent has push authority.
    - [x] Commit each fix with the external repo's conventions.
    - **Acceptance:** all agent-addressable CI failures are fixed or precisely blocked.
    > CHECKPOINT (2026-07-06): No live PRs exist for the staged adoption artifacts at verification time. The external PRs visible in the target repositories are unrelated to the current staged submissions, so there was nothing agent-addressable to fix here.
- [x] Task: Reconcile GitHub Projects status fields
    - [x] Confirm project items match local track and adoption ledger states.
    - [x] Use parent issue/sub-issue progress to report completion.
    - [x] Update issue comments with CI and PR URLs when status changes.
    - **Acceptance:** GitHub project state is not stale relative to local docs.
- [x] Task: Update adoption ledger and README summary
    - [x] Refresh `external/ADOPTION_STATUS.md`.
    - [x] Add a short status pointer in `README.md` or `conductor/tracks.md` if appropriate.
    - **Acceptance:** repo-local documentation matches live external state.
- [x] Task: [HUMAN] Merge or maintainer-response gate
    - [x] Present merge-ready PRs and external-response queue to Dylan.
    - [x] Record which PRs Dylan merges, which require maintainer review, and which are intentionally deferred.
    - **Acceptance:** no PR is represented as merged without URL evidence.

> CHECKPOINT (2026-07-09): Authorized submission batch completed.
> - `edithatogo/foi-o` OIA rules: [PR #20](https://github.com/edithatogo/foi-o/pull/20) **merged** (`d2f5dbd`).
> - `TheAxiomFoundation/rulespec-nz` KiwiSaver compile: [issue #79](https://github.com/TheAxiomFoundation/rulespec-nz/issues/79) **submitted**.
> - PolicyEngine: issues [#512](https://github.com/PolicyEngine/policyengine-core/issues/512), [#513](https://github.com/PolicyEngine/policyengine-core/issues/513), [#514](https://github.com/PolicyEngine/policyengine-core/issues/514) **submitted**.
> - OpenFisca: issues [#1380](https://github.com/openfisca/openfisca-core/issues/1380), [#1381](https://github.com/openfisca/openfisca-core/issues/1381) **submitted**.
> - Alaveteli: [issue #9355](https://github.com/mysociety/alaveteli/issues/9355) **submitted**.
> - DBN email remains `sent` / monitor-only.
>
> Remaining work is **maintainer-response monitoring**, not further agent submission. No row is marked merged without URL evidence.

- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 3 - CI, Review, And Merge Closure' (Protocol in workflow.md)

> CHECKPOINT (2026-07-09): Phase 3 closed for agent submission duties. Ledger holds durable URLs for every GitHub-target adoption row. Track remains open only for passive monitoring of maintainer replies unless a follow-up track is created.
