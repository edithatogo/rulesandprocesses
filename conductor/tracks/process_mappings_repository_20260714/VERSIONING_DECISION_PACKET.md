# Process-Mappings Versioning Decision Packet

Status: recommendation prepared; no tag or release has been created.

## Current state

- Repository: `https://github.com/edithatogo/process-mappings`
- Branch: `main`
- Migration commit: `d0257c1a99068262ea257643f3d6bdb57f2baee6`
- Existing tags: none
- Existing releases: none
- Canonical status: staged public extraction; the parent remains authoritative

## Recommendation

Approve `0.1.0` as the first public pre-1.0 release after canonical cutover is
certified. Do not use an `-incubation` suffix: the repository boundary and
hosted controls are already public, while the pre-1.0 major version communicates
that the profile and adapter APIs are not stable.

The release must not be created until the parent consumer migration is complete
and the source-of-truth decision is recorded. A tag alone must never be treated
as evidence of legal, clinical, or process certification.

## Proposed policy

- `0.1.x`: backward-compatible documentation, fixture, source-ledger, and
  validation fixes that do not alter the profile or adapter contract.
- `0.2.0`: incompatible changes to the process-profile or adapter contract,
  with migration notes and regenerated validation evidence.
- `1.0.0`: only after the v1 release gates, source certification, independent
  validation, and the relevant consumer evidence are complete.
- Profile content and optional platform adapters may identify their own schema
  revisions, but must retain the repository release and immutable source
  revision that produced them.
- No release may promote `agent-proposed` mappings or imply controlling legal,
  clinical, funding, or policy authority.

## Human decision

Approve or amend the recommended initial release policy:

> Approve `0.1.0` as the first public pre-1.0 process-mappings release,
> subject to canonical cutover certification; do not create the tag yet.

This decision is separate from approval of canonical cutover and does not
authorize a release, profile promotion, or source certification.
