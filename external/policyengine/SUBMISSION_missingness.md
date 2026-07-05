# Draft PolicyEngine Issue: missingness semantics

Target repository: `PolicyEngine/policyengine-core`

Suggested title:

`Proposal: preserve missing-input state instead of collapsing it to zero`

## Draft body

I have been testing SNAP-style screener flows in `policyengine-us`, and I found that omitted monetary inputs behave the same as explicit zeros at the engine boundary.

Concrete examples from a local Texas SNAP household:

- No `employment_income` / `self_employment_income` provided:
  - `snap_gross_income = 0.0`
  - `snap_net_income = 0.0`
  - `snap = 291.0`
- No `child_support_expense` provided:
  - `snap_child_support_deduction = 0.0`
- No `housing_cost` provided:
  - `snap_excess_shelter_expense_deduction = 0.0`

That is convenient for fully specified simulations, but it makes it impossible to tell the difference between:

1. The user intentionally entered zero, and
2. The user did not provide the field at all.

For screener-style and partially completed scenarios, that distinction matters. A missing income field should usually be represented as unknown or incomplete, not silently coerced to zero.

Would maintainers consider one of these approaches idiomatic?

- A preserved missingness state on input holders
- An explicit `valueState`-like annotation for inputs
- A documented partial-input mode that propagates "cannot determine" rather than defaulting to zero

I am not proposing an engine-wide rewrite here. I am asking whether there is an accepted way to distinguish missing from zero today. If not, I would be glad to follow up with a narrow proposal.

Footnote: this repo's `pic-semantics` contract already models `valueState` explicitly, so the distinction is already available in downstream interchange artifacts.

## Local evidence

- `external/policyengine/MISSINGNESS_CASES.md`
- local PolicyEngine runtime run with `policyengine-core==3.28.0` and `policyengine-us==1.755.5`

