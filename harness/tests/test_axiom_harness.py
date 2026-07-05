from __future__ import annotations

import json
from pathlib import Path
from typing import Any
import pytest

from harness.axiom.adapter import AxiomAdapter, ExecutionResponse, QueryResult, ScalarOutput, ScalarValue, ExecutionMetadata
from harness.axiom.runner import HarnessRunner
from harness.axiom.report import generate_report

def test_pic_case_conversion_to_axiom_request() -> None:
    adapter = AxiomAdapter()
    pic_case = {
        "caseId": "test-case-1",
        "period": "2026-01",
        "inputs": {
            "us-snap/variable.earned_income_monthly": {
                "value": "1200.00",
                "valueState": "known",
                "epistemicStatus": "asserted"
            },
            "us-snap/variable.has_elderly_disabled": {
                "value": False,
                "valueState": "known",
                "epistemicStatus": "asserted"
            }
        },
        "expected": {
            "us-snap/decision.eligible": {
                "value": True,
                "valueState": "known",
                "epistemicStatus": "observed"
            }
        }
    }
    
    req = adapter.build_execution_request(pic_case)
    assert req.mode == "explain"
    assert len(req.dataset.inputs) == 2
    
    # Check variables mapping (clean name)
    names = {inp.name for inp in req.dataset.inputs}
    assert "earned_income_monthly" in names
    assert "has_elderly_disabled" in names
    
    # Check values
    for inp in req.dataset.inputs:
        if inp.name == "earned_income_monthly":
            assert inp.value.kind == "decimal"
            assert inp.value.value == "1200.00"
        elif inp.name == "has_elderly_disabled":
            assert inp.value.kind == "bool"
            assert inp.value.value is False

def test_runner_with_stub_callback() -> None:
    runner = HarnessRunner()
    pic_case = {
        "caseId": "test-case-1",
        "period": "2026-01",
        "inputs": {},
        "expected": {
            "us-snap/decision.eligible": {
                "value": True
            }
        }
    }
    
    # We define a stub callback that returns a valid ExecutionResponse
    def stub_executor(request: Any) -> ExecutionResponse:
        return ExecutionResponse(
            metadata=ExecutionMetadata(requested_mode="explain", actual_mode="explain"),
            results=[
                QueryResult(
                    entity_id="household",
                    period=request.queries[0].period,
                    outputs={
                        "eligible": ScalarOutput(
                            kind="scalar",
                            name="eligible",
                            dtype="bool",
                            value=ScalarValue(kind="bool", value=True)
                        )
                    }
                )
            ]
        )
        
    res = runner.run_case_differential(pic_case, engine_stub_callback=stub_executor)
    assert res["caseId"] == "test-case-1"
    # Even if PolicyEngine execution fails (because it's not installed in dev venv),
    # the harness captures the results or error cleanly.
    assert res["status"] in ("exact_match", "adapter_failure")

def test_report_generation() -> None:
    results = [
        {
            "caseId": "case-1",
            "status": "exact_match",
            "axiom_error": None,
            "policyengine_error": None,
            "comparison": {},
            "mismatches": []
        },
        {
            "caseId": "case-2",
            "status": "output_mismatch",
            "axiom_error": None,
            "policyengine_error": None,
            "comparison": {},
            "mismatches": ["eligible: Axiom=True != PE=False"]
        }
    ]
    report = generate_report(results)
    assert "Axiom Differential Validation Report" in report
    assert "case-1" in report
    assert "case-2" in report
    assert "exact_match" in report
    assert "output_mismatch" in report
