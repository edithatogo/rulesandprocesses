# GitHub Planning Integration

Last updated: 2026-07-06.

Local Conductor files remain the detailed source of truth. GitHub Issues and Projects are the cross-repo execution ledger for visibility, CI, review, and external adoption state.

## Required GitHub Shape

- One parent issue represents the next-generation roadmap.
- Each active Conductor track is represented by one GitHub issue.
- Track issues are linked to the parent issue as native GitHub sub-issues where the API/UI supports it.
- Every track issue includes a hidden marker:
  - `<!-- conductor-track-id: <track_id> -->`
- Track issues should be added to the `Rules and Processes Integration Dashboard` project.
- The project should show `Parent issue` and `Sub-issues progress` fields.
- Track issues should use a milestone for the roadmap release.

## Recommended Labels

| Label | Purpose |
|---|---|
| `conductor-track` | Issue mirrors a local Conductor track. |
| `roadmap-nextgen` | Next-generation roadmap work. |
| `external-gate` | Depends on maintainer, reviewer, upstream, or email response. |
| `ci-required` | Requires local checks and GitHub Actions monitoring. |
| `human-gate` | Dylan must approve, submit, merge, or decide. |
| `repo-boundary` | Work is constrained by repo relevance boundaries. |
| `adoption` | External adoption or upstream follow-through. |
| `contract` | PIC contract/schema work. |
| `validation-harness` | Harness, runner, or differential-validation work. |
| `service-demo` | Demo or integration surface work. |
| `comparative-study` | Comparative study selection and execution. |
| `release` | Roadmap release orchestration and certification. |
| `github-project` | Work item is mirrored in GitHub Projects. |

## Project Features To Use

- **Sub-issues:** model parent roadmap -> track issues -> optionally phase issues if a track becomes large.
- **Parent issue and Sub-issues progress fields:** expose roadmap progress without duplicating status text.
- **Issue dependencies:** use `blocked by` / `blocking` relationships for true cross-track blockers that are actionable in GitHub. Do not encode every Conductor ordering rule as a dependency.
- **Milestones:** use one milestone per roadmap release or external closeout window.
- **Labels:** separate local implementation, CI, external gates, and human gates.
- **Project views:** maintain at least:
  - `Roadmap hierarchy`: table with hierarchy visible.
  - `External gates`: filtered by `external-gate` or `human-gate`.
  - `CI / PR readiness`: filtered by `ci-required`.
  - `By track`: grouped by parent issue or milestone.
  - `Review queue`: filtered by linked PRs, reviewers, and `human-gate`.
- **Pull request linking:** every implementation PR should reference the relevant track issue and local track path.
- **Custom fields, if needed:** add small single-select fields only for durable workflow concepts such as `Certification level` or `External state`. Avoid free-text fields that duplicate Conductor plans.

## What Not To Use Yet

- Do not use GitHub Projects as the primary source of requirements. Specs and plans remain in `conductor/tracks/*`.
- Do not use project-only draft items for executable work once a track exists; use issue-backed items.
- Do not represent external merges as complete without a URL or recorded blocker.
- Do not create phase-level sub-issues unless the parent track is too large to review as one issue.
