# RaC Conformance v1 Levels and Evidence

Status: draft for v1 foundation review  
Owner: RaC Conformance maintainers  
Last reviewed: 2026-07-15

Conformance describes evidence about a declared artifact and test scope. It is
not a claim of legal, clinical, welfare, funding, or standards-body authority.
Every result MUST name the artifact version, subject, jurisdiction/profile (if
applicable), test scope, observation time, and evidence locations.

## Levels

| Level | Question answered | Deterministic minimum evidence | Does not establish |
| --- | --- | --- | --- |
| `syntactic` | Does the artifact validate against its declared PIC schema? | Schema version, validator version, valid corpus result, invalid corpus result | Semantic correctness or source authority |
| `semantic` | Does the artifact obey the declared PIC semantic rules? | Semantic test result, canonical serialization, edge-case corpus, rejected-value evidence | Correctness of an external engine or law |
| `execution` | Does the declared runner produce the expected typed result for the stated inputs? | Pinned runner/dependency versions, executable command, input fixture, output, exit status | Jurisdictional validity or independent adoption |
| `trace` | Does execution emit a complete and schema-valid trace? | Trace artifact, trace schema result, input/output linkage, missingness and error semantics | Provenance of the underlying policy text |
| `source` | Are the encoded assumptions linked to controlling primary or official sources? | Source identifier, effective date, retrieval date, quoted or structured assertion, scope and limitations | That the source interpretation is uncontested |
| `independently_certified` | Has a qualified independent party reviewed and certified the declared scope? | Named certifier, independence statement, reviewed commit/digest, method, exceptions, date, certification record | Government endorsement or universal portability |

Levels are cumulative for a claim: a higher level MUST reference evidence for
all lower levels that it relies on. A source-level result cannot be inferred
from a syntactic pass. An independently certified result cannot be inferred
from repository ownership, a paper citation, a self-certified demo, or a
maintainer statement.

## Evidence states

Every gate and conformance result MUST use exactly one state:

| State | Meaning | Release effect |
| --- | --- | --- |
| `pass` | All required deterministic checks and evidence are present, current, and within scope | May satisfy this gate |
| `fail` | A required check ran and did not meet its declared assertion | Blocks the dependent gate |
| `blocked` | A required external, human, primary-source, or unavailable-runtime dependency cannot yet be completed | Blocks the dependent gate; never converted to pass locally |
| `exception` | A named deviation has an owner, rationale, scope, expiry/review date, and approval record | Blocks GA unless the gate explicitly permits the exception |
| `not_applicable` | The gate is explicitly outside the artifact's declared scope with a recorded reason | Does not block, but cannot be used as evidence for another gate |

`pass` MUST include evidence links or content digests. `fail`, `blocked`, and
`exception` MUST include a stable reason code and the next action. A missing or
ambiguous state is invalid. “Pending”, “complete”, and “verified” are prose
descriptions, not v1 gate states.

## Independence requirements

Repository tests may establish syntactic, semantic, execution, and trace
evidence for repository-owned artifacts. Source evidence requires controlling
primary or official assertions and their effective dates. Independent
certification requires a reviewer who did not author the implementation or
promote its golden fixtures, and must identify the reviewed digest.

AI-generated drafts MAY help assemble candidates, but deterministic validators
MUST make the release decision and a human MUST certify any human-gated or
independence-gated evidence. No runtime path may call an AI system to decide a
conformance result.

## Claim boundaries

Badges, reports, and release notes MUST say what was tested and what was not.
They MUST NOT use conformance to imply legal compliance, clinical safety,
funding eligibility, official policy status, standards-body endorsement, or
universal jurisdictional portability. A profile-specific result must remain
profile-specific when reused by another repository or paper.
