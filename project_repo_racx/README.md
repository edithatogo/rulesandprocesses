# RaCX - Rules-as-Code Exchange Superset

RaCX is a proposed policy exchange and conformance package for Rules-as-Code ecosystems. It is designed to support, not replace, OpenFisca, PolicyEngine, Axiom, DMN/BPMN tools, web apps, and evaluation systems.

## Problem

Rules-as-Code projects can share some parameters, APIs, and metadata, but executable policy logic, semantic definitions, tests, traces, and implementation process are difficult to exchange across tools. OpenFisca and PolicyEngine encode much logic in Python. Enterprise systems often use BPMN/DMN. Web apps often use JSON-native formats such as JSON Logic and XState. Legal/document standards such as Akoma Ntoso and LegalRuleML solve only part of the problem.

## Aim

RaCX provides a canonical JSON-LD policy lifecycle package and a set of conformance profiles so that engines can share:

- semantic concepts and variable IDs;
- temporal parameters;
- source references;
- declarative decision/rule subsets;
- evidence requirements;
- process/case bindings;
- tests;
- traces;
- simulation metadata;
- mappings to engine-native objects.

## Non-goals

- Replacing OpenFisca, PolicyEngine, or Axiom.
- Importing/exporting arbitrary Python formulas perfectly.
- Claiming that a computational artifact is the law.
- Runtime LLM decision-making.
- Full coverage of BPMN/DMN/CMMN/LegalRuleML/OWL.

## Core idea

```text
Legal and policy sources
        ↓
RaCX canonical JSON-LD policy lifecycle package
        ↓
Conformance profiles and adapters
        ↓
OpenFisca / PolicyEngine / Axiom / DMN / BPMN / XState / JSON Logic / APIs
```

## Repository structure

```text
docs/                 Architecture and specification notes
schemas/              JSON Schema drafts for RaCX objects
examples/             Example RaCX policy packages
src/racx_validator/   Minimal reference validator/evaluator skeleton
tests/                Example conformance tests
prompts/              AI-assisted migration and review prompts
```

## MVP

The v0.1 MVP is a sidecar-first package for a small tax credit or benefit rule set. It should support stable IDs, variable/parameter export, source references, test fixtures, decision traces, and a simple evidence -> decision -> notice/review process binding.

## Quick start

```bash
python -m pip install -e .
racx-validate examples/basic-income-support/racx.manifest.jsonld
pytest
```

The current code is intentionally a skeleton. The important deliverables are the proposed package shape, profiles, examples, and conformance direction.
