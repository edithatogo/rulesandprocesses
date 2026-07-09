# NZ reconciliation reports

Canonical Phase 2 divergence report:

→ [`results/DIVERGENCE_REPORT.md`](results/DIVERGENCE_REPORT.md)

Human certification package:

→ [`results/HUMAN_REVIEW.md`](results/HUMAN_REVIEW.md)

Regenerate with:

```bash
PYTHONPATH=studies/nz-reconciliation/runner/src \
  uv run --with pyyaml python -m nz_reconciliation.run_suite
```
