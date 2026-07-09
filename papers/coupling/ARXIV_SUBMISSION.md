# arXiv submission packet — coupling paper

**Status:** ready for `[HUMAN]` review / submit  
**Prepared:** 2026-07-09  
**Source draft:** [`paper.md`](paper.md)

## Proposed metadata

| Field | Value |
|---|---|
| Title | Coupling Statutory Rules and Administrative Processes: A Pragmatic Contract-Based Approach to Rules-as-Code |
| Authors | Dylan Mordaunt |
| Corresponding | Dylan Mordaunt (`edithatogo`) |
| License | CC-BY-4.0 for the paper text; code/schemas Apache-2.0 (see repo `LICENSE`) |
| Primary category | `cs.CY` (Computers and Society) |
| Cross-lists (optional) | `cs.SE`, `cs.AI` (only if arXiv moderators accept; do not over-claim AI) |
| Comments |  Draft companion paper to the SNAP divergence study and foi-o OIA rules module. |

## Abstract (paste into arXiv)

Rules-as-Code (RaC) initiatives typically focus on rules-heavy domains (such as tax-benefit calculations) or process-heavy domains (such as public record lifecycle tracking) in isolation. However, actual administrative operations require coupling these two surfaces. This paper presents a pragmatic, contract-based approach to coupling statutory rules and administrative processes. We define a lightweight Policy Interchange Contract (PIC) schema that acts as a boundary between process state machines (like foi-o for official information requests) and isolated rules modules. We evaluate this approach across two distinct case studies: Official Information Act (OIA) clocks in New Zealand, and a multi-state SNAP eligibility study. Our results demonstrate that decoupled rules modules can achieve 100% differential testing parity while maintaining strict import-graph isolation and preserving non-computable discretion points.

## Artifact links (include in comments / paper)

- Repository: https://github.com/edithatogo/rulesandprocesses
- OIA rules consumer: https://github.com/edithatogo/foi-o (PRs #20, #21)
- SNAP study: `studies/snap-divergence/`
- Cite software: `CITATION.cff`

## `[HUMAN]` checklist

1. [ ] Read `paper.md`; fix author line (remove “Antigravity” if undesired on arXiv).
2. [ ] Confirm claims table still matches current repo paths (foi-o now on upstream `main`).
3. [ ] Convert to arXiv-acceptable PDF (LaTeX or pandoc); keep decimal money as strings in any tables.
4. [ ] Submit to arXiv **or** defer and record decision below.
5. [ ] If submitted: paste arXiv ID/URL here and update `external/ADOPTION_STATUS.md` / release status.

## Decision log

| Date | Decision | By |
|---|---|---|
| 2026-07-09 | Packet prepared; submission pending | Agent (authorized closeout) |
| | | |
