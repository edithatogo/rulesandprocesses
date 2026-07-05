from __future__ import annotations

import json
from pathlib import Path
from typing import Any

def generate_report(results: list[dict[str, Any]]) -> str:
    """Generates a Markdown report of the differential validation results."""
    lines = []
    lines.append("# Axiom Differential Validation Report")
    lines.append("")
    
    total = len(results)
    exact_matches = sum(1 for r in results if r["status"] == "exact_match")
    mismatches = sum(1 for r in results if r["status"] == "output_mismatch")
    failures = sum(1 for r in results if r["status"] == "adapter_failure")
    
    lines.append("## Summary Statistics")
    lines.append(f"- **Total Cases Run:** {total}")
    lines.append(f"- **Exact Matches:** {exact_matches}")
    lines.append(f"- **Output Mismatches:** {mismatches}")
    lines.append(f"- **Adapter/Runner Failures:** {failures}")
    lines.append("")
    
    lines.append("## Detailed Results")
    lines.append("| Case ID | Status | Mismatches / Errors |")
    lines.append("|---|---|---|")
    
    for r in results:
        case_id = r["caseId"]
        status = r["status"]
        
        detail = ""
        if r["axiom_error"]:
            detail += f"Axiom error: {r['axiom_error']}; "
        if r["policyengine_error"]:
            detail += f"PolicyEngine error: {r['policyengine_error']}; "
        if r["mismatches"]:
            detail += ", ".join(r["mismatches"])
            
        if not detail:
            detail = "None"
            
        lines.append(f"| {case_id} | {status} | {detail} |")
        
    return "\n".join(lines) + "\n"

def write_reports(results: list[dict[str, Any]], output_dir: str | Path) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    # 1. Markdown report
    md_content = generate_report(results)
    (out_path / "report.md").write_text(md_content, encoding="utf-8")
    
    # 2. JSON summary
    summary = {
        "total": len(results),
        "exact_matches": sum(1 for r in results if r["status"] == "exact_match"),
        "mismatches": sum(1 for r in results if r["status"] == "output_mismatch"),
        "failures": sum(1 for r in results if r["status"] == "adapter_failure"),
        "results": results
    }
    (out_path / "report.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
