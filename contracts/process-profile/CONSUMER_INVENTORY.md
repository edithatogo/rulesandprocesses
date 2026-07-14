# PIC Process Profile Consumer Inventory

Status: draft for process-profile design  
Owner: PIC maintainers  
Last reviewed: 2026-07-15

This inventory is the boundary for the first process-profile version. A field
may enter the normative contract only when a current consumer and evidence
artifact are named. This is a consumer inventory, not a proposal for a global
ontology, BPMN replacement, or workflow-engine API.

## Consumers and evidence

| Consumer | Evidence artifact | What it consumes | Boundary |
| --- | --- | --- | --- |
| FOI-O OIA rules | `external/foi-o/rules/traces/*.json` and `external/foi-o/rules/DESIGN.md` | Rule invocation, input/output value states, decision identifiers, parameter versions, source references, human-discretion signals, and trace step order | FOI-O remains semantic and jurisdictional authority; the profile records compatibility and loss |
| FOI-O event vocabulary | `external/foi-o/rules/DESIGN.md` | Transfer, deadline, extension, refusal, and review-related event references | Existing FOI-O event names are consumed as evidence; no new generic event ontology is introduced |
| Docassemble-shaped OIA demo | `demos/docassemble-oia-clock/src/oia_clock_demo/evaluate.py` and `demos/docassemble-oia-clock/tests/test_evaluate.py` | A case input, deterministic rule invocation, response deadline output, trace step, adapter identifier, and source reference | The demo is an adapter/example, not a legal decision-maker or core runtime dependency |
| Service-boundary examples | `demos/service-boundaries/examples/*.json` and `demos/service-boundaries/src/service_boundary_demos/core.py` | Request/response envelope, service name, operation, typed result, trace, and explicit boundary errors | Service envelopes remain non-normative examples; no platform-specific transport is required |
| PIC trace projection harness | `harness/policyengine_trace/projection.py` and `harness/tests/test_policyengine_trace_projection.py` | Case ID, input variables, dependency-ordered steps, decision IDs, parameter versions, output values, and source references | PolicyEngine is an optional adapter/evidence source; its flat trace is not the process-profile authority |
| Axiom harness | `harness/axiom/adapter.py`, `harness/axiom/runner.py`, and `harness/tests/test_axiom_harness.py` | Fixture case ID, rule invocation, normalized output, trace, comparison status, and adapter failure | Axiom/OpenFisca-compatible execution remains an adapter and independent-oracle boundary |
| Health-technology pathway track | `conductor/tracks/health_technology_pathways_20260714/spec.md` | Planned authority, jurisdiction, indication, decision owner, stage, exception, review, and post-market handoff concepts | No health mapping is implemented or certified by this inventory; no patient-level or confidential data is a consumer |

## Candidate field inventory

| Field or concept | Consumer(s) | Cardinality | Time semantics | Failure behavior |
| --- | --- | --- | --- | --- |
| `processId` | FOI-O, Docassemble, service examples, health track | exactly one per profile | Stable identifier; not a date | Reject missing or reused identifier |
| `processDefinitionVersion` | FOI-O traces, health track | exactly one per profile | Version effective date required when supplied | Hold if version is absent where comparison requires it |
| `caseId` | FOI-O traces, demos, harnesses | exactly one per trace | Identifies a synthetic or permitted evidence case | Reject trace without a case identifier |
| `jurisdiction` | FOI-O, health track | exactly one when jurisdictional | Applies to the profile and source scope | Reject cross-jurisdiction comparison without explicit overlay |
| `state` | FOI-O events, health track | zero or more over a trace | Observed or derived at an observation time | Do not infer state from an absent event |
| `event` | FOI-O traces, service examples | zero or more | Must distinguish event time from observation time | Reject ambiguous timestamps |
| `transition` | FOI-O trace ordering, health track | zero or more | Links predecessor/successor states and triggering evidence | Reject a transition with missing endpoints |
| `actorOrAuthority` | FOI-O source references, health track | zero or more | Authority scope has an effective date | Hold if authority is missing or out of scope |
| `timer` | OIA deadline traces, health track | zero or more | Start, due, applicable period, and calendar semantics | Preserve unknown/not-provided; never calculate from an ambiguous date |
| `humanTask` | FOI-O discretion points, health track | zero or more | Created, assigned, reviewed, and completed times when observed | Remains an explicit human task; no automatic certification |
| `ruleInvocation` | FOI-O rules, Docassemble, harnesses | zero or more | Parameter version and applicable date are required | Reject invocation without rule/parameter identifiers |
| `evidenceReference` | All current consumers | zero or more | Retrieval date and source effective date are distinct | Block controlling use if source is stale, conflicting, or undated |
| `exception` | FOI-O warnings/discretion, health track | zero or more | Exception observation time and review state | Emit explicit exception; do not silently normalize it away |
| `traceLink` | PIC trace projections and FOI-O | zero or more | Links process evidence to a PIC trace digest/version | Reject dangling or unverifiable links |

## Explicit exclusions

The following are rejected from the normative profile because no current
consumer requires them in this repository:

- a global ontology, JSON-LD context, URI registry, or universal vocabulary;
- BPMN elements, Camunda execution semantics, gateways, jobs, or deployment
  configuration;
- embedded expressions, rule languages, or runtime AI decisions;
- inferred clinical, legal, regulatory, funding, or confidential facts;
- patient-level data or real incident records;
- an assertion that a process trace proves legal, clinical, funding, or
  standards-body authority.

The Camunda and other platform tracks may define non-normative projections only
after a named consumer exists and must report representational loss.
