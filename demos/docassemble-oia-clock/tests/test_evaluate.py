from __future__ import annotations

from oia_clock_demo.evaluate import evaluate_response_deadline


def test_evaluate_response_deadline_matches_service_boundary_example():
    result = evaluate_response_deadline("2026-07-01", ["2026-07-06"])

    assert result["decision_id"] == "nz-oia/decision.response_deadline"
    assert result["output"]["value"] == "2026-07-30"
    assert result["output"]["valueState"] == "known"
    assert result["trace"]["adapter"] == "docassemble-oia-clock"
    assert result["trace"]["stepId"] == "nz-oia/decision.response_deadline"
    assert "OIA 1982 s 15" in result["trace"]["sourceRefs"]
    assert "Indicative" in result["disclaimer"]


def test_evaluate_response_deadline_without_holidays():
    result = evaluate_response_deadline("2026-07-01")

    assert result["output"]["valueState"] == "known"
    assert result["output"]["value"] is not None
    assert result["trace"]["kind"] == "decision"
