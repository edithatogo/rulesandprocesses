# PolicyEngine Trace Investigation

Track: `engine_contributions_20260704` phase 1 C-A

Date: 2026-07-04

## Environment

Installed in local editable mode with:

```bash
uv venv .venv-policyengine
. .venv-policyengine/bin/activate
uv pip install -e .external-repos/policyengine-core -e .external-repos/policyengine-us
```

Verified installed versions:

- `policyengine-core==3.28.0`
- `policyengine-us==1.755.5`
- `numpy==2.5.1`
- `pandas==3.0.3`

Local upstream revisions:

- `policyengine-core`: `f761573c2a13adecc3826be04af1980d13657e1d`
- `policyengine-us`: `fc64cef64ab55c3c48309c7fb304c35e5f3c9184`

## Household Trace Run

The traced household case is adapted from PolicyEngine-US' own SNAP baseline tests, specifically the "Case 5, work-requirement-ineligible adult is excluded from SNAP benefit size" case in `policyengine_us/tests/policy/baseline/gov/usda/snap/snap.yaml`.

Command run:

```bash
. .venv-policyengine/bin/activate
python - <<'PY'
import json
from policyengine_us import Simulation

situation = {
    "people": {
        "person1": {
            "age": {"2024": 35},
            "monthly_age": 35,
            "is_tax_unit_dependent": False,
            "meets_snap_general_work_requirements": True,
            "meets_snap_abawd_work_requirements": True,
        },
        "person2": {
            "age": {"2024": 30},
            "monthly_age": 30,
            "is_tax_unit_dependent": False,
            "meets_snap_general_work_requirements": False,
            "meets_snap_abawd_work_requirements": False,
        },
    },
    "spm_units": {"spm_unit": {"members": ["person1", "person2"]}},
    "tax_units": {"tax_unit": {"members": ["person1", "person2"]}},
    "households": {
        "household": {"members": ["person1", "person2"], "state_code": "TX"}
    },
}

sim = Simulation(
    situation=situation,
    trace=True,
    default_input_period="2024",
    default_calculation_period="2024",
)
value = sim.calculate("snap", "2024-01")
flat = sim.tracer.get_serialized_flat_trace()
print("snap", value.tolist() if hasattr(value, "tolist") else value)
print("tree_count", len(sim.tracer.trees))
print("flat_node_count", len(flat))
print("first_keys", list(flat)[:8])
root = list(flat)[0]
print("root", root, json.dumps(flat[root], default=str)[:1000])
PY
```

Observed output:

```text
snap [291.0]
tree_count 1
flat_node_count 2833
first_keys ['snap<2024-01, (default)>', 'takes_up_snap_if_eligible<2024-01, (default)>', 'snap_normal_allotment<2024-01, (default)>', 'is_snap_eligible<2024-01, (default)>', 'meets_snap_net_income_test<2024-01, (default)>', 'snap_net_income_fpg_ratio<2024-01, (default)>', 'snap_net_income<2024-01, (default)>', 'snap_gross_income<2024-01, (default)>']
root snap<2024-01, (default)> {"dependencies": ["takes_up_snap_if_eligible<2024-01, (default)>", "snap_normal_allotment<2024-01, (default)>", "snap_emergency_allotment<2024-01, (default)>", "dc_snap_temporary_local_benefit<2024-01, (default)>"], "parameters": {}, "value": [291.0], "calculation_time": 2.615, "formula_time": 0.0001338}
```

## Tracer Source Findings

Primary source links are pinned to the local upstream commit above.

- `Simulation.__init__` installs `FullTracer` when `trace=True`, otherwise `SimpleTracer`: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/simulations/simulation.py#L115-L158>
- The `trace` property setter also swaps between `FullTracer` and `SimpleTracer`: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/simulations/simulation.py#L520-L530>
- `Simulation.calculate()` wraps every calculation with `record_calculation_start`, `record_calculation_result`, and `record_calculation_end`: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/simulations/simulation.py#L558-L612>
- `TraceNode` contains `name`, `period`, `branch_name`, `parent`, `children`, `parameters`, `value`, `start`, and `end`, plus derived `calculation_time()` and `formula_time()`: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/tracers/trace_node.py#L16-L50>
- `FullTracer` builds a rooted tree by appending each child calculation under the current node and also records parameter accesses on the current node: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/tracers/full_tracer.py#L27-L73>
- `FullTracer` exposes `trees`, `browse_trace()`, `get_flat_trace()`, and `get_serialized_flat_trace()`: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/tracers/full_tracer.py#L112-L173>
- `FlatTrace` serializes each node into a stable key of the form `variable<period, (branch)>`, with `dependencies`, `parameters`, `value`, `calculation_time`, and `formula_time`: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/tracers/flat_trace.py#L24-L89>
- Parameter reads are traced by wrapping `ParameterNodeAtInstant`; scalar or array leaf reads call `record_parameter_access`: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/tracers/tracing_parameter_node_at_instant.py#L24-L80>
- Parameter tracing is activated when a `ParameterNode` is at an instant and has tracing enabled: <https://github.com/PolicyEngine/policyengine-core/blob/f761573c2a13adecc3826be04af1980d13657e1d/policyengine_core/parameters/parameter_node.py#L216-L227>

## Node Contents

The current serialized flat trace is already close to a PIC trace source:

```json
{
  "snap<2024-01, (default)>": {
    "dependencies": [
      "takes_up_snap_if_eligible<2024-01, (default)>",
      "snap_normal_allotment<2024-01, (default)>",
      "snap_emergency_allotment<2024-01, (default)>",
      "dc_snap_temporary_local_benefit<2024-01, (default)>"
    ],
    "parameters": {},
    "value": [291.0],
    "calculation_time": 2.615,
    "formula_time": 0.0001338
  }
}
```

Projection notes:

- A PolicyEngine flat-trace key can be parsed into PIC step `id`, `period`, and an engine branch qualifier.
- `dependencies` gives direct input step references. Topological order can be recovered by post-order traversal from the requested output or by sorting each node after its dependencies.
- `parameters` can populate PIC `parameterVersions` or step annotations. Current keys include the accessed parameter name and instant but not the source file commit, so a versioned upstream export should include an explicit model version and parameter revision.
- `value` should be serialized into deterministic JSON-compatible values. Money-like outputs should be decimal strings in PIC-facing documents rather than binary floats.
- `calculation_time` and `formula_time` are useful diagnostics but should be optional metadata, not part of the normative result.

## Feasibility Assessment

Household-level trace export is direct. The current public API already returns enough structure for a versioned `to_trace()` helper to produce a deterministic trace document for one requested calculation.

Microsimulation vectorized derivation is not proven by this run. The installed `policyengine-us` README says direct `policyengine-us` `Microsimulation()` is deprecated in favour of the managed `policyengine.py` bundle, and its docs show default and CPS datasets loaded from Hugging Face (`enhanced_cps_2024.h5`, `cps_2023.h5`). The local checkout does not include a 1k-household CPS sample, and this investigation did not download external microdata or run the managed `policyengine.py` bundle.

Honest block for microsim measurement:

- Blocker: no local 1k-household CPS/enhanced-CPS dataset is present in the repo or existing engine clone.
- Relevant source: PolicyEngine-US README deprecates direct `policyengine-us` microsimulation and points to the managed bundle: <https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/README.md#L7>
- Relevant source: PolicyEngine-US docs identify the remote dataset URIs: <https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/docs/usage/microsimulation.md#L96-L106>
- Proposed follow-up measurement, once Dylan approves remote dataset access: install the managed bundle, load a pinned dataset revision, sample exactly 1,000 households with fixed seed, and compare (a) one vectorized traced `snap` run against (b) per-household re-execution with `trace=True`, reporting wall time, peak memory, node counts, and whether dependency order differs materially.

## Upstream Recommendation

Propose a versioned trace export on `FullTracer` or `Simulation`, for example:

```python
sim = Simulation(situation=situation, trace=True)
sim.calculate("snap", "2024-01")
trace = sim.tracer.to_trace(format="policyengine.trace.v1")
```

Minimum useful fields:

- `format`: version string, such as `policyengine.trace.v1`
- `engine`: package name, package version, model package version, and optional git revision
- `calculation`: requested variable, period, branch, entity/count metadata
- `nodes`: dependency-ordered nodes with `id`, `variable`, `period`, `branch`, `dependencies`, `parameters`, `value`, and optional timings
- `parameters`: accessed parameter names, instants, scalar/vector value summaries, and source/version metadata when available

The PIC projection should remain a downstream proof point, not a requirement for PolicyEngine users.
