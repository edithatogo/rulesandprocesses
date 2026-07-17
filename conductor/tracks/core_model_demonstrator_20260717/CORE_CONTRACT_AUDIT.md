# Core Contract Audit

Audit date: 2026-07-17
Audit branch: `codex/focused-core-demonstrator`
Evidence state: `pass` for repository-local contract checks.

## Corpus inventory

| Contract | Valid examples | Invalid examples |
| --- | ---: | ---: |
| `pic-crosswalk` | 2 | 4 |
| `pic-fixtures` | 2 | 3 |
| `pic-foio-compatibility` | 2 | 3 |
| `pic-parameters` | 3 | 4 |
| `pic-semantics` | 2 | 3 |
| `pic-traces` | 3 | 4 |
| `pic-process-profile` | 3 | 9 |

Every core schema has both positive and negative examples. The process-profile
validator rejects missing authority, missing effective dates for controlling
assertions, invalid references, invalid temporal ordering, and non-deterministic
rule invocations.

## Verification

- `PYTHONPATH=. uv run python -m tools.repo_audit` passed.
- `make check` passed: 70 repository tests, 105 contract-tool tests, 25
  converter tests, and all harness, study, and demo suites.
- Contract-tool coverage: 84.94%, above the 80% gate.
- Example validation passed for all contracts.
- Repository/runtime scan found no runtime AI dependency under core contracts,
  tools, or harness code.
- Decimal-string money and bounded safety validation remain enforced by the
  existing contract and safety tests.

## Boundary

This audit proves repository-local syntactic, semantic, execution, and trace
checks only. It does not certify legal meaning, external adoption, independent
implementation, publication, or a v1.0 release.
