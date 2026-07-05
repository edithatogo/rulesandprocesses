# Axiom Differential Validation Harness Runbook

Track: `engine_contributions_20260704` Phase 3
Status: Prototype complete

This harness performs differential validation between Axiom-generated models (via `axiom-rules-engine`) and reference implementations like `policyengine-us`.

## Setup

1. **Build the Axiom Rules Engine binary:**
   Ensure the `axiom-rules-engine` Rust binary is compiled and available locally. By default, the harness expects it at:
   ```bash
   target/debug/axiom-rules-engine
   ```

2. **Set up the virtual environment:**
   Ensure `policyengine-us` and the harness dependencies are installed:
   ```bash
   poetry install
   ```

## Running the Harness

To execute the differential validation run over a PIC fixtures package:

```python
from harness.axiom.runner import HarnessRunner
from harness.axiom.report import write_reports

# Initialize the runner pointing to the Axiom rules engine binary
runner = HarnessRunner(axiom_bin="target/debug/axiom-rules-engine")

# Run all cases in the target PIC fixtures corpus
results = runner.run_fixtures_file("studies/snap-divergence/fixtures/snap-fy2026-fixtures.json")

# Write report.md and report.json summaries
write_reports(results, output_dir="outputs/axiom-validation/")
```

## Report Artifacts

The execution will generate:
1. `outputs/axiom-validation/report.md`: Markdown summary classification for human audit.
2. `outputs/axiom-validation/report.json`: Machine-readable results for CI pipelines.
