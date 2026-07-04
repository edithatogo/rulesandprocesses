# Assistant output 3 - revised RaCX superset and red-team review

Yes - with your clarification, I would revise my earlier advice. I still think the earlier “perfect translation / zero technical debt” framing in the attached agent discussion was overconfident, but I now think my own response **over-separated rules from process** and **over-weighted the need for a separate IR**.

Your target is sharper:

> Not a replacement for OpenFisca, PolicyEngine, or Axiom; an **exchange and interoperability layer** that lets them keep their strengths while sharing policy semantics, rules, parameters, processes, tests, traces, and evaluation tooling.

That is the right framing.

The attached thread begins from the accurate observation that there is no universal open format for seamlessly moving executable legislative logic between Rules-as-Code systems, while noting that some layers already move better than others: parameters, metadata, APIs, and datasets. It then moves toward a more ambitious dual rules/process architecture. I would keep that ambition, but redesign it as a **profiled exchange superset**, not as “BPMN/DMN and XState/JSON Logic are always equivalent.”

## Conductor context ledger

**Working object:** a Rules-as-Code interoperability and exchange format.

**Purpose:** support OpenFisca, PolicyEngine, Axiom, DMN/BPMN tools, web apps, simulation tools, authoring tools, and evaluation tools without forcing a single engine.

**Core design shift:** use one canonical exchange option, but make it a real policy-exchange package, not raw XState/JSON Logic or raw BPMN/DMN.

**Updated thesis:** rules and process should be closer than I initially framed, because eligibility, evidence, review, notices, discretion, appeals, implementation burden, and fiscal modelling are part of the same policy lifecycle.

**Constraint:** AI may radically reduce migration, authoring, and refactoring costs, but the exchange format still needs stable semantics, conformance tests, deterministic execution, provenance, and governance.

**Open design question:** whether the canonical option should be a new JSON-LD package, an extension profile of Axiom, or a standards-stack packaging convention. My current recommendation is a JSON-LD policy package that can be adopted incrementally by Axiom, PolicyEngine, and OpenFisca.

# 1. Development of the idea so far

| Stage | Idea | What survives | What needs correction |
|---|---|---|---|
| Initial problem | OpenFisca/PolicyEngine models are hard to exchange because executable logic lives in Python. | Correct. Exchange exists for parameters and APIs more than formulas. | Do not frame this as a failure of those projects; it reflects their optimisation for microsimulation. |
| Open standards turn | Use LegalDocML, LegalRuleML, DMN, BPMN, SHACL, JSON-LD, etc. | Correct direction. Existing standards should be reused. | None is sufficient alone. |
| Agentic turn | AI makes verbose, formal, machine-first formats more practical. | Important. Authoring ergonomics matter less if agents assist. | AI does not make semantics, governance, or correctness free. |
| Dual rules/process turn | Rules and process should be linked. | Strong insight. Policy is not just calculation. | Link them, but do not collapse them into one undifferentiated workflow blob. |
| My previous critique | Need a canonical model and constrained profiles. | Still true. | I should not have implied that the canonical model must be a third, neutral artifact separate from the deployable options. |
| Your refinement | Make one option the canonical exchange model. | I agree, with a caveat. | The canonical option should be Option B++, not raw Option B. |

# 2. Revised design: RaCX, a Rules-as-Code Exchange Superset

Working name: **RaCX - Rules-as-Code Exchange Superset**.

RaCX is not a new rules engine. It is not a replacement for OpenFisca or PolicyEngine. It is a **policy package format** and **conformance layer** that engines can import, export, annotate, validate, and test against.

The core package should be JSON-native and JSON-LD-aware, because JSON-LD gives you ordinary JSON ergonomics while allowing global semantic identifiers and linked-data mappings.

The canonical model should therefore be:

> **A JSON-LD policy graph package that contains rules, parameters, entities, processes, evidence requirements, tests, traces, provenance, and mappings to other standards.**

That gives you one canonical option, but avoids making raw XState/JSON Logic carry more semantic weight than they can bear.

## Canonical stack

```text
RaCX package, canonical JSON-LD
  ├── semantic registry
  ├── entities and variables
  ├── parameters and temporal values
  ├── decision/rule graph
  ├── process/case graph
  ├── evidence and data requirements
  ├── tests and traces
  ├── provenance and legal-source anchors
  ├── simulation bindings
  └── engine mappings
        ├── OpenFisca / PolicyEngine / Axiom
        ├── DMN / FEEL
        ├── BPMN / CMMN
        ├── JSON Logic
        ├── XState
        ├── OpenAPI / JSON Schema
        └── LegalDocML / LegalRuleML / SHACL / OWL
```

This is the compromise: **one canonical exchange option**, but that option is a superset package rather than one narrow runtime format.

# 3. Why not make raw XState/JSON Logic the IR?

Because it would smuggle web-app assumptions into the policy layer.

XState is excellent for application and workflow state. JSON Logic is deliberately compact and portable, but it is also deliberately limited. Its usefulness comes from small, deterministic expressions, not from being a full policy ontology or socio-fiscal modelling language.

So I would make the canonical option **web-native**, but not simply:

```text
XState + JSON Logic
```

Instead:

```text
RaCX JSON-LD package
  uses:
    - JSON-compatible expression trees
    - state-machine-compatible process graphs
    - JSON Schema-compatible data contracts
    - JSON-LD semantic identifiers
  exports:
    - XState
    - JSON Logic
    - DMN
    - BPMN
    - OpenFisca/PolicyEngine/Axiom adapters
```

This preserves your “make one option canonical” idea without making the wrong level canonical.

# 4. Rules and process should be closer - but coupled through typed bindings

I agree with your pushback. My earlier separation of “eligibility model” and “service process” was too strong. In real policy, the process is often part of the policy:

- evidence requirements affect eligibility;
- time limits affect entitlement;
- review rights affect implementation;
- discretion affects outcomes;
- notice requirements affect lawful decision-making;
- administrative burden affects whether a policy is practically deliverable;
- process bottlenecks affect policy evaluation.

But the right pattern is **typed coupling**, not fusion.

## The binding pattern

```json
{
  "@id": "racx:state.calculate_entitlement",
  "@type": "racx:AutomatedDecisionStep",
  "requiresEvidence": [
    "racx:evidence.identity_verified",
    "racx:evidence.income_statement"
  ],
  "invokesDecision": "racx:decision.entitlement_amount",
  "produces": [
    "racx:variable.eligible",
    "racx:variable.entitlement_amount",
    "racx:notice.reason_code"
  ],
  "transitions": [
    {
      "when": { "var": "eligible" },
      "to": "racx:state.issue_approval_notice"
    },
    {
      "when": { "not": [{ "var": "eligible" }] },
      "to": "racx:state.issue_refusal_notice"
    }
  ],
  "sourceRefs": [
    "akn:act/2026/12/section/14",
    "akn:act/2026/12/section/18"
  ]
}
```

That object is not “just a rule” or “just a workflow state.” It is a policy implementation node: evidence, decision, result, transition, and legal source are bound together.

This is the key design principle:

> Rules and process should be modelled together as a **policy lifecycle graph**, but each edge should say exactly what kind of relationship it represents.

# 5. The superset over existing ontologies

Your “superset” point is important. I would not create a monolithic ontology that tries to replace all existing standards. I would create a **federated superset**: a small RaCX core vocabulary plus formal mappings to existing standards.

Existing standards already cover important pieces: Akoma Ntoso / LegalDocML, LegalRuleML, SHACL, OWL, SKOS, PROV-O, QUDT, JSON Schema, BPMN, DMN, CMMN, JSON-LD, JSON Logic, XState, and OpenAPI.

## Superset modules

| RaCX module | Purpose | Existing standards it should map to |
|---|---|---|
| Source module | Legal text anchors, amendments, commencement, repeal | Akoma Ntoso, ELI where relevant |
| Norm module | Obligations, permissions, prohibitions, powers, exceptions | LegalRuleML, RuleML |
| Concept module | Policy concepts, definitions, controlled vocabulary | SKOS, OWL, JSON-LD |
| Data module | Entities, variables, input/output schemas | JSON Schema, SHACL, OpenAPI |
| Unit module | Money, dates, periods, units, rounding | QUDT, ISO date/time conventions |
| Rule module | Calculations, eligibility, classifications | DMN, FEEL, JSON Logic, OpenFisca/PolicyEngine formulas |
| Process module | Deterministic workflow, tasks, transitions | BPMN, XState |
| Case module | Discretion, review, caseworker actions | CMMN |
| Evidence module | Evidence requirements, confidence, verification | JSON Schema, SHACL, domain-specific vocabularies |
| Simulation module | Population data, weights, microsimulation bindings | OpenFisca/PolicyEngine conventions, HDF5 metadata |
| Provenance module | Who changed what, why, from which source | PROV-O |
| Test module | Golden cases, boundary cases, trace comparison | New RaCX conformance suite |
| Trace module | Decision traces, process traces, source refs | PROV-O plus RaCX trace schema |

This is the heart of the superset: **not one ontology to rule them all, but a crosswalk layer that makes existing ontologies operationally useful together.**

# 6. How this supports OpenFisca, PolicyEngine, and Axiom

RaCX should support these tools in their natural strengths:

| Engine/tool | Do not force it to become | RaCX should provide |
|---|---|---|
| OpenFisca | A full workflow engine | variable registry, parameter exchange, tests, provenance, formula annotations, optional process hooks |
| PolicyEngine | A BPMN system | reform package metadata, simulation bindings, parameter/rule/test exchange, process-impact metadata |
| Axiom | Merely a wrapper around legacy models | native authoring/exchange layer, schema-first redesign, AI-assisted migration, conformance harness |
| DMN tools | Microsimulation engines | auditable decision tables and decision services |
| BPMN/CMMN tools | Tax-benefit calculators | implementation process, human review, discretion, operational routing |
| Web apps | Legal record systems | citizen-facing state machines, input validation, explanation traces |

The first adoption target should not be “import/export arbitrary Python formulas perfectly.” The first target should be shared concept IDs, shared variable metadata, shared parameter metadata, shared test cases, shared decision traces, shared process bindings, shared source references, and optional expression profiles for declarative rules.

# 7. Updated architecture

```text
                Legal / policy sources
          Akoma Ntoso, manuals, guidance, cases
                         │
                         ▼
              RaCX canonical package
       JSON-LD policy lifecycle graph superset
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
OpenFisca /          PolicyEngine /       Axiom
PolicyEngine         reform analysis      authoring / migration
adapters             and simulation       and exchange UX
      │                  │                  │
      └──────────────────┼──────────────────┘
                         ▼
                  Conformance suite
         golden cases, boundary cases, traces
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
DMN / FEEL           BPMN / CMMN          XState / JSON Logic
decision view        process/case view    web/app view
```

# 8. Red team: my previous advice

1. I overcorrected toward separation.
2. I made “IR” sound too external.
3. I underweighted AI-enabled redesign.
4. I underweighted OpenFisca/PolicyEngine support.
5. I did not emphasise evaluation enough.

# 9. Devil’s advocate: your suggestions

## Challenge 1 - “Superset” could become ontology sprawl

A superset over all existing ontologies can become unbuildable if it tries to capture everything.

**Mitigation:** define a tiny core plus profiles.

## Challenge 2 - Making one option canonical could bias the ecosystem

If the canonical option is too close to XState/JSON Logic, enterprise users may reject it. If it is too close to BPMN/DMN, web and microsimulation users may reject it.

**Mitigation:** canonicalise the policy graph, not any one runtime.

## Challenge 3 - Tighter rules/process coupling can reduce reusability

A payment calculation should not have to know whether an application is submitted through a web form, paper form, call centre, or caseworker portal.

**Mitigation:** bind rules to process through interfaces.

## Challenge 4 - AI-enabled redesign can create new technical debt faster

AI can rapidly generate schemas, adapters, and migrations. It can also rapidly generate inconsistent schemas, brittle translation code, and false confidence.

**Mitigation:** require reference implementations, conformance suites, semantic versioning, and signed test fixtures.

## Challenge 5 - PolicyEngine/OpenFisca adoption depends on low friction

If adopting RaCX requires rewriting every formula, it will fail.

**Mitigation:** start as metadata and test exchange, not full formula exchange.

Adoption ladder:

```text
Level 0: no adoption
Level 1: RaCX concept IDs in variable metadata
Level 2: RaCX parameter metadata and source refs
Level 3: RaCX test cases and expected outputs
Level 4: RaCX decision traces
Level 5: RaCX declarative rules where possible
Level 6: RaCX process bindings
Level 7: full import/export for supported profiles
```

# 10. Core RaCX objects

Core objects include Concept, Variable, Parameter, Decision, and ProcessStep.

# 11. Conformance profiles

Do not define one huge format and ask everyone to support all of it. Define profiles:

- RaCX-Core
- RaCX-Calc
- RaCX-Simulation
- RaCX-Process
- RaCX-Case
- RaCX-Trace

# 12. How to make this adoptable by OpenFisca and PolicyEngine

The first useful contribution should be a sidecar standard, not a full rewrite.

```text
policyengine-us/
  variables/
    income.py
  parameters/
    income_tax.yaml
  racx/
    manifest.jsonld
    concepts.jsonld
    variable_mappings.jsonld
    parameter_mappings.jsonld
    source_refs.jsonld
    tests.racx.json
    traces.racx.schema.json
```

# 13. Redesigning interchange in the Axiom context

Axiom should not merely be a prettier front end over existing Python rules. It could become an authoring environment for RaCX packages, a migration workbench, semantic registry manager, test and trace generator, process/rule binding editor, policy evaluation workbench, and adapter generator.

# 14. Additional improvements

1. Add an evidence model.
2. Add missingness and uncertainty as first-class semantics.
3. Add “normative status” to every process node.
4. Add change-impact diffs.
5. Add reference interpreter and conformance suite.
6. Add a public registry of concept IDs.
7. Add semantic equivalence, not just output equivalence.

# 15. Updated MoSCoW requirements

## Must have

- Canonical RaCX package
- Stable semantic IDs
- Engine mappings
- Temporal parameter model
- Evidence model
- Rule/process bindings
- Test fixture format
- Trace format
- Source provenance
- Conformance profiles
- Deterministic execution

## Should have

- OpenFisca/PolicyEngine sidecar
- Axiom authoring workbench
- DMN/BPMN export
- JSON Logic/XState export
- SHACL/JSON Schema validation
- Administrative burden metrics
- Policy diff engine
- Concept registry

## Could have

- LegalRuleML export
- CMMN export
- Formal verification
- L4/Catala adapters
- Natural-language explanation templates
- Public benchmark suite

## Won’t have initially

- Perfect import of arbitrary Python formulas
- Full BPMN/DMN coverage
- One universal ontology of law
- Runtime AI decisions
- Claim that RaCX is the law

# 16. Revised MVP

**RaCX v0.1: Policy Exchange Sidecar for OpenFisca/PolicyEngine/Axiom**

Scope:

```text
One benefit or tax-credit model
10-20 variables
5-10 parameters
5-10 decisions
one simple process graph
one evidence model
one OpenFisca or PolicyEngine mapping
one Axiom authoring view
one DMN export
one XState/JSON Logic export
one conformance test suite
one trace format
```

Success criteria:

```text
1. Existing PolicyEngine/OpenFisca model can be annotated without rewriting all formulas.
2. Variables and parameters export to RaCX.
3. RaCX test fixtures can run against the native engine.
4. Native engine emits RaCX-compatible traces.
5. A simple process graph binds evidence -> decision -> notice/review/payment.
6. DMN and XState/JSON Logic exports work for the supported subset.
7. The same golden cases produce equivalent outputs and equivalent traces.
8. A policy change generates a readable rule/process/evaluation diff.
```

# 17. Final position

Build a **Rules-as-Code Exchange Superset** that supports OpenFisca, PolicyEngine, and Axiom rather than replacing them. Make the canonical option a JSON-LD policy lifecycle package, not a third hidden IR and not raw XState/JSON Logic. Treat BPMN, DMN, CMMN, XState, JSON Logic, OpenFisca, PolicyEngine, and Axiom as projections, adapters, or authoring/execution environments. Bring rules and process closer through typed bindings: evidence, decision invocation, notices, review, discretion, implementation cost, and evaluation traces. Use AI to migrate, annotate, generate adapters, and create tests - but keep execution and conformance deterministic.
