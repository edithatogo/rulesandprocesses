# Axiom upstream feedback draft

Track: `axiom_validation_20260706`
Status: **submitted** — https://github.com/TheAxiomFoundation/rulespec-nz/issues/79 (2026-07-09)

## Live issue

- URL: https://github.com/TheAxiomFoundation/rulespec-nz/issues/79
- Title: KiwiSaver contributions module fails to compile with the pinned Axiom RuleSpec engine

## Draft issue: KiwiSaver contributions module fails to compile

- Target repo: `TheAxiomFoundation/rulespec-nz`
- Affected module: `nz/statutes/kiwisaver/contributions.yaml`
- Companion test: `nz/statutes/kiwisaver/contributions.test.yaml`
- Pinned engine repo: `TheAxiomFoundation/axiom-rules-engine` at `732ad89f47035987ed0510979514aa405a1ee47c`
- Pinned rulespec repo: `TheAxiomFoundation/rulespec-nz` at `3c6436b2ecf82dd7a7f7810a406a2695a64af33a`

### Title

`KiwiSaver contributions module fails to compile with the pinned Axiom RuleSpec engine`

### Summary

The KiwiSaver contributions module currently fails during `axiom-rules-engine compile`, which blocks that slice from the live validation suite. The same pinned engine compiles and runs the GST, ACC earners levy, income tax, and New Zealand Superannuation slices successfully.

### Reproduction

```bash
AXIOM_RULESPEC_REPO_ROOTS=.external-repos/rulespec-nz \
  .external-repos/axiom-rules-engine/target/debug/axiom-rules-engine compile \
  --program .external-repos/rulespec-nz/nz/statutes/kiwisaver/contributions.yaml \
  --output /tmp/rulespec-nz-kiwisaver-contributions.compiled.json
```

Observed error:

```text
failed to load RuleSpec module `.external-repos/rulespec-nz/nz/statutes/kiwisaver/contributions.yaml`:
yaml parse error: rules[1].versions[0].values: invalid type: sequence, expected a map at line 44 column 11
```

### Expected

The module should compile in the same way as the other selected `rulespec-nz` slices, or the module should be updated to the engine-supported structure if the current `values` shape is no longer valid.

### Impact

- Blocks the KiwiSaver slice from the live validation suite.
- Prevents the harness from reaching the selected-validation coverage target with the pinned engine.
- Does not affect the already-green GST, ACC earners levy, income tax, or New Zealand Superannuation slices.

### Draft issue body

The KiwiSaver contributions module fails to compile under the pinned Axiom RuleSpec engine:

```text
failed to load RuleSpec module `.external-repos/rulespec-nz/nz/statutes/kiwisaver/contributions.yaml`:
yaml parse error: rules[1].versions[0].values: invalid type: sequence, expected a map at line 44 column 11
```

This blocks KiwiSaver from the live validation suite in `rulesandprocesses`.
The same pinned engine compiles and runs GST, ACC earners levy, income tax,
and New Zealand Superannuation slices successfully, so this appears isolated to
the KiwiSaver module shape or a parser expectation mismatch.

Please confirm whether the `versions[0].values` shape in this module is still
supported. If not, I can update the module to the current schema shape or apply
the corresponding compatibility fix once the intended contract is clear.
