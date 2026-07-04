# MoSCoW requirements for RaCX v0.1

## Must have

| Requirement | Description |
|---|---|
| Canonical package | JSON-LD-compatible policy lifecycle package with a manifest and stable IDs. |
| RaCX-Core profile | Small mandatory core: concepts, variables, parameters, source refs, tests, traces, mappings. |
| Stable semantic IDs | Concepts, variables, parameters, decisions, process nodes. |
| Temporal parameters | Effective dates, values, source refs, repeal/supersession. |
| Test fixtures | Golden and boundary tests that can run against native engines. |
| Trace format | Decision traces with rule IDs, parameter versions, source refs, engine version, and outputs. |
| OpenFisca/PolicyEngine sidecar mappings | Non-invasive adoption path. |
| Evidence model | Required evidence, verification state, confidence, expiry. |
| Typed rule/process bindings | Process steps invoke decisions through explicit interfaces. |
| Deterministic validation | Schema/profile validation without runtime AI. |

## Should have

| Requirement | Description |
|---|---|
| Axiom authoring view | AI-assisted editing, migration, mapping, and conformance workflow. |
| DMN/JSON Logic exports | For supported declarative rule subsets. |
| BPMN/XState exports | For supported process subsets. |
| Simulation metadata | Population entities, weights, reform scenarios, metrics. |
| Policy diff engine | Rule, parameter, process, trace, fiscal, and admin-burden diffs. |
| Public concept registry | Jurisdiction-specific concept IDs and mappings. |
| Semantic equivalence tests | Compare traces and source refs, not just outputs. |

## Could have

| Requirement | Description |
|---|---|
| CMMN export | For case management and discretionary processes. |
| LegalRuleML export | For legal-norm interchange. |
| SHACL validation | For graph constraints and data validation. |
| Formal verification | For high-risk profiled subsets. |
| L4/Catala adapters | Where those DSLs are used. |
| Explanation templates | Citizen and caseworker explanations generated from traces and approved text. |

## Won't have initially

| Exclusion | Rationale |
|---|---|
| Perfect arbitrary Python import/export | Too hard and not needed for first adoption. |
| Full BPMN/DMN coverage | Too expressive for safe exchange. |
| Runtime AI legal decisions | Unnecessary and unsafe. |
| One global ontology of law | Jurisdictional specificity matters. |
| Claim that RaCX is legally authoritative | The law remains the law unless a jurisdiction provides otherwise. |
