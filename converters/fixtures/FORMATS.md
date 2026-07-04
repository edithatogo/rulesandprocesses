# Fixture Format Comparison

Verified 2026-07-04 from current upstream code checkouts:

| Ecosystem | Repository | Commit | Loader source |
|---|---|---:|---|
| OpenFisca | `openfisca/openfisca-core` | `4f7f09833afe7e8b6856e8d7a3016c04a931009b` | [`openfisca_core/tools/test_runner.py`](https://github.com/openfisca/openfisca-core/blob/4f7f09833afe7e8b6856e8d7a3016c04a931009b/openfisca_core/tools/test_runner.py) |
| OpenFisca country corpus | `openfisca/openfisca-france` | `6eeee2e09b9f807ab3735ef494a92001a975f4ad` | [`tests/`](https://github.com/openfisca/openfisca-france/tree/6eeee2e09b9f807ab3735ef494a92001a975f4ad/tests) |
| PolicyEngine | `PolicyEngine/policyengine-core` | `f761573c2a13adecc3826be04af1980d13657e1d` | [`policyengine_core/tools/test_runner.py`](https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/tools/test_runner.py) |
| PolicyEngine country corpus | `PolicyEngine/policyengine-us` | `fc64cef64ab55c3c48309c7fb304c35e5f3c9184` | [`policyengine_us/tests/`](https://github.com/PolicyEngine/policyengine-us/tree/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/tests) |
| PIC | this repository | local | [`contracts/pic-fixtures/0.1.0/schema.json`](../../contracts/pic-fixtures/0.1.0/schema.json) |

`openfisca-aotearoa` was attempted first because the plan prefers it for the NZ tie-in. The repository was not available at `https://github.com/openfisca/openfisca-aotearoa.git`, so this track uses `openfisca-france` as the plan's fallback country package.

## Loader Facts From Code

OpenFisca accepts YAML files as either one mapping or a list of mappings, then builds a typed `Test` dataclass. Its accepted top-level fields are `absolute_error_margin`, `description`, `extensions`, `ignore_variables`, `input`, `keywords`, `max_spiral_loops`, `name`, `only_variables`, `output`, `period`, `parameters`, `reforms`, and `relative_error_margin`. Error margins may be scalar values or per-variable mappings. `output` is mandatory at runtime. OpenFisca applies `parameters` through `InYamlTestReform` before building the simulation and applies `max_spiral_loops` to the simulation. Output may be a direct variable, an entity singular, or an entity plural keyed by instance id.

PolicyEngine accepts YAML files as one mapping or a list of mappings. Its accepted top-level fields are `absolute_error_margin`, `description`, `extensions`, `ignore_variables`, `input`, `keywords`, `name`, `only_variables`, `output`, `period`, `reforms`, and `relative_error_margin`. It rejects non-mapping YAML test entries and unexpected keys. `output` is mandatory at runtime. PolicyEngine also treats dotted input keys as inline parameter reforms, building a reform with `set_parameter`; this differs from OpenFisca's explicit `parameters` field. Output may be a direct variable, an entity singular, or an entity plural keyed by instance id.

PIC fixtures require `conformsTo`, file-level `provenance`, and `cases`. Each case requires `caseId`, `description`, `period`, `entities`, `inputs`, `expected`, and `sourceRefs`. Inputs and expected outputs are keyed by PIC IDs. Values use PIC `valueState` and optional `epistemicStatus`; expected values may also carry `tolerance`. Provenance supports `method: mechanical`, which is the correct method for deterministic format conversion.

## Field Comparison

| Construct | OpenFisca YAML | PolicyEngine YAML | PIC fixture |
|---|---|---|---|
| Document shape | Mapping or list of mappings | Mapping or list of mappings; each list item must be a mapping | One object with `cases` array |
| Test id/name | Optional `name` | Optional `name` | Required `caseId`; `description` required |
| Description | Optional `description` | Optional `description` | Required `description`; file/case provenance carries source |
| Period | Optional `period`, passed as default simulation period | Optional `period`, passed as default simulation period | Required string `period` |
| Inputs | `input` mapping; may be scalar variables or entity structures | `input` mapping; dotted keys are inline parameter reforms | `inputs` map keyed by PIC/native IDs, each a `valueObject` |
| Outputs | `output` mapping; required at runtime; nested dicts mean periods or entity outputs depending on key context | Same runtime output traversal as OpenFisca | `expected` map keyed by PIC/native IDs |
| Entity plural outputs | Output key may resolve to plural population, then instance id, then variable | Same | Represented in case `entities`, with flattened expected IDs in v0.1 converter subset |
| Entity inputs | Passed through `SimulationBuilder.build_from_dict` | Passed through `SimulationBuilder.build_from_dict` | Captured in `entities` plus flattened `inputs` |
| Absolute tolerance | `absolute_error_margin`, scalar or per-variable mapping | `absolute_error_margin`, scalar only in runner usage | `expected[*].tolerance` decimal string |
| Relative tolerance | `relative_error_margin`, scalar or per-variable mapping | `relative_error_margin`, scalar only in runner usage | Rejected in v0.1; PIC tolerance is absolute |
| Reforms | `reforms` sequence | `reforms` string or sequence | Rejected in v0.1 |
| Extensions | `extensions` sequence | `extensions` string or sequence | Rejected in v0.1 |
| Inline parameters | `parameters` mapping | Dotted `input` keys are rewritten with `set_parameter` | Rejected in v0.1 converter subset |
| Keywords/filtering | `keywords`, `ignore_variables`, `only_variables` | `keywords`, `ignore_variables`, `only_variables` | Rejected in v0.1; test-runner filtering metadata is not fixture semantics |
| Spiral controls | `max_spiral_loops` | Not accepted | Rejected in v0.1 |
| Value types | Native YAML scalar values and nested dicts | Native YAML scalar values and nested dicts | Boolean, integer, string, decimal strings via PIC semantics |
| Enums | Native YAML strings | Native YAML strings | String values; crosswalk can give PIC meaning |
| Source provenance | File path and repo commit external to YAML | File path and repo commit external to YAML | Required file-level provenance and `sourceRefs` |

## Divergences To Preserve

- OpenFisca's current loader supports `parameters` and `max_spiral_loops`; PolicyEngine's loader does not.
- PolicyEngine treats dotted input keys as inline parameter reforms; OpenFisca separates parameter overrides into `parameters`.
- OpenFisca wraps error margins in an `ErrorMargin` helper that supports per-variable mappings; PolicyEngine forwards the top-level margin values directly to `assert_near`.
- PolicyEngine rejects unexpected top-level fields explicitly. OpenFisca's dataclass construction also rejects unknown fields, but through dataclass construction rather than an explicit pre-check.
- Both loaders share the same broad output traversal shape, but converting entity structures without a model-specific entity schema is lossy. The v0.1 converter therefore supports simple scalar tests and explicit nested entity cases only when the shape can be flattened and reconstructed mechanically.
