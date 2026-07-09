**Status (2026-07-09): submitted.** https://github.com/openfisca/openfisca-core/issues/1380

# Draft OpenFisca Issue: missingness semantics

Target repository: `openfisca/openfisca-core` and/or `openfisca/openfisca-france`

Suggested title:

`Proposal: preserve missing-input state instead of collapsing it to zero`

## Draft body

I have been testing France scenarios in OpenFisca, and I found that omitted salary inputs are treated the same as explicit zeros once the scenario is built.

Concrete local evidence:

- Without `salaire_de_base`:
  - `salaire_de_base = [0.0, 0.0]`
  - `salaire_super_brut = [0.0, 0.0]`
- With `salaire_de_base = 0`:
  - `salaire_de_base = [0.0, 0.0]`
  - `salaire_super_brut = [0.0, 0.0]`
- With `salaire_de_base = 2000`:
  - `salaire_de_base = [166.6666717529297, 0.0]`
  - `salaire_super_brut = [170.17333984375, 0.0]`

That is convenient for fully specified simulations, but it erases the difference between:

1. The user intentionally entered zero, and
2. The user did not provide the field at all.

For screener-style or partially completed scenarios, that distinction matters. A missing salary field should usually propagate as unknown or incomplete instead of being silently normalized to zero.

Would maintainers consider one of these approaches idiomatic?

- A preserved missingness state on input holders
- An explicit `valueState`-style annotation for inputs
- A documented partial-input mode that propagates "cannot determine" rather than defaulting to zero

I am not proposing an engine-wide rewrite here. I am asking whether there is an accepted way to distinguish missing from zero today. If not, I would be glad to follow up with a narrow proposal.

## Local evidence

- `external/openfisca/MISSINGNESS_CASES.md`
- local OpenFisca runtime run with `openfisca-core==44.7.0` and `openfisca-france==175.1.0`
