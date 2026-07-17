# Canonical Cutover Consumer Inventory

Status: prepared for final human cutover review; the parent subtree remains the
only writable source until this inventory is reconciled.

## Destination

- Canonical candidate: `https://github.com/edithatogo/process-mappings`
- Migration commit: `d0257c1a99068262ea257643f3d6bdb57f2baee6`
- Destination governance issue: `process-mappings#1`
- Programme issue: `rac-conformance#50`
- Programme projects: Project 19 (delivery) and Project 14 (FOI programme)

## Consumer classes

| Consumer or reference | Current state | Cutover action |
| --- | --- | --- |
| PIC process-profile track and certification packet | Parent paths under `subrepos/process-mappings/` | Update implementation and evidence links to the destination after the canonical decision; retain immutable migration references. |
| Health-technology pathways track and source packet | Parent paths under `subrepos/process-mappings/` | Update implementation and evidence links to the destination after profile scope and source gates are satisfied. |
| Camunda portability track | Parent adapter path under `subrepos/process-mappings/adapters/` | Update adapter home and consumer instructions after the adapter demonstrator is certified. |
| Adverse-incident/open-disclosure archive | Historical parent evidence | Preserve archive provenance; update only forward-looking implementation links. |
| FOI profile and contract-consumption manifest | Parent subtree is currently executable by `make check` | Change the verifier to consume the pinned destination revision, then remove the writable parent copy in the same cutover change. |
| Parent README, roadmap, boundaries, and gate packets | Parent documentation names the subtree as provisional | Replace provisional wording with the canonical URL and migration policy after cutover approval. |
| Parent tests and validation scripts | Several defaults point at `subrepos/process-mappings/` | Make the canonical path explicit and ensure no test or script writes to the retired location. |

## Writable-path audit

The following parent paths currently contain or reference the incubator and must
be handled as one cutover transaction:

- `subrepos/process-mappings/`
- `tools/validate_process_mappings_contracts.py`
- `tools/validate_health_technology_matrix.py`
- `tools/process_mappings_rehearsal.py`
- `tools/rehearse_process_mappings_extraction.py`
- `tools/tests/test_process_mappings_*.py`
- active Conductor tracks #40, #42, and #43
- parent README, roadmap, boundary, and release-gate documents

No automation may continue writing to the retired parent profile or adapter
directories once the destination becomes canonical. The cutover change must
therefore update readers, tests, and documentation before deleting or replacing
the parent subtree.

## Completion criteria

Canonical cutover is ready for certification only when:

1. every forward-looking consumer has a destination URL and pinned revision;
2. parent validation reads the destination without network-dependent test
   behaviour in ordinary local checks;
3. the parent subtree is removed or replaced by a read-only provenance
   reference in the same reviewed change;
4. a clean parent checkout passes `make check`;
5. the destination clean clone passes its standalone checks; and
6. the final human decision records the cutover date, destination revision, and
   rollback pointer.

Until those conditions are met, the remote is a verified staged extraction, not
the canonical source of truth.
