"""Materialise RuleSpec-side results from companion-test oracles in the inventory."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

from nz_reconciliation.comparison import write_jsonl
from nz_reconciliation.inventory import DEFAULT_INVENTORY, load_inventory, select_cases

DEFAULT_OUTPUT = Path("studies/nz-reconciliation/results/rulespec-candidate-results.jsonl")


def _money_string(value: Any) -> str | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None
    text = format(number, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def materialise_rulespec_result(case: dict[str, Any]) -> dict[str, Any]:
    """Turn one inventory case into a RuleSpec result row.

    Companion-test `expectedRulespec` outputs are the oracle for this phase.
    Live engine execution is optional later; KiwiSaver remains compile-blocked.
    """
    rulespec = case.get("rulespec") or {}
    compile_status = rulespec.get("compileStatus", "ok")
    expected = case.get("expectedRulespec") or {}
    outputs: dict[str, Any] = {}
    for key, raw in expected.items():
        short = key.rsplit("#", 1)[-1]
        money = _money_string(raw)
        if money is not None and not isinstance(raw, bool):
            outputs[short] = {
                "value": money,
                "valueState": "known",
                "currency": "NZD" if abs(Decimal(money)) >= 1 or money == "0" else None,
            }
            if outputs[short]["currency"] is None and "." in money and Decimal(money) < 1:
                # rates stay dimensionless
                del outputs[short]["currency"]
        else:
            outputs[short] = {"value": raw, "valueState": "known"}

    status = "ok" if compile_status == "ok" else "compile_blocked"
    return {
        "caseId": case["caseId"],
        "domain": case.get("domain"),
        "engine": "rulespec-nz",
        "status": status,
        "compileStatus": compile_status,
        "method": "companion-oracle",
        "period": case.get("period"),
        "outputs": outputs,
        "sourceRefs": case.get("sourceRefs") or [],
        "notes": (
            "Companion-test expected outputs materialised as oracle."
            if status == "ok"
            else "RuleSpec module compile blocked (see TheAxiomFoundation/rulespec-nz#79)."
        ),
    }


def run_rulespec_suite(
    inventory_path: Path | None = None,
    *,
    include_blocked: bool = True,
) -> list[dict[str, Any]]:
    inventory = load_inventory(inventory_path or DEFAULT_INVENTORY)
    cases = select_cases(inventory, include_blocked=include_blocked)
    return [materialise_rulespec_result(case) for case in cases]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Materialise RuleSpec NZ reconciliation results.")
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--exclude-blocked", action="store_true")
    args = parser.parse_args(argv)

    rows = run_rulespec_suite(args.inventory, include_blocked=not args.exclude_blocked)
    write_jsonl(args.output, rows)
    ok = sum(1 for row in rows if row["status"] == "ok")
    print(
        json.dumps(
            {
                "ok": True,
                "cases": len(rows),
                "oracle_ok": ok,
                "compile_blocked": len(rows) - ok,
                "output": str(args.output),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
