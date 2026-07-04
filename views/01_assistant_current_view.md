# Assistant current view

## Short version

The strongest design is not a replacement rules engine and not a universal legal DSL. It is a **policy exchange package and conformance layer** that lets OpenFisca, PolicyEngine, Axiom, DMN/BPMN tools, web apps, and evaluation tools share semantics, tests, traces, and process bindings.

## Recommended architecture

Use a canonical **RaCX JSON-LD policy lifecycle package** with profiles. This package is the exchange contract. It can export to, import from, or annotate existing systems.

The core should include:

- stable concept IDs;
- variable metadata;
- temporal parameters;
- evidence requirements;
- decisions and expressions where declarative enough;
- process/case nodes;
- typed rule/process bindings;
- source references;
- tests;
- traces;
- engine mappings.

## Why JSON-LD

JSON-LD keeps developer ergonomics close to ordinary JSON while allowing global semantic identifiers and mappings to RDF/linked data. It is a reasonable canonical exchange serialization, but it must not become raw XState/JSON Logic. It should be a policy graph, not a web-app state machine.

## Why not raw BPMN/DMN

BPMN/DMN are valuable projections and may be authoritative in some enterprise contexts, but they are too expressive, XML-heavy, and enterprise-workflow-biased to be the whole exchange layer. They also do not naturally cover microsimulation datasets, population weights, OpenFisca/PolicyEngine variable semantics, test fixtures, or policy-evaluation metadata.

## Why not raw XState/JSON Logic

XState/JSON Logic are valuable web/app projections. They are not enough to carry legal source provenance, ontology mappings, temporal parameter semantics, fiscal simulation bindings, case management, evidence confidence, normative status, or cross-engine conformance.

## Why rules/process coupling matters

Eligibility and process cannot be fully separated in real policy systems. Evidence requirements, time limits, manual review, notices, discretion, appeals, and operational burden shape actual outcomes. However, coupling should be typed and explicit:

```text
process step -> requires evidence -> invokes decision -> produces outputs -> issues notice / routes case -> emits trace
```

Calculations should remain reusable decision services; process nodes should bind to them through interfaces.

## Adoption philosophy

Start low-friction:

1. stable concept IDs;
2. variable and parameter sidecars;
3. source references;
4. shared test fixtures;
5. decision traces;
6. declarative expression exchange for supported subsets;
7. process/evidence bindings;
8. full import/export only for profiled subsets.

## Biggest warning

Do not claim perfect translation, zero technical debt, or legal correctness. The value is not perfect syntax conversion. The value is semantic governance, tests, traces, versioning, comparability, and interoperability.
