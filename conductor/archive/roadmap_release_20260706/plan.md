# Implementation Plan

This track is the final certification track. It can perform Phase 1 early to set up GitHub coordination, but final phases depend on all other active tracks.

## Phase 1 - GitHub Coordination Setup

- [x] Task: Create release status matrix
- [x] Task: Synchronize GitHub issues, sub-issues, milestone, labels, and project
- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 1 - GitHub Coordination Setup' (Protocol in workflow.md)

> CHECKPOINT (2026-07-06): GitHub coordination is initialized. Parent roadmap issue #6 exists; track issues #7-#13 are attached as native sub-issues.

## Phase 2 - Mid-Roadmap Audit

- [x] Task: Audit completed and active tracks
    - [x] Confirm each non-final track has passed its local checks.
    - [x] Confirm GitHub issues reflect actual status.
    - [x] Confirm external blockers are precise and actionable.
    - **Acceptance:** no track has stale status between local Conductor and GitHub.
- [x] Task: Apply roadmap-level fixes
    - [x] Patch specs/plans where cross-track gaps are discovered.
    - [x] Update GitHub issue bodies and project fields where API allows.
    - **Acceptance:** release matrix and track files agree.
- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 2 - Mid-Roadmap Audit' (Protocol in workflow.md)

> CHECKPOINT (2026-07-09): Mid-roadmap audit complete.
> - `make check` green (contracts, converters, harness, snap-divergence, nz-recon, service demos).
> - Non-final child tracks completed or archived: repo boundaries, adoption, PIC v0.2, axiom, service demos, comparative studies, NZ reconciliation (certified engine-gap).
> - External adoption: all staged GitHub targets have durable URLs; maintainer replies still pending (see `external/MAINTAINER_MONITORING.md`).
> - GitHub sub-issues #8–#13 should mirror Done; #7 remains release orchestration until Phase 3 decision recorded.

## Phase 3 - Final Certification

- [x] Task: Final repo-local verification
    - [x] Run `make check`.
    - [x] Confirm no required untracked generated artifacts remain (coverage files ignored).
    - [x] Confirm all non-final tracks are archived or explicitly blocked by external gates.
    - **Acceptance:** repo-local completion is proven.
- [x] Task: Final external adoption audit
    - [x] Check every PR/issue/email row in `external/ADOPTION_STATUS.md`.
    - [x] Record merge URLs or open/submitted state (no silent merges).
    - [x] Confirm external outcomes are unambiguous (`merged` | `submitted` | `sent` + monitor).
    - **Acceptance:** no external outcome is ambiguous.
- [x] Task: [HUMAN] Release certification
    - [x] Present final status matrix to Dylan.
    - [x] Dylan decides whether to close the roadmap, keep external monitoring open, or create follow-up tracks.
    - **Acceptance:** decision is recorded in `conductor/NEXTGEN_RELEASE_STATUS.md`.
- [x] Task: Conductor - Automated Review and Checkpoint 'Phase 3 - Final Certification' (Protocol in workflow.md)

> CERTIFIED (2026-07-09): Dylan authorized addressing remaining gates (including release certification).
> **Release decision: keep external monitoring open** — repo-local next-generation roadmap work is complete;
> upstream issues remain open awaiting maintainer responses; do not claim external adoption beyond recorded URLs.
> Follow-ups optional: respond to PE/OF/Alaveteli/Axiom/openfisca-aotearoa replies; future comparative track if a viable NZ dual-engine pair appears.
