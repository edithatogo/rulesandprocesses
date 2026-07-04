# Design decisions log

## DD-001: Support, do not replace, OpenFisca/PolicyEngine/Axiom

Decision: RaCX is an exchange and conformance layer, not a replacement engine.

Rationale: OpenFisca and PolicyEngine are optimized for microsimulation and tax-benefit computation. The proposal should lower interoperability costs, not require migration away from established systems.

## DD-002: Use a canonical JSON-LD package

Decision: Use a JSON-native, JSON-LD-aware policy lifecycle package as the canonical exchange representation.

Rationale: JSON is accessible to modern tooling and agents. JSON-LD allows stable semantic IDs and crosswalks to RDF/ontologies. Raw XState/JSON Logic and raw BPMN/DMN are too narrow as canonical models.

## DD-003: Profiles over universal coverage

Decision: Define profiles such as RaCX-Core, RaCX-Calc, RaCX-Simulation, RaCX-Process, RaCX-Case, and RaCX-Trace.

Rationale: No single engine should be expected to support the whole superset.

## DD-004: Typed coupling between rules and process

Decision: Couple rules and process through explicit object types and interfaces, not by merging everything into one workflow.

Rationale: Process context matters, but decision services must remain reusable.

## DD-005: Sidecar-first adoption

Decision: Begin with sidecar metadata, tests, traces, and mappings.

Rationale: Lowest adoption friction for OpenFisca/PolicyEngine. Full formula translation can be added only for declarative subsets.

## DD-006: No runtime AI for decisions

Decision: AI can draft, migrate, annotate, generate tests, and assist review. It must not execute eligibility/payment/tax decisions at runtime.

Rationale: Determinism, auditability, legal safety, reproducibility.

## DD-007: Semantic equivalence over syntax equivalence

Decision: Conformance should compare outputs, traces, source refs, parameters, and rule paths, not just generated code syntax.

Rationale: Two engines can produce the same value for different reasons; policy assurance needs deeper comparison.
