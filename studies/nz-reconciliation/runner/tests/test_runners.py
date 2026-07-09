from __future__ import annotations

from pathlib import Path

from nz_reconciliation.openfisca_runner import probe_openfisca_tree, run_openfisca_suite
from nz_reconciliation.rulespec_runner import run_rulespec_suite
from nz_reconciliation.run_suite import main as run_suite_main

ROOT = Path(__file__).resolve().parents[4]
REPO = ROOT / ".external-repos/openfisca-aotearoa"


def test_rulespec_suite_materialises_seventeen_cases() -> None:
    rows = run_rulespec_suite()
    assert len(rows) == 17
    assert sum(1 for row in rows if row["status"] == "ok") == 14
    assert sum(1 for row in rows if row["status"] == "compile_blocked") == 3
    first = next(row for row in rows if row["domain"] == "income_tax")
    assert first["outputs"]
    assert first["method"] == "companion-oracle"


def test_openfisca_probe_finds_stale_or_partial_tax_surface() -> None:
    if not REPO.exists():
        return
    probe = probe_openfisca_tree(REPO)
    assert probe["rateParameterPath"] is not None
    assert probe["definesScheduleIncomeTaxPayable"] is False
    assert probe["hasEarnersLevyVariables"] is False


def test_openfisca_suite_marks_engine_gaps() -> None:
    if not REPO.exists():
        return
    rows, probe = run_openfisca_suite(repo_root=REPO)
    assert len(rows) == 17
    assert all(row["status"] == "engine_gap" for row in rows)
    assert probe["latestRateInstant"] is not None


def test_run_suite_writes_reports(tmp_path: Path) -> None:
    if not REPO.exists():
        return
    out = tmp_path / "results"
    assert run_suite_main(["--results-dir", str(out)]) == 0
    assert (out / "DIVERGENCE_REPORT.md").exists()
    assert (out / "comparison-candidate-results.jsonl").exists()
    assert (out / "rulespec-candidate-results.jsonl").exists()
