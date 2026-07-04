# pic-traces 0.1.0

`pic-traces` records scalar, case-level decision traces. A trace states inputs, outputs, engine metadata, ordered steps, parameter versions, and source references.

## Vectorized Engines

Batch derivation for vectorized engines is deferred. Acceptable future approaches may include per-case re-execution, sampling, or computation-tree projection. Track 4 investigates PolicyEngine computation-tree feasibility. Version 0.1.0 only claims scalar/case-level traces.

## File Shape

```json
{
  "conformsTo": "pic-traces/0.1.0",
  "caseId": "nz-oia/fixture.simple",
  "packageRef": {"id": "nz-oia-clocks", "version": "0.1.0"},
  "engine": {"name": "example", "version": "0.1.0"},
  "timestamp": "2026-07-05T00:00:00Z",
  "inputs": {},
  "outputs": {},
  "steps": []
}
```

## Step Shape

Steps are constrained to `decision`, `process`, `evidence_check`, or `notice`. Each step records the PIC IDs it used, parameter versions it depended on, a value-state-aware result, and source references.

## Equivalence Levels

- Output-equivalent: outputs are the same.
- Path-equivalent: output-equivalent and the same ordered `stepId` plus `parameterVersions`.
- Semantically equivalent: path-equivalent and each step has the same `sourceRefs`.

Conformance reports must state the strongest equivalence level they claim.

