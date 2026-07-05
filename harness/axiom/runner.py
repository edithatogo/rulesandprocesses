from __future__ import annotations

import json
from pathlib import Path
from typing import Any
import decimal

from harness.axiom.adapter import AxiomAdapter, ExecutionRequest, ExecutionResponse

class HarnessRunner:
    """Runs differential validation comparing Axiom against PolicyEngine-US."""

    def __init__(self, axiom_bin: str | Path = "target/debug/axiom-rules-engine") -> None:
        self.axiom_bin = Path(axiom_bin)
        self.adapter = AxiomAdapter()

    def run_case_differential(self, case: dict[str, Any], engine_stub_callback: Any = None) -> dict[str, Any]:
        case_id = case["caseId"]
        
        # 1. Run Axiom
        axiom_request = self.adapter.build_execution_request(case)
        axiom_results = {}
        axiom_error = None
        
        if engine_stub_callback:
            # Use stub execution for tests
            try:
                response = engine_stub_callback(axiom_request)
                axiom_results = self.adapter.normalize_execution_response(response, case)
            except Exception as e:
                axiom_error = str(e)
        else:
            # Run actual Axiom subprocess (requires binary)
            try:
                from axiom_rules_engine.client import AxiomRulesEngine
                client = AxiomRulesEngine(binary_path=self.axiom_bin)
                response = client.execute(axiom_request)
                axiom_results = self.adapter.normalize_execution_response(response, case)
            except Exception as e:
                axiom_error = str(e)

        # 2. Run PolicyEngine
        pe_results = {}
        pe_error = None
        try:
            from snap_divergence.policyengine_runner import run_policyengine_case
            pe_res = run_policyengine_case(case, include_trace=False)
            for var_name, var_info in pe_res["outputs"].items():
                clean_name = var_name.split(".")[-1]
                pe_results[clean_name] = var_info["value"]
        except Exception as e:
            pe_error = str(e)

        # 3. Compare outputs
        comparison = {}
        all_keys = set(axiom_results.keys()) | set(pe_results.keys())
        
        mismatches = []
        for key in all_keys:
            axiom_val = axiom_results.get(key)
            pe_val = pe_results.get(key)
            match = True
            if axiom_val != pe_val:
                match = False
                mismatches.append(f"{key}: Axiom={axiom_val} != PE={pe_val}")
            comparison[key] = {
                "axiom": axiom_val,
                "policyengine": pe_val,
                "match": match
            }

        status = "exact_match"
        if axiom_error or pe_error:
            status = "adapter_failure"
        elif mismatches:
            status = "output_mismatch"

        return {
            "caseId": case_id,
            "status": status,
            "axiom_error": axiom_error,
            "policyengine_error": pe_error,
            "comparison": comparison,
            "mismatches": mismatches
        }

    def run_fixtures_file(self, fixtures_path: str | Path, engine_stub_callback: Any = None) -> list[dict[str, Any]]:
        with open(fixtures_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        results = []
        for case in data.get("cases", []):
            results.append(self.run_case_differential(case, engine_stub_callback=engine_stub_callback))
        return results
