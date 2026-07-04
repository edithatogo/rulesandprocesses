# Red-team notes

## Failure modes

1. RaCX becomes too large to implement.
2. The canonical package becomes an unacknowledged new DSL/IR.
3. Standards mapping becomes superficial and non-executable.
4. OpenFisca/PolicyEngine maintainers see no immediate benefit.
5. AI-generated mappings create false semantic equivalence.
6. Process integration overcouples reusable calculations to one service channel.
7. Legal reviewers reject computational artifacts as insufficiently authoritative.
8. Traces are too verbose to use or too shallow to audit.
9. Concept registry governance becomes political or under-resourced.
10. v0.1 attempts formula translation before metadata/test/trace exchange works.

## Countermeasures

- Keep RaCX-Core small.
- Publish conformance fixtures early.
- Require explicit profile declarations.
- Use sidecar-first adoption.
- Compare traces, not just values.
- Separate decision-service interfaces from process bindings.
- Make AI outputs reviewable drafts.
- Use public versioned registries and deprecation policies.
- Build reference validators and example adapters.
