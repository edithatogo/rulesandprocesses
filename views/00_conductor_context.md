# Conductor context ledger

## Mission

Create a second-opinion review pack for a proposed Rules-as-Code exchange/interoperability architecture. The project is currently called **RaCX - Rules-as-Code Exchange Superset**.

## User intent

Dylan wants to support OpenFisca, PolicyEngine, and Axiom by defining exchange formats they could adopt. The project is explicitly not intended to replace those systems. It should abstract tooling from underlying rules/processes and permit interoperability across execution, authoring, simulation, workflow, and evaluation environments.

## Current thesis

Rules and process should be brought closer together than typical RaC systems do. In policy implementation, eligibility logic, evidence requirements, administrative process, human review, notices, appeals, fiscal modelling, and administrative-burden evaluation are linked parts of the same lifecycle.

## Current proposed architecture

A canonical JSON-LD policy lifecycle package with typed objects for:

- concepts;
- variables;
- parameters;
- decisions/rules;
- evidence requirements;
- process/case steps;
- tests;
- traces;
- source provenance;
- engine mappings;
- simulation and evaluation metadata.

This is a "superset" in the sense of a federated crosswalk over existing standards, not a monolithic replacement ontology.

## Key constraints

- No runtime LLM decisions for eligibility, payment, refusal, tax, or administrative rights.
- AI is used for migration, drafting, annotation, testing, adapter generation, and review.
- Deterministic validators, reference interpreters, conformance suites, and audit traces are required.
- Adoption should start as sidecar metadata/tests/traces, not a forced rewrite of OpenFisca/PolicyEngine formulas.

## Key unresolved questions

1. Should the canonical package be JSON-LD, Axiom-native, or a standards-stack packaging convention?
2. What is the smallest useful RaCX-Core?
3. How much formula exchange should v0.1 attempt?
4. How should rules/process coupling be typed to avoid overcoupling?
5. What is the adoption path for PolicyEngine/Axiom that creates value quickly?
6. How should a public registry of concepts be governed?
7. How should semantic equivalence and trace equivalence be tested?

## Next requested model task

Claude Fable 5 should read the package, red-team it, and propose whether it would approach the exchange/interchange design differently.
