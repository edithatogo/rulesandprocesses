# v1 Hosted Governance Verification

Observed: 2026-07-16 via the authenticated GitHub API for
`edithatogo/rac-conformance`.

## Repository security settings

- Repository is public and `main` is the default branch.
- Secret scanning is enabled.
- Secret-scanning push protection is enabled.
- Dependabot security updates are enabled.
- Secret validity checks and non-provider-pattern scanning are disabled.

## Main branch protection

- Strict required checks are enabled.
- One approving review is required and code-owner review is required.
- Required checks are `check`, `full-check`, `analyze`, `CodeQL`,
  `dependency-review`, `workflow-lint`, `workflow-security`, and all four
  v1 matrix jobs for Ubuntu/macOS and Python 3.12/3.13.
- Admin enforcement, linear history, conversation resolution, no force-push,
  and no deletion are enabled.
- Required commit signatures are disabled.

## Remaining hosted limitations

This verification does not establish protected release environments, signed
release tags, artifact attestations, or an external independent implementation.
Those remain explicit v1 release gates. Secret validity checks and scanning of
non-provider patterns should be enabled only after reviewing their operational
false-positive and remediation impact.
