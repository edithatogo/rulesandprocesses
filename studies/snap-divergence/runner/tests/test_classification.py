from __future__ import annotations

from snap_divergence.classification import classify_comparison


def _comparison(case_id: str) -> dict:
    return {
        "caseId": case_id,
        "agreement": False,
        "classification": "unclassified",
        "evidence": [],
    }


def test_classify_asset_case() -> None:
    classified = classify_comparison(_comparison("us-snap/fixture.tx_asset_above_limit"))

    assert classified["classification"] == "state-option modeling"
    assert "asset-test" in classified["classificationDetail"].lower()
    assert classified["investigationStatus"] == "source-level-reviewed"
    assert any("benefits_functions.R" in ref for ref in classified["sourcePermalinks"])
    assert any("meets_tanf_non_cash_asset_test.py" in ref for ref in classified["sourcePermalinks"])


def test_classify_pa_utility_case() -> None:
    classified = classify_comparison(_comparison("us-snap/fixture.pa_gross_130_below"))

    assert classified["classification"] == "deduction handling"
    assert "Heat-and-Eat" in classified["classificationDetail"]
    assert any("snap_utility_allowance_type.py" in ref for ref in classified["sourcePermalinks"])


def test_classify_agreement_is_unchanged() -> None:
    comparison = {"caseId": "us-snap/fixture.ok", "agreement": True, "classification": "agreement"}

    assert classify_comparison(comparison) == comparison
