# v1 Supply-Chain Evidence

Observed: 2026-07-16 from the RaC v1 integration worktree.

## Local evidence

| Check | Result | Evidence or limitation |
| --- | --- | --- |
| Workflow action pinning | pass | Every `uses:` reference in `.github/workflows/` uses an immutable commit SHA. |
| Workflow permissions | pass | Workflows declare least-privilege top-level permissions; CodeQL separately requests `security-events: write` for its required upload. |
| Workflow security audit | pass | `uvx zizmor .github/workflows` reported no findings; 10 informational findings are suppressed by existing configuration. |
| Dependency vulnerability audit | pass with limitation | `pip-audit` found no known vulnerabilities in the contract-tool environment. The local editable `pic-contracts` package is not present on PyPI and was not auditable as a distribution. |
| Dependency locking | pass | `contracts/tools/uv.lock` and `converters/fixtures/uv.lock` are tracked. |
| SBOM | pass | `docs/V1_SBOM.json` is a CycloneDX JSON inventory generated with reproducible output. |
| Secret scanning | not locally certifiable | Hosted secret scanning and push protection require GitHub-side verification. |
| Branch protection | not locally certifiable | Required checks and approval rules require GitHub-side verification. |
| Release environment protection | not locally certifiable | Signing, protected environments, and artifact attestations require hosted verification. |

## Release disposition

The local controls are suitable for continued engineering, but the v1 release
remains blocked until the hosted controls are verified and recorded. A clean
local audit must not be represented as proof that GitHub branch protection,
secret scanning, signing, or release permissions are configured.
