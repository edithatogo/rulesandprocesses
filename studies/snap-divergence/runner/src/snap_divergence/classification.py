"""Source-level classification for candidate SNAP divergences."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from snap_divergence.comparison import load_jsonl

DEFAULT_COMPARISON_RESULTS = Path("studies/snap-divergence/results/comparison-candidate-results.jsonl")
DEFAULT_CLASSIFIED_RESULTS = Path("studies/snap-divergence/results/classified-candidate-divergences.jsonl")
DEFAULT_REPORT = Path("studies/snap-divergence/DIVERGENCE_CLASSIFICATION.md")

EVIDENCE_REFS = [
    "studies/snap-divergence/SCOPE.md",
    "studies/snap-divergence/PE_NOTES.md",
    "studies/snap-divergence/PRD_NOTES.md",
    "studies/snap-divergence/results/comparison-candidate-results.jsonl",
]

SOURCE_REFS = {
    "prd_snap_function": "https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/functions/benefits_functions.R#L579-L708",
    "prd_parameter_blob": "https://github.com/Research-Division/policy-rules-database/blob/1d8e8674563a7653ec707d18956faa14b016bc5b/prd_parameters/benefit.parameters.rdata",
    "pe_snap_eligibility": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/is_snap_eligible.py#L16-L36",
    "pe_categorical_eligibility": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/eligibility/meets_snap_categorical_eligibility.py#L12-L17",
    "pe_tanf_non_cash": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/is_tanf_non_cash_eligible.py#L11-L15",
    "pe_tanf_gross": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_gross_income_test.py#L11-L34",
    "pe_tanf_asset": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_asset_test.py#L11-L29",
    "pe_tanf_net": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/hhs/tanf/non_cash/meets_tanf_non_cash_net_income_test.py#L11-L24",
    "pe_gross_parameters": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/income_limit/gross.yaml#L29-L117",
    "pe_asset_parameters": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/hhs/tanf/non_cash/asset_limit.yaml#L32-L103",
    "pe_utility_type": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/income/deductions/shelter/snap_utility_allowance_type.py#L20-L39",
    "pe_always_sua": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/usda/snap/income/deductions/utility/always_standard.yaml#L23-L94",
    "pe_phone_allowance": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/parameters/gov/usda/snap/income/deductions/utility/single/phone.yaml#L358-L368",
    "pe_allotment_rounding": "https://github.com/PolicyEngine/policyengine-us/blob/fc64cef64ab55c3c48309c7fb304c35e5f3c9184/policyengine_us/variables/gov/usda/snap/snap_expected_contribution.py#L13-L19",
}


def classify_comparison(comparison: dict[str, Any]) -> dict[str, Any]:
    if comparison.get("agreement"):
        return comparison
    case_id = comparison["caseId"]
    classified = dict(comparison)
    classification, detail, source_refs = _classification_for_case(case_id)
    classified["classification"] = classification
    classified["classificationDetail"] = detail
    classified["investigationStatus"] = "source-level-reviewed"
    classified["sourcePermalinks"] = source_refs
    classified["evidence"] = list(dict.fromkeys(comparison.get("evidence", []) + EVIDENCE_REFS))
    return classified


def classify_all(comparisons: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [classify_comparison(comparison) for comparison in comparisons]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))


def write_classification_report(path: Path, rows: list[dict[str, Any]]) -> None:
    divergent = [row for row in rows if not row.get("agreement")]
    counts: dict[str, int] = {}
    for row in divergent:
        counts[row["classification"]] = counts.get(row["classification"], 0) + 1
    lines = [
        "# SNAP Divergence Source-Level Classification",
        "",
        "This classification is over the 15 held candidate divergences. It is source-level classified, but not a legal adjudication of which engine is correct.",
        "",
        "## Summary",
        "",
        f"- Divergences classified: {len(divergent)}",
        f"- Remaining unclassified divergences: {sum(1 for row in divergent if row['classification'] == 'unclassified')}",
        "",
        "## Counts",
        "",
        "| Classification | Count |",
        "|---|---:|",
    ]
    for classification, count in sorted(counts.items()):
        lines.append(f"| {classification} | {count} |")
    lines.extend(
        [
            "",
            "## Cases",
            "",
            "| Case | Classification | Decision-relevant | Detail |",
            "|---|---|---|---|",
        ],
    )
    for row in divergent:
        lines.append(
            f"| `{row['caseId']}` | {row['classification']} | "
            f"{str(row['decisionRelevant']).lower()} | {row['classificationDetail']} |",
        )
    lines.extend(["", "## Source Evidence", ""])
    for row in divergent:
        lines.append(f"### `{row['caseId']}`")
        lines.append("")
        for ref in row.get("sourcePermalinks", []):
            lines.append(f"- {ref}")
        lines.append("")
    path.write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--comparison", type=Path, default=DEFAULT_COMPARISON_RESULTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_CLASSIFIED_RESULTS)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args(argv)

    classified = classify_all(load_jsonl(args.comparison))
    write_jsonl(args.output, classified)
    write_classification_report(args.report, classified)
    return 0


def _classification_for_case(case_id: str) -> tuple[str, str, list[str]]:
    if "_asset_above_limit" in case_id:
        return (
            "state-option modeling",
            "Asset-test divergence: PRD applies direct SNAP asset-test columns to totalassets in function.snapBenefit, while PolicyEngine routes BBCE through TANF non-cash eligibility and state asset-limit parameters before SNAP categorical eligibility. Legal correctness is not adjudicated here.",
            [
                SOURCE_REFS["prd_snap_function"],
                SOURCE_REFS["prd_parameter_blob"],
                SOURCE_REFS["pe_snap_eligibility"],
                SOURCE_REFS["pe_categorical_eligibility"],
                SOURCE_REFS["pe_tanf_non_cash"],
                SOURCE_REFS["pe_tanf_asset"],
                SOURCE_REFS["pe_asset_parameters"],
            ],
        )
    if case_id.startswith("us-snap/fixture.pa_"):
        return (
            "deduction handling",
            "Pennsylvania Heat-and-Eat/SUA divergence: PRD's snapData has HeatandEatState=Yes and HCSUAValue=778.466, with utility deduction triggered inside function.snapBenefit; PolicyEngine marks PA as always-SUA and uses its utility-allowance parameter table. The observed offset is a deduction/parameter-surface mismatch, not an eligibility flip.",
            [
                SOURCE_REFS["prd_snap_function"],
                SOURCE_REFS["prd_parameter_blob"],
                SOURCE_REFS["pe_utility_type"],
                SOURCE_REFS["pe_always_sua"],
            ],
        )
    if case_id.startswith("us-snap/fixture.tx_"):
        return (
            "state-option modeling",
            "Texas BBCE divergence: PRD encodes BBCE_State=Yes, GrossIncomeEligibilityFPL=1.65, and AssetTest_nonelddis=5000 in snapData and then applies direct gross/asset gates; PolicyEngine encodes the same state-option surface through TANF non-cash gross, net, and asset tests feeding SNAP categorical eligibility. Legal correctness is not adjudicated here.",
            [
                SOURCE_REFS["prd_snap_function"],
                SOURCE_REFS["prd_parameter_blob"],
                SOURCE_REFS["pe_snap_eligibility"],
                SOURCE_REFS["pe_categorical_eligibility"],
                SOURCE_REFS["pe_tanf_non_cash"],
                SOURCE_REFS["pe_tanf_gross"],
                SOURCE_REFS["pe_tanf_net"],
                SOURCE_REFS["pe_tanf_asset"],
                SOURCE_REFS["pe_gross_parameters"],
                SOURCE_REFS["pe_asset_parameters"],
            ],
        )
    if case_id.startswith("us-snap/fixture.ga_"):
        return (
            "state-option modeling",
            "Georgia limited-BBCE divergence: PRD snapData carries BBCE_State=Yes but a 1.30 gross-FPL threshold, while PolicyEngine routes the state option through TANF non-cash categorical eligibility with a 1.30 gross threshold and no TANF non-cash net/asset constraint. Legal correctness is not adjudicated here.",
            [
                SOURCE_REFS["prd_snap_function"],
                SOURCE_REFS["prd_parameter_blob"],
                SOURCE_REFS["pe_snap_eligibility"],
                SOURCE_REFS["pe_categorical_eligibility"],
                SOURCE_REFS["pe_tanf_non_cash"],
                SOURCE_REFS["pe_tanf_gross"],
                SOURCE_REFS["pe_tanf_net"],
                SOURCE_REFS["pe_gross_parameters"],
            ],
        )
    if case_id.startswith("us-snap/fixture.ms_utility"):
        return (
            "deduction handling",
            "Mississippi phone-only utility divergence: PRD applies the SNAP utility deduction through HCSUA/HCSUAValue when utilities are positive and rounds annual snapValue; PolicyEngine chooses between SUA/LUA/IUA from distinct utility bills and uses the Mississippi phone allowance parameter. The remaining difference is non-decision-relevant.",
            [
                SOURCE_REFS["prd_snap_function"],
                SOURCE_REFS["prd_parameter_blob"],
                SOURCE_REFS["pe_utility_type"],
                SOURCE_REFS["pe_always_sua"],
                SOURCE_REFS["pe_phone_allowance"],
                SOURCE_REFS["pe_allotment_rounding"],
            ],
        )
    if case_id.startswith("us-snap/fixture.ms_"):
        return (
            "parameter vintage",
            "Mississippi non-BBCE divergence: PRD snapData has BBCE_State=No, GrossIncomeEligibilityFPL=1.30, finite AssetTest_nonelddis=3000, and non-waived net tests; PolicyEngine represents non-BBCE TANF non-cash eligibility with negative-infinity gross/asset parameters while normal SNAP eligibility uses federal SNAP tests. The result is source-level classified as a parameter-surface/vintage mismatch pending legal adjudication.",
            [
                SOURCE_REFS["prd_snap_function"],
                SOURCE_REFS["prd_parameter_blob"],
                SOURCE_REFS["pe_snap_eligibility"],
                SOURCE_REFS["pe_tanf_gross"],
                SOURCE_REFS["pe_tanf_asset"],
                SOURCE_REFS["pe_gross_parameters"],
                SOURCE_REFS["pe_asset_parameters"],
            ],
        )
    return ("unclassified", "No source-level rule matched this candidate divergence.", [])


if __name__ == "__main__":
    raise SystemExit(main())
