# Prompt for Claude Fable 5: second-opinion review of RaCX policy exchange proposal

You are Claude Fable 5. Please review the attached zip as a complete context pack. The purpose is to get a rigorous second opinion on a proposed Rules-as-Code interoperability/exchange architecture.

## Context

Dylan works with PolicyEngine and its newer Axiom software. The goal is not to replace OpenFisca, PolicyEngine, or Axiom. The goal is to create exchange/interchange formats and tooling that they could adopt or interoperate with, abstracting policy content, rules, parameters, processes, tests, traces, and semantic metadata from any one engine.

The original attached PDF started from the question of whether OpenFisca and PolicyEngine use open formats that can be moved between projects. The discussion evolved through: parameters and metadata; ontologies; DSLs vs existing standards; AI coding agents changing the ergonomics of verbose open formats; linking rules/settings with processes/workflows; BPMN/DMN and XState/JSON Logic; whether to use an IR; and whether a broader superset over existing ontologies is needed.

ChatGPT's current recommendation is to develop **RaCX - Rules-as-Code Exchange Superset**:

- a canonical JSON-LD policy lifecycle package;
- a federated superset/crosswalk over existing standards and ontologies rather than a replacement ontology;
- support for OpenFisca, PolicyEngine, and Axiom through sidecars/adapters rather than replacement;
- typed coupling between rules, evidence, process, decisions, notices, review, implementation burden, and evaluation;
- deterministic conformance testing, traces, versioning, and no runtime LLM execution for actual policy decisions;
- AI used for migration, annotation, code generation, adapter generation, semantic review, test generation, and redesign.

## Files to read first

1. `README_PACKAGE.md`
2. `views/00_conductor_context.md`
3. `views/01_assistant_current_view.md`
4. `views/02_red_team_on_assistant_and_user.md`
5. `project_repo_racx/README.md`
6. `project_repo_racx/docs/architecture.md`
7. `project_repo_racx/docs/specification/racx-core-v0.1.md`
8. `project_repo_racx/docs/adoption/openfisca-policyengine-axiom.md`
9. `source_material/original_google_search_extracted_text.txt`
10. `conversation/visible_prompts_and_outputs.md`

## Your tasks

Please produce a rigorous, independent review. I want you to be constructively skeptical, not merely agreeable.

### 1. Executive judgement

Give a clear verdict on whether RaCX, as currently conceived, is useful, overcomplicated, underspecified, or strategically promising. Say what you would keep, drop, or reframe.

### 2. Architecture review

Evaluate the core architectural choice: using a canonical JSON-LD policy lifecycle package as the exchange model, with profiles and mappings to OpenFisca, PolicyEngine, Axiom, DMN, BPMN, CMMN, JSON Logic, XState, LegalDocML, LegalRuleML, SHACL, OWL, SKOS, PROV-O, QUDT, JSON Schema, and OpenAPI.

Would you instead choose:

- a separate IR;
- one of the existing standards as canonical;
- an Axiom-native canonical format;
- a DMN/BPMN-first architecture;
- a JSON Logic/XState-first architecture;
- a sidecar-only standard;
- a conformance-test-only standard;
- something else entirely?

### 3. Rules/process coupling

Critically assess Dylan's claim that rules and process are more related than many people claim, and that bringing them closer would improve policy implementation, evaluation, and development.

Please distinguish:

- legal entitlement logic;
- administrative process;
- evidence and verification;
- human discretion and case management;
- notices and review rights;
- operational/service design;
- fiscal and distributional evaluation;
- administrative burden evaluation.

Where should these be coupled? Where must they stay separated?

### 4. OpenFisca / PolicyEngine / Axiom adoption

Assess whether this proposal supports or burdens OpenFisca, PolicyEngine, and Axiom. Suggest an adoption ladder that starts with low-friction metadata, parameter, test, and trace exchange before attempting formula or process exchange.

### 5. Superset over ontologies

Dylan's point is that a superset is needed over all existing ontologies and standards. Evaluate whether that is right. If yes, define the minimum viable superset. If no, suggest a better framing.

### 6. AI and technical debt

PolicyEngine/Axiom's point is that AI enables rapid redesign to remove old technical debt. Evaluate this claim in the context of interchange/exchange. Where does AI genuinely reduce cost? Where can it create new debt or false confidence?

### 7. Red-team review

Red-team both:

- ChatGPT's interpretation and advice;
- Dylan's suggestions and assumptions.

Include failure modes, adoption risks, legal/semantic risks, technical risks, governance risks, and risks from overfitting to one ecosystem.

### 8. Repo/spec review

Review the conceived repo under `project_repo_racx/`. Identify gaps in schemas, examples, tests, governance, conformance profiles, developer ergonomics, and implementation sequencing.

### 9. Alternative design

Propose your own preferred design. It may be a modification of RaCX or a different architecture. Provide a concrete MVP, repo shape, and first 90-day roadmap.

### 10. Output format

Please structure your response as:

1. Executive summary
2. Where you agree
3. Where you disagree
4. Biggest risks
5. Recommended architecture
6. MVP design
7. Adoption path for OpenFisca/PolicyEngine/Axiom
8. Ontology/superset strategy
9. AI usage strategy
10. Specific repo/spec edits
11. Questions for Dylan
12. Final verdict

Please be precise and practical. Do not assume the project is trying to replace OpenFisca or PolicyEngine. Do not assume runtime AI will make legal decisions. Treat the project as an exchange, conformance, and policy-lifecycle interoperability layer.
