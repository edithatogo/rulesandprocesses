# arXiv submission packet — SNAP divergence study

**Status:** ready for `[HUMAN]` review / submit  
**Prepared:** 2026-07-09  
**Source draft:** [`paper.md`](paper.md)

## Proposed metadata

| Field | Value |
|---|---|
| Title | Independent Rules-as-Code Implementation Agreement and Divergence Study: SNAP Eligibility and Allotments in PolicyEngine and the Policy Rules Database (PRD) |
| Authors | Dylan Mordaunt |
| Corresponding | Dylan Mordaunt (`edithatogo`) |
| License | CC-BY-4.0 for the paper text; study code Apache-2.0 |
| Primary category | `cs.CY` |
| Cross-lists (optional) | `econ.GN` only if appropriate; prefer `cs.SE` for methods |
| Comments | Companion empirical study to the PIC coupling paper. Fixtures: 50 human-promoted agreement cases (2026-07-06). |

## Abstract (paste into arXiv)

Rules-as-Code (RaC) promises to improve the precision, transparency, and consistency of public benefits programs by translating statutory and regulatory texts into executable code. However, a critical question remains: do independent implementations of the same legislative rules yield identical results? This paper presents a systematic, differential-testing evaluation of two leading RaC engines—PolicyEngine (Python) and the Atlanta Fed Policy Rules Database (PRD, R)—implementing the Supplemental Nutrition Assistance Program (SNAP) for Federal Fiscal Year 2026. Testing against a corpus of 65 human-curated and AI-proposed scenarios across five states (California, Texas, Pennsylvania, Mississippi, and Georgia) reveals a 100% output agreement rate (50 out of 50) for core compliance scenarios. For the remaining 15 held cases, we document and classify structural differences in state-option modeling, utility deduction triggers, and parameter surfaces.

## Artifact links

- Study root: https://github.com/edithatogo/rulesandprocesses/tree/main/studies/snap-divergence
- Golden fixtures: `studies/snap-divergence/fixtures/snap-fy2026-fixtures.json` (human-promoted 2026-07-06)
- Report: `studies/snap-divergence/REPORT.md`
- DBN outreach draft: `external/dbn/EMAIL.md` (already sent; monitor reply)

## `[HUMAN]` checklist

1. [ ] Read `paper.md`; replace AI-pair author credit with preferred byline.
2. [ ] Confirm 50/50 agreement claim matches `REPORT.md` / promoted fixtures.
3. [ ] Ensure PRD / PolicyEngine licenses and citations are preserved in the PDF.
4. [ ] Submit to arXiv **or** defer; optionally pair with IJM venue decision.
5. [ ] If submitted: paste arXiv ID/URL here.

## Decision log

| Date | Decision | By |
|---|---|---|
| 2026-07-09 | Packet prepared; submission pending | Agent (authorized closeout) |
| | | |
