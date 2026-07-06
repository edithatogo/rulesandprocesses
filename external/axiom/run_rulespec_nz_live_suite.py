from __future__ import annotations

import argparse
import json
from pathlib import Path

from axiom import (
    build_rulespec_nz_acc_earners_levy_adapter,
    build_rulespec_nz_gst_adapter,
    build_rulespec_nz_individual_income_tax_adapter,
    build_rulespec_nz_new_zealand_superannuation_core_adapter,
    build_rulespec_nz_new_zealand_superannuation_special_rates_adapter,
    write_reports,
)
from axiom.runner import AxiomCompiledArtifactExecutor, AxiomHarnessRunner


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the rulespec-nz Axiom live suite.")
    parser.add_argument(
        "--engine-binary",
        default=".external-repos/axiom-rules-engine/target/debug/axiom-rules-engine",
    )
    parser.add_argument("--gst-artifact", default="/tmp/rulespec-nz-gst.compiled.json")
    parser.add_argument(
        "--acc-artifact",
        default="/tmp/rulespec-nz-acc-earners-levy.compiled.json",
    )
    parser.add_argument(
        "--income-tax-artifact",
        default="/tmp/rulespec-nz-individual-income-tax.compiled.json",
    )
    parser.add_argument(
        "--super-core-artifact",
        default="/tmp/rulespec-nz-new-zealand-superannuation-core.compiled.json",
    )
    parser.add_argument(
        "--super-special-rates-artifact",
        default="/tmp/rulespec-nz-new-zealand-superannuation-special-rates.compiled.json",
    )
    parser.add_argument(
        "--output-dir",
        default="external/axiom/results/rulespec-nz-live-suite",
    )
    args = parser.parse_args()

    acc_above_cap_case = {
        "caseId": "nz-acc/fixture.standard_2026_earnings_above_cap",
        "description": "ACC earners levy standard 2026 earnings above cap.",
        "period": "2026-04-01/2027-03-31",
        "entities": {"person": {"type": "Person", "id": "person:1"}},
        "inputs": {
            "nz-acc/variable.acc_earnings_for_earners_levy": {
                "value": "200000",
                "valueState": "known",
                "currency": "NZD",
            }
        },
        "expected": {
            "nz-acc/decision.acc_standard_earners_levy_excluding_gst": {
                "value": "2380.9432",
                "valueState": "known",
                "currency": "NZD",
            },
            "nz-acc/decision.acc_standard_earners_levy_including_gst": {
                "value": "2741.22",
                "valueState": "known",
                "currency": "NZD",
            },
        },
        "sourceRefs": [
            "https://github.com/TheAxiomFoundation/rulespec-nz/blob/3c6436b2ecf82dd7a7f7810a406a2695a64af33a/nz/regulations/acc/earners_levy.test.yaml"
        ],
    }

    runs = [
        (
            build_rulespec_nz_gst_adapter(),
            args.gst_artifact,
            Path("external/axiom/fixtures/rulespec-nz-gst-smoke.pic-fixtures.json"),
        ),
        (
            build_rulespec_nz_acc_earners_levy_adapter(),
            args.acc_artifact,
            Path("external/axiom/fixtures/rulespec-nz-acc-earners-levy-smoke.pic-fixtures.json"),
        ),
        (
            build_rulespec_nz_individual_income_tax_adapter(),
            args.income_tax_artifact,
            Path("external/axiom/fixtures/rulespec-nz-individual-income-tax-smoke.pic-fixtures.json"),
        ),
        (
            build_rulespec_nz_new_zealand_superannuation_core_adapter(),
            args.super_core_artifact,
            Path(
                "external/axiom/fixtures/"
                "rulespec-nz-new-zealand-superannuation-core-source.pic-fixtures.json"
            ),
        ),
        (
            build_rulespec_nz_new_zealand_superannuation_special_rates_adapter(),
            args.super_special_rates_artifact,
            Path(
                "external/axiom/fixtures/"
                "rulespec-nz-new-zealand-superannuation-special-rates-source.pic-fixtures.json"
            ),
        ),
    ]
    results = []
    for adapter, artifact, fixtures_path in runs:
        runner = AxiomHarnessRunner(
            adapter=adapter,
            executor=AxiomCompiledArtifactExecutor(
                binary_path=args.engine_binary,
                artifact_path=artifact,
            ),
        )
        fixture_document = json.loads(fixtures_path.read_text(encoding="utf-8"))
        results.extend(runner.run_fixture_document(fixture_document))

    acc_runner = AxiomHarnessRunner(
        adapter=build_rulespec_nz_acc_earners_levy_adapter(),
        executor=AxiomCompiledArtifactExecutor(
            binary_path=args.engine_binary,
            artifact_path=args.acc_artifact,
        ),
    )
    results.append(acc_runner.run_case(acc_above_cap_case))

    write_reports(results, args.output_dir)
    failed = [result for result in results if result["status"] != "exact_match"]
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
