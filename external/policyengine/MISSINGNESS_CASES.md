# PolicyEngine missingness cases

Track: `engine_contributions_20260704` phase 2 C-B
Status: local evidence draft, upstream submission remains `[HUMAN]`

## Environment

- `policyengine-core`: local editable checkout at `.external-repos/policyengine-core`
- `policyengine-us`: local editable checkout at `.external-repos/policyengine-us`
- Installed runtime used for the runs below: `.venv-policyengine`

## Evidence summary

PolicyEngine accepts omitted household inputs as if they were zero-valued inputs in the SNAP path below. That is not just a neutral default: it collapses "not provided" into the same code path as a real zero, so screener-style usage cannot distinguish missing information from a deliberate zero.

The single-household probe used one adult in Texas with the SNAP work-requirement flags set true. Two runs were compared:

- `missing_all`: no monetary inputs were provided.
- `explicit_income_and_expenses`: the same household with `employment_income=1200`, `self_employment_income=0`, `child_support_expense=500`, and `housing_cost=600`.

Observed outputs:

```text
CASE missing_all
snap_gross_income [0.0]
snap_child_support_deduction [0.0]
snap_excess_shelter_expense_deduction [0.0]
snap [291.0]
CASE explicit_income_and_expenses
snap_gross_income [58.33333206176758]
snap_child_support_deduction [0.0]
snap_excess_shelter_expense_deduction [50.0]
snap [291.0]
```

The omitted-input run is also identical to an explicit-zero run for the same variables:

```text
CASE omitted
snap_gross_income [0.0]
snap_net_income [0.0]
snap_child_support_deduction [0.0]
snap_excess_shelter_expense_deduction [0.0]
snap [291.0]
CASE explicit_zero_income
snap_gross_income [0.0]
snap_net_income [0.0]
snap_child_support_deduction [0.0]
snap_excess_shelter_expense_deduction [0.0]
snap [291.0]
```

## Runnable cases

### Case 1: Missing income is treated as zero income

Input: household with no `employment_income` or `self_employment_income`.

Observed output:

- `snap_gross_income = 0.0`
- `snap_net_income = 0.0`
- `snap = 291.0`

### Case 2: Missing child support expense is treated as zero expense

Input: same household, no `child_support_expense`.

Observed output:

- `snap_child_support_deduction = 0.0`

### Case 3: Missing housing cost is treated as zero housing cost

Input: same household, no `housing_cost`.

Observed output:

- `snap_excess_shelter_expense_deduction = 0.0`

## Why this matters

The SNAP screener path now behaves as if every absent monetary field means zero. For users who do not know whether a field is unknown or genuinely zero, that can produce a false sense of certainty. A `valueState`-style input annotation would let the engine preserve the distinction instead of collapsing it at the input boundary.

## Source pointers

- SNAP gross income sums `snap_earned_income` and `snap_unearned_income`: `.external-repos/policyengine-us/policyengine_us/variables/gov/usda/snap/income/gross/snap_gross_income.py`
- SNAP child support deductions read `child_support_expense`: `.external-repos/policyengine-us/policyengine_us/variables/gov/usda/snap/income/gross/snap_child_support_gross_income_deduction.py`
- SNAP shelter deductions read `housing_cost`: `.external-repos/policyengine-us/policyengine_us/variables/gov/usda/snap/income/deductions/shelter/snap_excess_shelter_expense_deduction.py`
- Direct input defaulting comes from the holder/simulation layer in PolicyEngine core, which stores absent inputs as zero-equivalent defaults rather than an explicit missingness state: `.external-repos/policyengine-core/policyengine_core/holders/holder.py`

