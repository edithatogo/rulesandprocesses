# RaC Conformance v1 Scope

Status: draft for v1 foundation review  
Owner: RaC Conformance maintainers  
Last reviewed: 2026-07-15

This document is the v1 product-boundary inventory. It distinguishes what the
repository promises to preserve from material that is a profile, an adapter,
an experiment, or an internal implementation detail. A surface is not part of
the v1 guarantee merely because it is present in the repository.

## Stability classes

| Class | Meaning | v1 promise |
| --- | --- | --- |
| Core | Public PIC contract or validator required for interoperable use | SemVer-governed compatibility and deterministic validation |
| Optional profile | A published domain or jurisdiction contract that consumes core PIC contracts | Maintained independently; never a core runtime dependency |
| Jurisdiction profile | A profile containing jurisdiction-specific law, policy, or effective dates | Explicit jurisdiction/version scope; no portability claim |
| Adapter | A boundary integration for an external engine or service | Version-pinned and replaceable; no claim that the target is authoritative |
| Experimental | Research, prototype, or incomplete surface | No compatibility or support commitment |
| Internal | Repository tooling, generated reports, fixtures, and development scaffolding | May change without public API compatibility, subject to reproducibility needs |

## Normative and optional surfaces

| Surface | Owner | Class | v1 support posture |
| --- | --- | --- | --- |
| `contracts/pic-crosswalk/0.1.0` | PIC maintainers | Core | Validate and document; additive changes require a new compatible release or explicit migration |
| `contracts/pic-fixtures/0.1.0` | PIC maintainers | Core | Validate and document; fixtures remain evidence artifacts and require human curation |
| `contracts/pic-parameters/0.1.0` and `0.2.0` | PIC maintainers | Core | Validate both published versions; preserve versioned schemas and migration notes |
| `contracts/pic-semantics/0.1.0` | PIC maintainers | Core | Validate and document value-state semantics and decimal-string money rules |
| `contracts/pic-traces/0.1.0` and `0.2.0` | PIC maintainers | Core | Validate and document trace shape and version compatibility |
| `contracts/pic-foio-compatibility/0.1.0` | PIC maintainers | Optional profile | Maintain the FOI-O bridge as an independently versioned consumer contract |
| `contracts/tools/src/pic_contracts` | PIC maintainers | Core | Support deterministic validation, diff, compatibility, and example-corpus CLIs |
| `contracts/tools` command-line tools | PIC maintainers | Core | Preserve documented exit status and machine-readable output semantics |
| `converters/fixtures` converters | Fixture-converter maintainers | Adapter | Support only declared source formats and pinned samples; reject unsupported constructs |
| `harness/axiom` | Harness maintainers | Adapter | Support measured Axiom/OpenFisca-compatible execution only when its dependency is available |
| `harness/policyengine_trace` | Harness maintainers | Adapter | Support trace projection for the pinned PolicyEngine evidence shape |
| `studies/nz-reconciliation` | Study maintainers | Jurisdiction profile | Maintain as an NZ study interface; results are evidence, not a general legal engine |
| `studies/snap-divergence` | Study maintainers | Optional profile | Maintain the SNAP research profile and its deterministic comparison/triangulation tooling |
| `demos/service-boundaries` | Demo maintainers | Experimental | Demonstrate boundary patterns; no production compatibility promise |
| `demos/docassemble-oia-clock` | Demo maintainers | Experimental | Demonstrate a bounded OIA clock use case; no legal-authority claim |
| `external/*` snapshots and submission trees | Programme maintainers | Internal | Staged provenance and submission material only; not runtime dependencies or upstream releases |
| `papers`, `source_material`, `conversation`, `views` | Research/publication maintainers | Internal | Evidence and publication inputs; never treated as independent adoption or runtime authority |
| `tools`, `Makefile`, CI workflows | Repository maintainers | Internal | Required for reproducible repository checks; implementation may evolve without public API status |

## v1 non-goals and prohibited claims

v1 MUST NOT:

- present PIC or any adapter as legal, clinical, welfare, funding, or
  standards-body authority;
- make an external engine, jurisdiction profile, platform, or paper a core
  runtime dependency;
- imply that repository ownership, a paper citation, or a self-certified demo
  is independent adoption;
- promote AI-proposed mappings or fixture candidates without human review;
- silently treat generated artifacts, narrative source packs, or stale external
  snapshots as current primary-source evidence;
- promise that one jurisdiction profile transfers to another jurisdiction;
- use an experimental demo or study result as a v1 compatibility guarantee.

v1 also does not include new process profiles, a workflow-platform runtime, a
standards-body endorsement, or a 1.0 release. Those are separate roadmap
decisions and must consume this boundary rather than expand it implicitly.

## Ownership and change control

The maintainers own the core PIC contracts and validators. Profile, adapter,
study, and demo owners are responsible for their own versioned evidence and
support statements. A change that moves a surface between classes requires a
track task, an updated inventory, and a compatibility or migration record.

This inventory is repository-local evidence. External adoption, upstream
acceptance, human certification, legal source verification, and publication
deposition remain separate gates and cannot be inferred from this document.
