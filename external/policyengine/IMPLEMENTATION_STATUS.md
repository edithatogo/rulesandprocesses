# PolicyEngine upstream implementation status

Date: 2026-07-17 (live status recheck)
Agent work against open issues on `PolicyEngine/policyengine-core`.  
Fork: `edithatogo/policyengine-core` (push OK). Org repo push: not available.

The three linked pull requests were rechecked on 2026-07-17 and remain open.
The query returned no listed checks. This packet records pending maintainer
review only; it does not claim merge, adoption, or independent validation.

## PRs opened

| Issue | PR | Branch | What landed |
| --- | --- | --- | --- |
| [#512](https://github.com/PolicyEngine/policyengine-core/issues/512) versioned trace export | **https://github.com/PolicyEngine/policyengine-core/pull/515** | `edithatogo:feature/versioned-trace-export` | `FullTracer.to_trace(format="policyengine.trace.v1")` + `Simulation.to_trace()` over existing FlatTrace data; engine metadata via `get_runtime_metadata()`; optional model metadata; unit tests + towncrier fragment |
| [#513](https://github.com/PolicyEngine/policyengine-core/issues/513) missingness semantics | **https://github.com/PolicyEngine/policyengine-core/pull/516** | `edithatogo:feature/explicit-input-value-state` | `Holder.is_input`, `Simulation.is_input`, `Simulation.get_value_state` (`explicit` \| `default`) using existing `_user_input_keys`; calculation defaults **unchanged**; tests for explicit zero vs missing, cache vs input, situation inputs |
| [#514](https://github.com/PolicyEngine/policyengine-core/issues/514) YAML converter | **https://github.com/PolicyEngine/policyengine-core/pull/517** | `edithatogo:docs/yaml-test-portability` | Docs-only: `docs/usage/yaml_tests.md` documents YAML test shape + portability guidance; converter stays external (`converters/fixtures/`) |

## Design choices

### #512
- Stable format string: `policyengine.trace.v1`
- Document fields: `format`, `engine`, `calculation.roots`, `nodes[]`, `parameters`, optional `model`
- No external schema dependency; pure JSON-compatible dict
- Requires `trace=True` / `FullTracer` for `Simulation.to_trace()`

### #513
- Narrow provenance API only — does **not** propagate unknown through formulas
- Explicit zero remains distinguishable from omitted fields
- `put_in_cache` / formula writes are not user inputs
- Full “partial-input mode / cannot determine” remains future work

### #514
- Full PE↔PIC converter is intentionally out of core (size + intermediate schema ownership)
- Upstream value is documenting the loader contract maintainers already ship

## Local evidence used

- `external/policyengine/TRACE_INVESTIGATION.md`
- `external/policyengine/MISSINGNESS_CASES.md`
- `harness/policyengine_trace/projection.py`
- `converters/fixtures/*`
- Checkout: `.external-repos/policyengine-core` @ upstream `af095b0` base

## Blockers / notes

1. **No write access to `PolicyEngine/policyengine-core`** — PRs opened from the `edithatogo` fork (explicitly requested). Org `AGENTS.md` prefers direct pushes; fork PRs are the available path.
2. CI status depends on PolicyEngine GitHub Actions running against fork PRs (may need maintainer approval for first-time contributors).
3. Maintainers may want a longer discussion on #513 before accepting any behavior that *changes* defaulting; this PR deliberately only adds queries.
4. Local dirty history on checkout `master` still contains an older combined conductor+prototype commit; the three PR branches above are clean rebased implementations from current `upstream/master`.

## Patches

Not required — branches are on the public fork. If PRs are closed without merge, re-export with:

```bash
cd .external-repos/policyengine-core
git format-patch upstream/master...feature/versioned-trace-export -o ../../external/policyengine/patches/
git format-patch upstream/master...feature/explicit-input-value-state -o ../../external/policyengine/patches/
git format-patch upstream/master...docs/yaml-test-portability -o ../../external/policyengine/patches/
```
