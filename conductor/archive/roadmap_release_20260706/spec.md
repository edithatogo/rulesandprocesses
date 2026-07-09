# Next-Generation Roadmap Release Orchestration

## Overview

The next-generation roadmap spans several tracks and external gates. This track owns the program-level release matrix, dependency order, GitHub issue/project synchronization, and final completion certification.

## Functional Requirements

1. Maintain `conductor/NEXTGEN_RELEASE_STATUS.md` as the release control document.
2. Track every active Conductor track, GitHub issue, sub-issue relationship, milestone, project item, CI state, PR state, and external gate.
3. Ensure every active track has:
   - local `spec.md`, `plan.md`, `metadata.json`;
   - one GitHub issue with hidden `conductor-track-id` marker;
   - parent/sub-issue linkage under the roadmap issue where supported;
   - milestone and project assignment;
   - closure criteria.
4. Define final certification levels:
   - repo-local complete;
   - submitted upstream;
   - under review;
   - merged;
   - declined;
   - blocked by external actor;
   - superseded.
5. Produce final closeout only after all tracks are archived or explicitly blocked by external gates.

## Non-Functional Requirements

- Do not weaken individual track acceptance criteria.
- Do not claim external completion without URLs or logged evidence.
- Keep local Conductor as source of truth; GitHub mirrors coordination state.

## Acceptance Criteria

- `conductor/NEXTGEN_RELEASE_STATUS.md` exists and is current.
- All active tracks are represented in GitHub Issues and the project board.
- Native sub-issue links are created when supported by GitHub API/permissions, otherwise fallback links are recorded.
- Final release status distinguishes repo-local completion from external adoption.
- `make check` and GitHub Actions pass before final certification.

## Out Of Scope

- Implementing the child tracks.
- Forcing external maintainers to merge.
- Replacing Conductor plans with GitHub Project fields.
