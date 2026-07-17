# Core Model and Demonstrator Completion

## Objective

Complete the smallest defensible RaC Conformance evidence package: stable PIC
contracts, the platform-neutral process profile, one human-certified FOI-O
process demonstrator, deterministic trace evidence, and repository-local
hardening.

This track is the active implementation priority. It does not attempt to prove
external adoption, platform portability, multi-jurisdiction breadth, paper
publication, repository extraction, or a 1.0 release.

## In scope

- Normative PIC contracts, validators, compatibility tools, and example corpus.
- `pic-process-profile/0.1.0` and its authority/source semantics.
- FOI-O candidate compatibility and the deterministic foi-process trace path.
- Human certification of the FOI-O source and mapping exceptions.
- Local hostile-input, property, mutation, reproducibility, and repository CI
  evidence required to show the package is safe to implement and run.
- A final core-readiness packet that states exactly what is proven and what is
  deferred.

## Out of scope and deferred

- Health-technology pathway breadth and Australian/UK/US expansion.
- Camunda or other workflow-platform adapters.
- Independent external implementation and adoption claims.
- Public process-mappings canonical cutover and release policy execution.
- Papers, arXiv, Zenodo, DOI, public announcement, and v1.0 publication.

## Safety and authority boundary

No runtime AI decisions are permitted. Candidate mappings remain
`agent-proposed` until human certification. The demonstrator establishes
interchange, validation, execution, and trace evidence; it does not establish
legal correctness, government endorsement, universal portability, or clinical,
funding, or policy authority.

## Completion outcome

Completion produces a reproducible core demonstrator package that an
independent implementer can inspect and run locally, together with an explicit
deferred-work ledger and human certification record.
