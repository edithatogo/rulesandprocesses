# Freedom of Information programme governance

## Objective

Use GitHub Project 14, Rare Insights Freedom of Information, as the focused
cross-repository programme board while preserving each repository's dedicated
Conductor roadmap as its implementation source of truth.

## In-scope repositories

- `edithatogo/foi-o`
- `edithatogo/fyi-cli`
- `edithatogo/fyi-archive`
- `edithatogo/nlp-policy-nz`
- `edithatogo/rac-conformance`
- `edithatogo/legislation`, limited to FOI legislation source work
- `edithatogo/alaveteli`, limited to upstream workflow/state intelligence

## Rules

- Mirror only FOI-relevant issues and pull requests into Project 14.
- Do not mirror every issue from broad repositories such as `nlp-policy-nz`,
  `legislation`, `rac-conformance`, or the Alaveteli fork.
- Represent Alaveteli as a read-only intelligence/reference dependency unless
  a separately authorized upstream contribution exists.
- Keep local Conductor plans authoritative and Project fields synchronized.
- Track jurisdiction, repository role, dependency, evidence status, human gate,
  and delivery status for cross-repository items.
- Do not use Project 4 or Project 19 as substitutes for this FOI-focused board.

## Acceptance criteria

- Project 14 documentation names every in-scope repository and its boundary.
- The current FOI-O, archive, NLP, legislation, and RaC issues appear on Project 14.
- Dedicated repository Projects retain their existing items and status.
- A repeatable sync contract documents inclusion filters and prevents unrelated
  open-policy, NLP, legislation, or rules-as-code work from leaking onto the board.
- Project status never implies legal validation, publication, or upstream acceptance.
