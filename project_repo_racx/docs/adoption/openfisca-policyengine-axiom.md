# Adoption path for OpenFisca, PolicyEngine, and Axiom

## Adoption principle

Do not require a rewrite. Start with sidecars and conformance fixtures.

## Level 1 - Stable IDs

Add RaCX concept IDs to variables and parameters.

Value: cross-engine comparison and migration.

## Level 2 - Parameter metadata

Export parameters to RaCX temporal parameter format with source refs.

Value: easier comparison of baselines and reforms.

## Level 3 - Test fixtures

Export golden cases and expected outputs in RaCX test format.

Value: shared conformance and regression testing.

## Level 4 - Traces

Emit RaCX-compatible traces from native calculations.

Value: audit, explanation, semantic equivalence testing.

## Level 5 - Source references

Annotate variables, parameters, and formula blocks with legal/policy source refs.

Value: provenance and review.

## Level 6 - Declarative expression export

Export supported formula subsets to RaCX expressions, DMN, or JSON Logic.

Value: partial executable interchange without arbitrary Python translation.

## Level 7 - Process bindings

Bind decisions to evidence and process nodes.

Value: implementation planning and administrative-burden evaluation.

## Axiom-specific opportunity

Axiom could become the authoring and migration workbench for RaCX:

- AI-assisted extraction and mapping;
- schema-first redesign;
- sidecar generation for existing models;
- process/rule binding editor;
- conformance test generation;
- diff and impact analysis;
- adapter generation.
