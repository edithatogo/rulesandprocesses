# Process Profile Compatibility Matrix

As at 2026-07-15. This matrix records repository-local validation only; it does
not certify external adoption, legal authority, or human promotion.

| Consumer | Contract | Evidence | Status | Limitation |
| --- | --- | --- | --- | --- |
| FOI-O staged traces | `pic-process-profile/0.1.0` candidate | `subrepos/process-mappings/profiles/foi/PROFILE_CANDIDATES.json`; process-profile corpus | Candidate-compatible | Mappings remain agent-proposed and source notes are not live-verified |
| Docassemble OIA demo | `pic-process-profile/0.1.0` concept inventory | `demos/docassemble-oia-clock/`; `contracts/process-profile/CONSUMER_INVENTORY.md` | Inventory-compatible | Demo adapter is not a certified profile implementation |
| Axiom/PolicyEngine trace harness | PIC trace dependency | `harness/tests/`; process-profile inventory | Evidence consumer | Engine traces are optional adapter evidence, not process-profile authority |
| Health-technology pathway track | Future process-profile consumer | `conductor/tracks/health_technology_pathways_20260714/spec.md` | Not implemented | No health mappings or patient-level data are present |
| Camunda portability track | Future projection consumer | `conductor/tracks/camunda_portability_20260714/spec.md` | Not implemented | No platform runtime or BPMN mapping is part of the contract |

## Gate commands

The repository gate is:

```sh
FOI_PROGRAMME_REPO_ROOT=/Volumes/PortableSSD/GitHub make check
```

The process-profile schema corpus is exercised by the contract-tool tests and
the general example validator. A consumer may claim compatibility only for a
specific contract commit, profile version, evidence corpus, jurisdiction, and
source status.
