# RaCX profiles

RaCX is too broad for one mandatory implementation target. Profiles let engines adopt the parts that fit their role.

## RaCX-Core

Required for all packages. Contains manifest, IDs, concepts, variables, parameters, source refs, mappings, tests, and trace contracts.

## RaCX-Calc

For calculation/eligibility engines. Adds expressions, decision services, rounding, periods, missingness semantics, and result traces.

## RaCX-Simulation

For microsimulation. Adds population entities, household units, weights, baselines, reforms, metrics, and dataset metadata.

## RaCX-Evidence

For implementation. Adds evidence requirements, sources, verification methods, confidence, expiry, and manual override semantics.

## RaCX-Process

For deterministic workflows. Adds process steps, events, transitions, decision invocations, notices, and review paths. May export to BPMN or XState subsets.

## RaCX-Case

For discretionary and non-linear case management. Adds available actions, human decision points, required reasons, and review rights. May export to CMMN subsets.

## RaCX-Trace

For assurance. Defines decision traces, process traces, semantic equivalence criteria, and conformance reporting.
