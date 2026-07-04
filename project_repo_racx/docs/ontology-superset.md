# Ontology and standards strategy

## Position

RaCX should not replace existing ontologies and standards. It should be a federated superset/crosswalk layer over them.

## Core vocabulary

RaCX core should define only the policy lifecycle concepts that are needed to bind existing standards together:

- `PolicyPackage`
- `Concept`
- `Variable`
- `TemporalParameter`
- `Decision`
- `EvidenceRequirement`
- `ProcessStep`
- `CaseAction`
- `TestFixture`
- `Trace`
- `EngineMapping`
- `SourceRef`

## Mappings

| RaCX area | Standards to map to |
|---|---|
| Legal source | Akoma Ntoso / LegalDocML, ELI where relevant |
| Normative rules | LegalRuleML, RuleML |
| Concepts | SKOS, OWL, JSON-LD |
| Data validation | JSON Schema, SHACL, OpenAPI |
| Units | QUDT, ISO date/time conventions |
| Decisions | DMN, FEEL, JSON Logic, OpenFisca/PolicyEngine/Axiom |
| Process | BPMN, XState |
| Case management | CMMN |
| Provenance | PROV-O |
| Simulation | OpenFisca/PolicyEngine conventions, HDF5 metadata |

## Governance questions

- Who can mint public concept IDs?
- How are jurisdictional concepts scoped?
- How are equivalent but not identical concepts represented?
- How are amendments and semantic drift handled?
- How are deprecated concepts preserved for old decisions?
