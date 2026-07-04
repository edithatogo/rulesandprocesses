from __future__ import annotations

from pathlib import Path

from pic_fixture_converters import corpus_report


def test_build_report_converts_and_summarizes_temp_corpus(tmp_path, monkeypatch) -> None:
    root = tmp_path
    openfisca_dir = root / "converters" / "fixtures" / "corpus" / "openfisca"
    policyengine_dir = root / "converters" / "fixtures" / "corpus" / "policyengine"
    openfisca_dir.mkdir(parents=True)
    policyengine_dir.mkdir(parents=True)
    sample = """
name: Basic
period: 2026
input:
  salary: 1000
output:
  tax: 100
"""
    (openfisca_dir / "basic.yaml").write_text(sample, encoding="utf-8")
    (policyengine_dir / "basic.yaml").write_text(sample, encoding="utf-8")
    validated: list[Path] = []

    def fake_validate(_repo_root: Path, path: Path) -> None:
        validated.append(path)

    monkeypatch.setattr(corpus_report, "_pic_validate", fake_validate)

    report = corpus_report.build_report(root)

    assert "- Total files: 2" in report
    assert "- Converted: 2" in report
    assert "- Clean conversion rate: 100.0%" in report
    assert len(validated) == 2


def test_main_check_detects_stale_report(tmp_path, monkeypatch) -> None:
    output = tmp_path / "REPORT.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("old", encoding="utf-8")
    monkeypatch.setattr(corpus_report, "build_report", lambda _root: "new")

    assert corpus_report.main(["--repo-root", str(tmp_path), "--output", str(output), "--check"]) == 1


def test_main_writes_report(tmp_path, monkeypatch) -> None:
    output = tmp_path / "REPORT.md"
    monkeypatch.setattr(corpus_report, "build_report", lambda _root: "generated")

    assert corpus_report.main(["--repo-root", str(tmp_path), "--output", str(output)]) == 0
    assert output.read_text(encoding="utf-8") == "generated"
