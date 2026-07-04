# RaCX-Core v0.1 draft

## Status

Exploratory draft. Not a standard.

## Required objects

A valid RaCX-Core package must include:

1. `Manifest`
2. `Concept`
3. `Variable`
4. `Parameter`
5. `SourceRef`
6. `TestFixture`
7. `TraceContract`
8. `EngineMapping`

## Optional objects

- `Decision`
- `Expression`
- `EvidenceRequirement`
- `ProcessStep`
- `NoticeTemplate`
- `SimulationScenario`
- `CaseAction`

## Required manifest fields

- `@context`
- `@id`
- `@type = racx:PolicyPackage`
- `racxVersion`
- `packageVersion`
- `jurisdiction`
- `profiles`
- `files`

## Identity rules

- All policy objects should have stable `@id` values.
- IDs should be jurisdictional and package-scoped unless registered globally.
- Amendments should not silently mutate meaning; use versioned parameters and source references.

## Period and temporal rules

- All variables and parameters with time dependence must specify period semantics.
- Temporal parameters must include effective date ranges.
- Date comparisons must define timezone/jurisdictional calendar conventions.

## Numeric rules

- Money must be represented as decimal strings or fixed-precision decimals, not binary floats.
- Rounding mode and scale must be declared where relevant.

## Missingness rules

RaCX must distinguish:

- value is zero;
- value is false;
- value is unknown;
- value was not provided;
- value is not applicable;
- value is provided but unverified;
- value is verified but stale;
- evidence is conflicting.

## Trace rules

A conforming engine should be able to emit a trace with:

- package ID and version;
- engine and adapter version;
- input values;
- output values;
- decision path;
- parameter versions;
- source references;
- process path where applicable.
