# SNAP Divergence Final Report

This report summarizes the completed Track 5 SNAP differential study. The 50 promoted golden fixtures were human-approved agreement cases. The 15 held candidate divergences were source-level classified, passed through deterministic source triangulation, and then human-adjudicated on 2026-07-06. The final adjudication found expected modeling scope or adapter differences, not code-level bugs in either engine.

## Summary

| Metric | Value |
|---|---:|
| Candidate cases executed | 65 |
| Human-approved golden agreement cases | 50 |
| Held divergences classified | 15 |
| Decision-relevant divergences | 14 |
| Non-decision-relevant divergences | 1 |
| Unclassified divergences | 0 |
| Confirmed code-level bugs | 0 |

## Classification Counts

| Classification | Count |
|---|---:|
| state-option modeling | 8 |
| deduction handling | 4 |
| parameter vintage | 3 |

## Final Adjudication

Human adjudication is controlling for publication and upstream-issue decisions. All 15 held divergences were adjudicated as expected modeling scope or adapter differences; no upstream issue drafts were required.

The deterministic triangulation resolver remains useful evidence for reducing human review. Its pre-human labels and exception queue are preserved in `studies/snap-divergence/TRIANGULATED_ADJUDICATION_PACKET.md`, but those proposed labels are not the final bug finding.

## Divergences

| Case | PolicyEngine allotment | PRD allotment | Difference | Decision-relevant | Classification |
|---|---:|---:|---:|---|---|
| `us-snap/fixture.ga_bbce_165_boundary` | 142.0999755859375 | 0 | 142.0999755859375 | true | state-option modeling |
| `us-snap/fixture.ga_gross_130_above` | 304.0999755859375 | 0 | 304.0999755859375 | true | state-option modeling |
| `us-snap/fixture.ga_gross_130_below` | 376.0999755859375 | 298.4167 | 77.6832755859375 | true | state-option modeling |
| `us-snap/fixture.ms_asset_above_limit` | 546 | 0 | 546 | true | state-option modeling |
| `us-snap/fixture.ms_bbce_165_boundary` | 142.0999755859375 | 0 | 142.0999755859375 | true | parameter vintage |
| `us-snap/fixture.ms_gross_130_above` | 304.0999755859375 | 0 | 304.0999755859375 | true | parameter vintage |
| `us-snap/fixture.ms_gross_130_below` | 376.0999755859375 | 269.5 | 106.5999755859375 | true | parameter vintage |
| `us-snap/fixture.ms_utility_allowance_phone_only` | 295.8999938964844 | 292.5 | 3.3999938964844 | false | deduction handling |
| `us-snap/fixture.pa_bbce_165_boundary` | 142.0999755859375 | 176.5833 | 34.4833244140625 | true | deduction handling |
| `us-snap/fixture.pa_gross_130_above` | 304.0999755859375 | 338.5833 | 34.4833244140625 | true | deduction handling |
| `us-snap/fixture.pa_gross_130_below` | 376.0999755859375 | 410.5833 | 34.4833244140625 | true | deduction handling |
| `us-snap/fixture.tx_asset_above_limit` | 546 | 0 | 546 | true | state-option modeling |
| `us-snap/fixture.tx_bbce_165_boundary` | 142.0999755859375 | 76.75 | 65.3499755859375 | true | state-option modeling |
| `us-snap/fixture.tx_gross_130_above` | 304.0999755859375 | 238.75 | 65.3499755859375 | true | state-option modeling |
| `us-snap/fixture.tx_gross_130_below` | 376.0999755859375 | 310.75 | 65.3499755859375 | true | state-option modeling |

## Evidence

- Human-approved fixture set: `studies/snap-divergence/fixtures/snap-fy2026-fixtures.json`
- Approved-fixture comparison rows: `studies/snap-divergence/results/comparison-approved-results.jsonl`
- Candidate comparison rows: `studies/snap-divergence/results/comparison-candidate-results.jsonl`
- Source-level classified rows: `studies/snap-divergence/results/classified-candidate-divergences.jsonl`
- Triangulated rows: `studies/snap-divergence/results/triangulated-candidate-divergences.jsonl`
- Classification narrative and permalinks: `studies/snap-divergence/DIVERGENCE_CLASSIFICATION.md`
- Triangulation packet: `studies/snap-divergence/TRIANGULATED_ADJUDICATION_PACKET.md`
- Human adjudication packet: `studies/snap-divergence/HUMAN_ADJUDICATION_PACKET.md`
