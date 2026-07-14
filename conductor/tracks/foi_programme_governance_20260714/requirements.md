# Requirements (MoSCoW)

| Priority | Requirement | Verification |
|---|---|---|
| Must | Keep Project 14 FOI-focused and repository-native Conductor plans authoritative. | Allowlist and drift checks. |
| Must | Pin FOI-O, PIC, legislation, archive, Hugging Face, NLP, jurisdiction, and calendar revisions. | Compatibility-manifest validation. |
| Must | Preserve FOI-O governance axes separately from PIC `valueState`. | Lossless crosswalk tests. |
| Must | Keep candidate-to-gold promotion and legal certification human-gated. | Negative governance fixtures. |
| Should | Synchronize Project status with live local track status. | Project evidence and reconciliation report. |
| Should | Test against published immutable artifacts, not checkout-relative paths. | CI compatibility matrix. |
| Could | Add signed/OCI distribution of evidence bundles. | Optional release gate. |
| Won't | Make PIC a FOI-O runtime dependency or mirror unrelated repository issues. | Boundary review. |
