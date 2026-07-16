# v1 Security, Licensing, and Claims Review

Review scope: current `codex/rac-v1-integration` working branch. A final
candidate commit and artifact set must be re-frozen after the remaining gates
are resolved.

## Verified locally

- `make check` passes, including repository audit and all declared local test,
  lint, example, converter, harness, study, and demo gates.
- `docs/V1_THREAT_MODEL.md` and `docs/V1_RISK_REGISTER.json` enumerate trust
  boundaries, threat classes, owners, controls, verification, and release
  dispositions.
- `docs/V1_VALIDATION_BASELINE.json` and `docs/V1_FUZZ_BASELINE.json` record
  bounded validation measurements and deterministic synthetic mutations.
- `docs/V1_SUPPLY_CHAIN_EVIDENCE.md` and `docs/V1_SBOM.json` record local
  workflow/dependency audits, lockfiles, SBOM evidence, and hosted-control
  limitations.
- GitHub Actions workflows use read-only contents permissions and immutable
  action references in the reviewed files.
- The candidate contains Apache-2.0 licensing metadata, `CITATION.cff`,
  `.zenodo.json`, `SECURITY.md`, dependency lock data, SBOM, checksums, and
  provenance.
- `docs/V1_SCOPE.md` excludes legal, clinical, funding, standards-body, and
  broad portability claims; candidate fixtures and AI-proposed mappings remain
  non-normative.

## Not locally certifiable

- Live dependency advisories, GitHub branch-protection status, hosted Actions
  results for this exact commit, secret-scanning results, and external source
  rights were not independently rechecked in this workspace.
- Mutation testing, cross-platform qualification, reproducible release-build
  comparison, rollback rehearsal, and hosted control verification remain open.
- Human approval is still required for release promotion, signing, package
  publication, DOI deposition, and announcements.

## Release disposition

`blocked`: no unresolved high/critical risk may be silently waived. This packet
is evidence for review, not a security certification or release authorization.
