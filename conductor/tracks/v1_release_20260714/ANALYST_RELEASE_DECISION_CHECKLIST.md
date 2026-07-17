# v1 Release Analyst Decision Checklist

**Review posture:** analyst-facing preparation only. This checklist does not
approve, sign, promote, publish, or alter any release gate.

**Review base:** `54d6c93`. Re-run the evidence checks and pin the resulting
commit and artifact set before recording a release decision.

## Release boundary

The analyst is deciding whether the current evidence is sufficient to recommend
one of: continue 0.x, request remediation, or send a separately authorized
release candidate for human approval. This is not itself release
authorization. No package, tag, DOI, announcement, or public artifact may be
treated as published from this checklist.

## Exact evidence links

| ID | Evidence link | Pin | What it establishes / does not establish |
| --- | --- | --- | --- |
| R1 | [`release/v1/gates.json`](../../../release/v1/gates.json) | `8be63eb89f330df4db404881345ec407326994704209b8ce75ed47c1e636f350` | Current local gate record; not hosted or human proof. |
| R2 | [`security/RISK_REGISTER.json`](../../../security/RISK_REGISTER.json) | `123b63a38c063f6b0f8ddd1394764ee7245be67d8cefb11348a41cf2a824d3e5` | Residual risk dispositions; not a risk acceptance. |
| R3 | [`security/THREAT_MODEL.md`](../../../security/THREAT_MODEL.md) | `f500e332d047befcac045174c05876b5445dadf96612488392cce399fcc2d793` | Threat/control model and named review boundary. |
| R4 | [`security/PROVENANCE.md`](../../../security/PROVENANCE.md) | `b544b37c8d96bbb28d8f323880ebb5757c6bbd2e61bf5bb12b1cda5e52ba6586` | Local reproducibility anchor and explicit hosted-attestation gap. |
| R5 | [`security/SBOM.spdx.json`](../../../security/SBOM.spdx.json) | `9aeb6c351a59eebc3b5bfdb0590427ce18decb2ccb3d7622bea6c5742a4e9fad` | Local SPDX evidence; not package-manager or hosted provenance. |
| R6 | [`security/ROLLBACK_REHEARSAL.md`](../../../security/ROLLBACK_REHEARSAL.md) | `de7a301c7cb0d387a37cf5e6ede465b51631b43e696ca00f2d049fe5c783e3ca` | Tabletop procedure; not evidence of a live rollback. |
| R7 | [`release/v1/README.md`](../../../release/v1/README.md) | Re-pin at review | Publication/signing boundary and regeneration requirement. |
| R8 | [`conductor/tracks/v1_release_20260714/spec.md`](./spec.md) | Re-pin at review | Normative release acceptance criteria and human gates. |
| R9 | [`conductor/NEXTGEN_RELEASE_STATUS.md`](../../NEXTGEN_RELEASE_STATUS.md) | Re-pin at review | Programme-level external and human gate context. |
| R10 | [`conductor/tracks/core_model_demonstrator_20260717/ANALYST_DECISION_PACKET.md`](../core_model_demonstrator_20260717/ANALYST_DECISION_PACKET.md) | This review set | FOI demonstrator boundary; it is not a release qualification result. |

## Residual release-risk review

For each item, record evidence, owner, and disposition. `Open` is the default
until the analyst has a current, independently checkable artifact.

| Risk | Current review question | Default disposition |
| --- | --- | --- |
| Source/profile authority | Is the FOI compatibility boundary human-reviewed, with candidate status and representational loss preserved? | Open; see R10. |
| Hosted security and workflow evidence | Are hosted checks, action/dependency review, SBOM publication, and attestation results available for this exact candidate? | Open; local files do not prove them. |
| Signing and provenance | Is there an authorized signing identity, signed immutable artifact, checksum, and verifiable provenance statement for the exact release bytes? | Open; no signing authorization is implied. |
| Reproducibility | Do two clean environments produce identical release artifacts, not only deterministic local test output? | Open until artifact manifests are attached. |
| Rollback | Has the documented procedure been exercised against a public artifact and recorded? | Open; R6 is tabletop procedure only. |
| External adoption and source rights | Are external consumer evidence, maintainer decisions, and redistribution rights current and exact? | Open unless separately evidenced. |
| Human authorization | Has the authorized reviewer approved a specific commit and artifact set? | Open; this checklist cannot supply approval. |

## Signing/provenance checklist

- [ ] Reviewed commit/tag is recorded: `______________________________`
- [ ] Artifact filenames and SHA-256 digests are attached: `________________`
- [ ] SBOM corresponds to those exact bytes: `____________________________`
- [ ] Provenance attestation URL or immutable local evidence is attached: `__`
- [ ] Signing identity and authorization source are recorded: `_____________`
- [ ] Signature verification was independently repeated: `__________________`
- [ ] No unsigned or locally generated artifact is described as released.

## Analyst conclusion

- Recommendation: `continue 0.x | remediation required | ready for separate human authorization`
- Analyst: `______________________________`
- Date: `__________________`
- Exact commit/artifact set: `______________________________`
- Unresolved risks and owners: `______________________________`

This section is intentionally blank. An agent must not complete it or change
machine-facing status fields in `plan.md`, `metadata.json`, or release
manifests.
