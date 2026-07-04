# AI governance

## Allowed uses

- Extract candidate concepts from source documents.
- Draft variable and parameter mappings.
- Generate tests and boundary cases.
- Suggest source references.
- Generate adapter code.
- Explain diffs for human review.
- Red-team schemas and examples.

## Disallowed uses

- Runtime eligibility or payment decisions.
- Final legal interpretation without human review.
- Silent mutation of canonical packages.
- Unreviewed schema changes.
- Deployment without deterministic conformance.

## Required controls

- Human approval for authoritative package releases.
- Deterministic validators and conformance suites.
- Reviewable AI-generated diffs.
- Provenance for AI-assisted changes.
- Versioned prompts and model details where AI materially influenced a package.
