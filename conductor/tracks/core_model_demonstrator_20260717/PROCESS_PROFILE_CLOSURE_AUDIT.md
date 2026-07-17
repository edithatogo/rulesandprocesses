# Process-Profile Closure Audit

Date: 2026-07-17  
Contract: `pic-process-profile/0.1.0`  
Status: pass for the focused core demonstrator scope

## Consumer and invariant coverage

| Normative field group | Named consumer(s) | Deterministic protection | Evidence |
| --- | --- | --- | --- |
| Profile identity, jurisdiction, applicability, observation | FOI-O baseline; future domain profiles | JSON Schema format/pattern checks; `observedAt >= applicableAt` | `contracts/process-profile/0.1.0/schema.json`; `pic_contracts.validation._process_profile_semantics` |
| States and transitions | FOI-O process definition; future adapters | Stable IDs and referential integrity for states, events, tasks, and source assertions | `CONSUMER_INVENTORY.md`; process-profile validator |
| Actors and authority links | FOI-O casework; adverse-incident review | Actor IDs are resolved; authority links are source-assertion references and are never inferred from labels | `CONSUMER_INVENTORY.md`; validator tests |
| Events and timestamps | FOI-O and `foi-process` evidence | Actor/source references are required; occurrence and observation ordering is checked | `SPEC.md`; `test_process_profile_schema.py` |
| Timers and deadlines | FOI-O statutory clocks; future health profiles | Start event and source references are resolved; calendar arithmetic remains in PIC rules/parameters | `DESIGN.md`; schema; validator |
| Human and deterministic tasks | FOI review; deterministic PIC rules | Human decisions require certified decision events; deterministic tasks require a rule invocation | `SPEC.md`; invalid task examples; validator tests |
| Rule invocations | PIC fixtures, parameters, and traces | Invocation references released contract IDs and a trace; deterministic flag is schema-constant | `CONSUMER_INVENTORY.md`; schema |
| Source assertions and effective dates | Every source-backed profile | Controlling assertions require official primary or human-approved status and `effectiveFrom`; other assertions remain non-controlling | `AUTHORITY_MODEL.md`; invalid authority/date examples; validator tests |
| Evidence references and traces | Conformance reports; optional adapters | Evidence hashes are schema-validated; trace links resolve and normalized projection is order-independent | `pic-foio-compatibility`; `pic_contracts.process_profile.normalize_trace`; determinism test |
| Exceptions | Human certification and exception review | Exceptions are preserved in the profile and are not converted into runtime decisions | `SPEC.md`; valid human-review example |

## Closure findings

- The profile is implementable without FOI-O, BPMN, DMN, FEEL, an ontology, or
  a workflow engine. Those systems are consumers or adapters, not normative
  dependencies.
- The validator fails closed for unqualified controlling assertions, missing
  effective dates, reversed source intervals, broken references, impossible
  event/profile times, and human tasks that do not point to certified human
  decisions.
- `normalize_trace` depends only on the profile document and trace ID. It
  sorts events by occurrence time and ID, rule invocations by ID, and loss
  notes lexically. Reordering source arrays therefore cannot change the
  projection.
- Source provenance remains intentionally bounded in `0.1.0`: the schema
  records URI, retrieval time, effective interval, source type, review state,
  authority class, and controlling status. Issuer, rights, digest, and named
  consumer remain source-pack or governance metadata until a versioned schema
  change is proposed and consumed.
- No candidate profile or fixture is promoted by this audit. Promotion and
  legal/source certification remain human gates.

## Verification

The focused closure change passes the process-profile corpus, including valid
and invalid examples and the order-independence regression. The repository
gate is recorded by the focused track checkpoint after `make check`.
