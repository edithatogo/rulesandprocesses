# RaCX / Policy Exchange Review Pack for Claude Fable 5

This zip is a self-contained review pack for a second-opinion review of the evolving Rules-as-Code exchange/interoperability proposal discussed by Dylan and ChatGPT.

## What is included

- `source_material/original_google_search.pdf` - the original attached PDF conversation that seeded the idea.
- `source_material/original_google_search_extracted_text.txt` - convenience text extraction from the PDF.
- `source_material/original_google_search_prompt_sequence.md` - the original Google/AI Mode prompt sequence reconstructed from the PDF.
- `conversation/` - visible prompts and ChatGPT outputs from the current conversation. Hidden system/developer prompts and private chain-of-thought are not included.
- `views/` - ChatGPT's current view, red-team critique, design decisions, MoSCoW requirements, and open questions for Fable.
- `project_repo_racx/` - a conceived repository skeleton for RaCX: a Rules-as-Code Exchange Superset / policy lifecycle graph package.
- `covering_prompt_for_fable5.md` - the prompt Dylan can paste into Claude Fable 5 with this zip attached.

## Intended use

Attach this zip to Claude Fable 5 and paste `covering_prompt_for_fable5.md`. The request asks Fable to review the entire proposal, red-team it, compare architectures, and say whether it would approach the interchange/exchange design differently.

## Important framing

RaCX is not intended to replace OpenFisca, PolicyEngine, or Axiom. It is intended to support them by providing exchange formats, semantic IDs, sidecar metadata, tests, traces, process bindings, and conformance profiles that allow tools to interoperate without forcing a single execution engine.

## Transparency note

This pack includes visible conversation content and synthesized views. It does not include hidden model chain-of-thought or private system/developer instructions.
