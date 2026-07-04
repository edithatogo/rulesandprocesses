# pic-fixtures 0.1.0

`pic-fixtures` defines engine-neutral test fixtures. Fixtures describe inputs, expected outputs, provenance, and source references; they do not define how an engine computes the result.

## File Shape

```json
{
  "conformsTo": "pic-fixtures/0.1.0",
  "provenance": {
    "curator": "Dylan",
    "method": "ai-proposed",
    "source": "Ombudsman worked example",
    "interpreterOfRecord": "pending human review",
    "disclaimer": "Interpretation, not law."
  },
  "cases": []
}
```

## Case Shape

Each case has:

- `caseId`: stable package-scoped fixture ID.
- `description`: short human-facing description.
- `period`: period under test.
- `entities`: engine-neutral entity data.
- `inputs`: mapping from PIC IDs to `pic-semantics` value objects.
- `expected`: mapping from PIC IDs to value objects plus optional `tolerance`.
- `sourceRefs`: source references for the interpretation.

Inputs may omit `value` when the `valueState` is enough, for example `not_provided`. Money and tolerances are decimal strings.

## Provenance

Fixture files must carry top-level provenance. Agents may draft fixtures with `method: "ai-proposed"`; promotion to human-approved golden fixtures requires Dylan's review.

