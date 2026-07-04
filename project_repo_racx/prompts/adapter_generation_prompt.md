# Adapter generation prompt draft

Given a RaCX package and a target engine specification, draft an adapter that maps RaCX concepts, variables, parameters, tests, and traces to the target engine.

Constraints:

- Do not translate arbitrary formulas unless they are within the declared expression profile.
- Preserve source references.
- Emit trace-compatible IDs.
- Generate tests that compare native engine output to RaCX expected output.
- Mark unsupported constructs explicitly.
