# New Zealand Rules-as-Code Coverage Gaps: RuleSpec and OpenFisca Aotearoa

**Author:** Dylan A Mordaunt  
**ORCID:** [0000-0002-9775-0603](https://orcid.org/0000-0002-9775-0603)  
**Status:** draft; submission deferred pending human authorization  
**Evidence track:** `nz_reconciliation_20260707`, `nz_recon_live_20260709`

## Abstract

Comparative rules-as-code studies can fail before numerical comparison when the selected engines do not expose the same policy surfaces. We examine a 17-case inventory spanning New Zealand individual schedule income tax, ACC earners' levy, and KiwiSaver contributions in a RuleSpec implementation and OpenFisca Aotearoa. RuleSpec produced 14/17 companion-oracle rows and blocked three KiwiSaver rows at compilation. OpenFisca Aotearoa produced 17/17 documented engine-gap rows because the checked package did not expose comparable 2026 schedule-tax, earners-levy, or KiwiSaver surfaces. Consequently, the study records zero numeric agreements as an expected coverage result, not as evidence of formula disagreement. The contribution is methodological: report coverage and model-surface compatibility before interpreting differential outputs.

## 1. Introduction

Differential testing assumes that two implementations expose comparable decisions, parameters, periods, and outputs. In public-policy software that assumption is often false: packages may model different years, variables, or administrative pathways. A zero-agreement result is therefore uninterpretable unless coverage gaps are measured separately.

## 2. Materials and methods

The inventory contains 17 cases: five income-tax cases, nine ACC earners' levy cases, and three KiwiSaver cases. The RuleSpec side uses companion fixtures and the pinned Axiom validation harness. The OpenFisca Aotearoa side uses the checked package's static surface probe and candidate test corpus. Results are classified as `ok`, `compile_blocked`, or `engine_gap` before any numeric comparison is attempted.

The source and effective-date boundary is maintained in [`papers/CITATION_LEDGER.md`](../../../papers/CITATION_LEDGER.md). Reproduction artifacts are listed in [`results/DIVERGENCE_REPORT.md`](../results/DIVERGENCE_REPORT.md) and the runner tests. The study does not invent missing OpenFisca formulas and does not treat RuleSpec output as a legal oracle.

## 3. Results

RuleSpec produced 14 `ok` rows and three KiwiSaver `compile_blocked` rows. OpenFisca Aotearoa produced 17 `engine_gap` rows. The resulting numeric agreement count was 0/17, because there were no paired numeric outputs. The gaps were: stale or absent current income-tax schedule surfaces, no comparable ACC earners' levy variables, and no comparable KiwiSaver variables. The KiwiSaver RuleSpec compile blocker is tracked in [rulespec-nz#79](https://github.com/TheAxiomFoundation/rulespec-nz/issues/79).

## 4. Discussion

The study demonstrates a precondition gate for cross-engine research: establish policy-vintage and surface overlap before computing agreement rates. Coverage gaps are findings about package scope and maintenance, not evidence that either engine's formulas are wrong. The result also provides a constructive upstream request, [openfisca-aotearoa#199](https://github.com/BetterRules/openfisca-aotearoa/issues/199), and a potential follow-up if maintainers add the missing surfaces.

## Data and code availability

Fixtures, static probes, candidate results, live results, compiled RuleSpec artifacts, runner tests, and the certified human review are committed under `studies/nz-reconciliation/`. Repository validation is run by `make check`; live engine reruns require the recorded third-party revisions and compatible runtimes.

## Limitations

This is a purposive 17-case inventory, not a population sample. It does not measure legal correctness, engine quality, or numerical agreement for surfaces that are not jointly implemented. Runtime dependency incompatibility limited live OpenFisca execution in the recorded environment. Rates and statutory interpretations are time-varying and require refresh before publication. The certified result is a coverage-gap finding, not a dual-engine parity result.

## 5. Conclusion

Cross-engine comparison should fail closed when the engines do not share a policy surface. Separating `engine_gap` and `compile_blocked` from numeric divergence prevented an invalid claim of disagreement and produced actionable upstream work.
