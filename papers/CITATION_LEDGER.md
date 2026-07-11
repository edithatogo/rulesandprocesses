# Shared citation and evidence ledger

Status: working ledger for the paper-completion track. Every manuscript claim must point to one or more rows and to a committed artifact where applicable.

| ID | Source | Role | Used by | Verification boundary |
|---|---|---|---|---|
| SRC-OIA-01 | https://www.legislation.govt.nz/act/public/1982/0156/latest/DLM65314.html | New Zealand Official Information Act text and definitions | Coupling paper | Primary legislation; effective text must be checked for the claimed date |
| SRC-IRD-01 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/tax-rates-for-individuals | NZ individual income-tax rates | NZ reconciliation | Official agency source; rates are time-varying |
| SRC-IRD-02 | https://www.ird.govt.nz/income-tax/income-tax-for-individuals/acc-clients-and-carers/acc-earners-levy-rates | NZ ACC earners levy | NZ reconciliation | Official agency source; rates and caps are time-varying |
| SRC-IRD-03 | https://www.ird.govt.nz/kiwisaver/kiwisaver-changes | NZ KiwiSaver rate changes | NZ reconciliation | Official agency source; eligibility and contribution scope remain limited |
| SRC-PE-01 | https://github.com/PolicyEngine/policyengine-taxsim | Independent differential-testing precedent | Coupling, SNAP | Public project description; not evidence for the study's numerical results |
| SRC-PRD-01 | https://github.com/Research-Division/policy-rules-database | PRD implementation and provenance boundary | SNAP | Upstream repository revision must be recorded for reruns |
| SRC-FNS-01 | https://www.fns.usda.gov/snap/eligibility | SNAP programme eligibility context | SNAP | Official federal source; state options require separate sources |
| SRC-RULESPEC-01 | https://github.com/TheAxiomFoundation/rulespec-nz | RuleSpec source and upstream compile gate | NZ reconciliation | Commit and manifest state are part of reproducibility |
| SRC-OF-AO-01 | https://github.com/BetterRules/openfisca-aotearoa | OpenFisca Aotearoa source and coverage boundary | NZ reconciliation | Package revision and dependency compatibility must be recorded |

## Claim rules

- A source supports the proposition stated, not a stronger adjacent proposition.
- A secondary source cannot support a confirmed legal or engine-bug claim when a primary source is required.
- Time-varying sources require an effective date in the artifact or the claim is marked unresolved.
- Engine agreement is not an independent legal oracle.
