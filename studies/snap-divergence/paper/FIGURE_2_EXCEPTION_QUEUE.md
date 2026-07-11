# Figure 2. Exception-queue reporting table

The committed triangulated JSONL is the source of truth. The table below defines the reporting categories without converting proposed dispositions into universal bug claims.

| Queue state | Meaning | Publication treatment |
|---|---|---|
| `confirmed_bug_policyengine` / `confirmed_bug_prd` | Controlling primary/official source assertions support the proposed engine-specific disposition | Report with source links and human certification boundary |
| `expected_modeling_difference` | Both implementations are internally coherent but model different pathways or surfaces | Report as non-bug divergence |
| `fixture_adapter_issue` | The comparison input or adapter is underspecified or wrong | Repair fixture/adapter before promotion |
| `needs_more_source_review` | Blocked, conflicting, stale, or secondary-only evidence | Keep out of confirmed conclusions |
