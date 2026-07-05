# OpenFisca missingness cases

Track: `engine_contributions_20260704` phase 2 C-B
Status: local evidence draft, upstream submission remains `[HUMAN]`

## Environment

- `openfisca-core`: local editable checkout at `.external-repos/openfisca-core`
- `openfisca-france`: local editable checkout at `.external-repos/openfisca-france`
- Isolated runtime used for the runs below: `.venv-openfisca`

## Evidence summary

OpenFisca-France also collapses omitted salary inputs into zero-valued inputs in the basic wage path. That means the engine cannot distinguish "not provided" from "intentionally zero" once the scenario has been built.

The probe used a two-parent household in France with `parent1` configured as a regular private-sector employee. Three cases were compared:

- `omitted_salary`: no `salaire_de_base` provided.
- `explicit_zero_salary`: the same scenario with `salaire_de_base = 0`.
- `positive_salary`: the same scenario with `salaire_de_base = 2000`.

Observed outputs:

```text
CASE omitted_salary
salaire_de_base [0.0, 0.0]
salaire_super_brut [0.0, 0.0]
CASE explicit_zero_salary
salaire_de_base [0.0, 0.0]
salaire_super_brut [0.0, 0.0]
CASE positive_salary
salaire_de_base [166.6666717529297, 0.0]
salaire_super_brut [170.17333984375, 0.0]
```

The first two cases are indistinguishable, which is the missingness problem in miniature.

## Runnable cases

### Case 1: Missing base salary is treated as zero

Input: the France scenario above without `salaire_de_base`.

Observed output:

- `salaire_de_base = [0.0, 0.0]`
- `salaire_super_brut = [0.0, 0.0]`

### Case 2: Explicit zero salary produces the same result as missing salary

Input: the same scenario with `salaire_de_base = 0`.

Observed output:

- `salaire_de_base = [0.0, 0.0]`
- `salaire_super_brut = [0.0, 0.0]`

### Case 3: Positive salary produces a different result

Input: the same scenario with `salaire_de_base = 2000`.

Observed output:

- `salaire_de_base = [166.6666717529297, 0.0]`
- `salaire_super_brut = [170.17333984375, 0.0]`

## Why this matters

For partially completed forms or screening workflows, the engine currently hides the difference between incomplete data and real zero values. That makes it impossible to propagate a "cannot determine yet" state through the model. A `valueState`-style input annotation would preserve that distinction.

## Source pointers

- France model salary input is declared without a missingness-aware default: `.external-repos/openfisca-france/openfisca_france/model/revenus/activite/salarie.py`
- The salary input uses `set_input_divide_by_period`, so omitted monthly salary data is normalized at the input boundary: `.external-repos/openfisca-france/openfisca_france/model/revenus/activite/salarie.py`
- `revenu_disponible` aggregates salary-derived income through the household model: `.external-repos/openfisca-france/openfisca_france/model/mesures.py`

