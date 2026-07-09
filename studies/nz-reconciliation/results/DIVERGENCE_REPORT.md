# NZ RuleSpec vs OpenFisca Aotearoa — Phase 2 divergence report

Generated cases: **17**

## Executive summary

Cross-engine **numeric** reconciliation is not yet possible for the inventory domains.
RuleSpec companion oracles materialise cleanly for non-KiwiSaver slices; OpenFisca
Aotearoa does not currently expose comparable 2026 schedule tax, earners levy, or
KiwiSaver contribution calculations in the checked-out package.

This is an **engine coverage / period / surface gap**, not a silent numeric disagreement.

## Runtime constraints (this environment)

- openfisca-core 41.x install: `blocked_pendulum_build_on_modern_python`
- openfisca-core 44.x + country package: `blocked_metaclass_conflict`
- live simulation: `unavailable`

## Static probe highlights

- Latest income-tax rate parameter instant: `2010-10-01`
- Covers tax year 2026+: `False`
- Defines schedule tax payable formula: `False`
- Earners levy variables present: `False`
- KiwiSaver variable files: `0`

## Per-domain classification

| Domain | RuleSpec | OpenFisca Aotearoa | Classification |
|---|---|---|---|
| `income_tax` | oracle_ok (5) | engine_gap (5) | `engine_gap_missing_schedule_tax_and_stale_parameters` |
| `acc_earners_levy` | oracle_ok (9) | engine_gap (9) | `engine_gap_no_earners_levy_surface` |
| `kiwisaver` | mixed_or_blocked (3) | engine_gap (3) | `engine_gap_no_kiwisaver_surface_plus_rulespec_compile_block` |

## Case rollup

- RuleSpec oracle rows: 17 (ok=14, compile_blocked=3)
- OpenFisca gap rows: 17 (engine_gap=17)
- Comparison agreements (numeric): 0 / 17

Numeric agreements are expected to be **zero** while OpenFisca outputs remain empty gaps.

## Upstream references

- RuleSpec KiwiSaver compile: https://github.com/TheAxiomFoundation/rulespec-nz/issues/79
- OpenFisca Aotearoa: https://github.com/ServiceInnovationLab/openfisca-aotearoa

## Recommended next steps

1. Wait for rulespec-nz#79 resolution, then re-enable KiwiSaver live compile.
2. Either contribute 2024–2026 tax brackets + schedule tax formula to openfisca-aotearoa,
   or document permanent non-overlap and narrow the study to shared surfaces only.
3. For ACC, locate an alternate NZ earners-levy open source implementation or keep
   RuleSpec as sole engine with dual-oracle source triangulation.

## Evidence files

- `results/rulespec-candidate-results.jsonl`
- `results/openfisca-aotearoa-candidate-results.jsonl`
- `results/openfisca-aotearoa-static-probe.json`
- `results/comparison-candidate-results.jsonl`
