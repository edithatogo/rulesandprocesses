# pic-semantics 0.1.0

`pic-semantics` defines the shared vocabulary imported by the other Policy Interchange Contracts. It does not define an expression language or a runtime. Engines remain responsible for calculation semantics and may declare stricter behavior in runner manifests.

## Value States

| `valueState` | Meaning |
|---|---|
| `known` | A concrete value is available and should be used. |
| `zero` | The value is explicitly zero, distinct from unknown or omitted. |
| `false` | The value is explicitly boolean false, distinct from unknown or omitted. |
| `unknown` | The value cannot be determined from available evidence. |
| `not_provided` | The value was requested or expected but not supplied. |
| `not_applicable` | The value does not apply to this case. |
| `provided_unverified` | A supplied value exists but has not been checked. |
| `verified_stale` | A value was previously verified but may no longer be current. |
| `conflicting` | Multiple available values conflict and cannot be deterministically reconciled. |

## Epistemic Status

| `epistemicStatus` | Meaning |
|---|---|
| `observed` | Directly observed in source data or an event log. |
| `inferred` | Derived from other observed or asserted facts. |
| `asserted` | Supplied by a person or system without independent certification. |
| `certified` | Certified by an accountable human or institutional process. |
| `unknown` | Epistemic basis is not known. |

## Propagation Table

Default propagation follows conservative three-valued logic. Implementations may be stricter but must not silently turn unknown, missing, stale, or conflicting values into ordinary known values.

| Operation | Rule |
|---|---|
| `and` | `false AND anything = false`; `unknown AND false = false`; `unknown AND true = unknown`; any `conflicting` operand yields `unknown-with-warning` unless the other operand is `false`. |
| `or` | `true OR anything = true`; `unknown OR true = true`; `unknown OR false = unknown`; any `conflicting` operand yields `unknown-with-warning` unless the other operand is `true`. |
| `not` | `not false = true`; `not known boolean true = false`; `not unknown = unknown`; `not conflicting = unknown-with-warning`. |
| comparison | Comparisons over `known`, `zero`, or `false` values return known booleans. Comparisons involving `unknown`, `not_provided`, `provided_unverified`, `verified_stale`, or `conflicting` return `unknown` and should carry a warning when the stale or conflicting state is material. |
| arithmetic | Arithmetic with only `known` and `zero` operands returns `known`. Arithmetic with any other value state returns `unknown`; `conflicting` and `verified_stale` should carry warnings. |
| `if` | If the condition is known true or false, evaluate the selected branch. If the condition is unknown, the result is unknown unless both branches are equivalent at the claimed trace-equivalence level. |

## Worked Examples

| Expression | Result |
|---|---|
| `unknown AND false` | `false` |
| `unknown + 5` | `unknown` |
| `verified_stale < threshold` | `unknown-with-warning` |

## Data Types

| `dataType` | Rules |
|---|---|
| `boolean` | JSON boolean values, or `valueState: false` for explicit false. |
| `integer` | JSON integer values only. |
| `decimal` | Decimal strings. |
| `money` | Decimal strings plus a three-letter `currency`. |
| `string` | JSON string values. |
| `date` | ISO 8601 date string. |
| `enum` | String value constrained by a contract-local `allowedValues` list. |
| `duration_working_days` | Integer count of working days under a declared calendar. |
| `duration_calendar_days` | Integer count of calendar days. |

## Rounding

Rounding declarations use:

```json
{"mode": "half_up", "scale": 2}
```

Allowed modes are `half_up`, `half_even`, `floor`, and `ceil`. `scale` is a non-negative integer.

