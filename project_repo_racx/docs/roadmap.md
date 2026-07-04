# 90-day roadmap

## Days 1-15: Core schema and example

- Finalise RaCX-Core object list.
- Create manifest, concept, variable, parameter, test, trace, and mapping schemas.
- Build the basic income support example.

## Days 16-30: Sidecar for existing engine

- Implement a PolicyEngine or OpenFisca sidecar exporter for concepts, variables, parameters, and source refs.
- Define a native-engine test runner that consumes RaCX fixtures.

## Days 31-45: Trace contract

- Implement trace output format.
- Build semantic equivalence comparison for inputs, outputs, parameter versions, source refs, and rule paths.

## Days 46-60: Evidence/process binding

- Define minimal evidence and process-step schema.
- Bind example evidence -> decision -> notice/review/payment flow.

## Days 61-75: Declarative export subset

- Implement JSON Logic and DMN exports for a small expression profile.
- Add golden and boundary tests.

## Days 76-90: Axiom workbench prototype

- Prototype AI-assisted mapping and review workflow.
- Generate change-impact diffs.
- Prepare adoption proposal for PolicyEngine/OpenFisca maintainers.
