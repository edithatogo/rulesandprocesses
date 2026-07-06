# Implementation Plan

This track is the final certification track. It can perform Phase 1 early to set up GitHub coordination, but final phases depend on all other active tracks.

## Phase 1 - GitHub Coordination Setup

- [x] Task: Create release status matrix
    - [x] Create `conductor/NEXTGEN_RELEASE_STATUS.md`.
    - [x] List all active tracks, dependencies, GitHub issue URLs, project status, CI status, and external gates.
    - [x] Include certification levels for repo-local and external outcomes.
    - **Acceptance:** every active track has a row and a known next action.
- [x] Task: Synchronize GitHub issues, sub-issues, milestone, labels, and project
    - [x] Create or update parent roadmap issue.
    - [x] Create or update one issue per active track with hidden `conductor-track-id` marker.
    - [x] Add track issues as native sub-issues under the parent issue where supported.
    - [x] Assign milestone and add to `Rules and Processes Integration Dashboard`.
    - [x] Apply labels for Conductor track, workstream, CI, external gate, and human gate.
    - **Acceptance:** GitHub issue/project state is recorded in `conductor/NEXTGEN_RELEASE_STATUS.md`.
- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 1 - GitHub Coordination Setup' (Protocol in workflow.md)

> CHECKPOINT (2026-07-06): GitHub coordination is initialized. Parent roadmap issue #6 exists; track issues #7-#13 are attached as native sub-issues, assigned to the `Next-generation roadmap` milestone, labelled, and added to the Rules and Processes Integration Dashboard. Prior completed issues #1-#5 are closed and marked Done in the project. Remaining Phase 1 work is review/validation only.

## Phase 2 - Mid-Roadmap Audit

- [ ] Task: Audit completed and active tracks
    - [ ] Confirm each non-final track has passed its local checks.
    - [ ] Confirm GitHub issues reflect actual status.
    - [ ] Confirm external blockers are precise and actionable.
    - **Acceptance:** no track has stale status between local Conductor and GitHub.
    > BLOCKED (2026-07-06): The roadmap release track cannot finish its audit or final certification until the remaining active child tracks complete their own checks, checkpoints, and any required human/external gates.
- [ ] Task: Apply roadmap-level fixes
    - [ ] Patch specs/plans where cross-track gaps are discovered.
    - [ ] Update GitHub issue bodies and project fields.
    - **Acceptance:** release matrix and track files agree.
- [ ] Task: Conductor - Automated Review and Checkpoint 'Phase 2 - Mid-Roadmap Audit' (Protocol in workflow.md)

## Phase 3 - Final Certification

- [ ] Task: Final repo-local verification
    - [ ] Run `make check`.
    - [ ] Confirm no untracked generated files remain.
    - [ ] Confirm all non-final tracks are archived or explicitly blocked by external gates.
    - **Acceptance:** repo-local completion is proven.
- [ ] Task: Final external adoption audit
    - [ ] Check every PR/issue/email row in `external/ADOPTION_STATUS.md`.
    - [ ] Record merge URLs or blockers.
    - [ ] Confirm GitHub issues/sub-issues reflect completion or external blocking state.
    - **Acceptance:** no external outcome is ambiguous.
- [ ] Task: [HUMAN] Release certification
    - [ ] Present final status matrix to Dylan.
    - [ ] Dylan decides whether to close the roadmap, keep external monitoring open, or create follow-up tracks.
    - **Acceptance:** decision is recorded in `conductor/NEXTGEN_RELEASE_STATUS.md`.
- [ ] Task: Conductor - Automated Review and Checkpoint 'Phase 3 - Final Certification' (Protocol in workflow.md)
