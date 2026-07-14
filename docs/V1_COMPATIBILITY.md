# RaC Conformance v1 Compatibility and Migration Policy

Status: draft for v1 foundation review  
Owner: RaC Conformance maintainers  
Last reviewed: 2026-07-15

This policy applies to the public PIC contracts and the documented
`pic-validate`, `pic-diff`, and `pic-foio-check` command-line interfaces. It
does not make study runners, external snapshots, demos, or adapters core
dependencies.

## Versioning boundaries

Each PIC package is independently versioned. The aggregate `pic-contracts`
tooling package has its own version and MUST declare the contract versions it
discovers or validates. A release MUST NOT silently change a contract schema,
CLI exit status, or canonical artifact meaning.

| Change | Package version | Required evidence |
| --- | --- | --- |
| Documentation, comments, or a clarification that cannot change validation | Patch | Changelog and unchanged example corpus |
| Backward-compatible optional field or additive enum value with explicit consumer behavior | Minor | Valid/invalid corpus, compatibility test, and migration note |
| Removal, type change, required-field change, identifier reinterpretation, canonicalization change, or incompatible CLI behavior | Major | Before/after fixtures, migration artifact, compatibility report, and deprecation history where possible |

For packages below 1.0, a breaking change MUST still be made explicit in the
package changelog and migration notes; a `0.x` number is not permission to
silently break consumers. The v1 programme version does not collapse the
independent PIC package versions.

## Serialization and identifiers

- Plain JSON is the canonical interchange form. YAML is import-only and MUST
  be normalized to the canonical JSON representation before comparison.
- Money and precise decimals remain decimal strings; binary floats are never a
  compatible interchange representation.
- Existing package-scoped identifiers retain their meaning for the lifetime of
  a major package version. Reuse of an identifier for a different concept is a
  breaking change even if the JSON schema still validates.
- Versioned schema directories and `conformsTo` values are immutable evidence
  references. A corrected artifact receives a new version or an explicitly
  documented replacement, never an in-place rewrite.
- CLI exit statuses and machine-readable output fields documented by a release
  are compatibility surfaces. Human-readable wording is not stable API.

## Deprecation and migration

An announced deprecation MUST identify the affected package, field or command,
replacement, first release, removal target, owner, and migration example. A
normal deprecation notice SHOULD remain for at least two minor releases or 90
days, whichever is longer, unless a security issue requires earlier removal.

A breaking release MUST include:

1. a before/after example;
2. a deterministic migration or an explicit statement that migration cannot be
   automated;
3. a compatibility matrix covering the last supported release;
4. updated valid and invalid example corpora; and
5. rollback guidance identifying the last compatible release.

Consumers MUST pin the contract versions they rely on and MUST report their
consumed versions in evidence artifacts. The repository may reject an
unrecognized future major version rather than guessing its semantics.

## Representative compatibility checks

The existing example and validator suites provide the baseline classifications
used by release review:

| Scenario | Classification | Evidence check |
| --- | --- | --- |
| Add an optional field to a versioned contract while old valid examples still validate | Compatible additive change | `contracts/tools/tests/test_pic_v02_schemas.py` and the example corpus gate |
| Preserve v0.1 validation while a v0.2 schema is added | Compatible parallel version | `contracts/tools/tests/test_pic_v02_schemas.py` |
| Change a required field, type, identifier meaning, or trace value-state rule | Breaking change | Invalid examples and the affected contract test module must reject the old shape or require a new version |
| Change `pic-validate` or `pic-diff` exit behavior | CLI breaking change | `contracts/tools/tests/test_cli_and_example_gates.py` and CLI compatibility review |

These checks classify schema and CLI behavior; they do not prove semantic or
source correctness. A release review records the exact test command and commit
digest alongside the compatibility decision.

## Compatibility claims

“Compatible” means that the declared consumer can validate and interpret the
declared artifact under the cited versions and test scope. It does not mean
that two engines agree, that a jurisdictional rule is legally current, or that
an adapter is authoritative. Cross-repository compatibility remains a separate
evidence gate and requires source, version, and digest provenance.
