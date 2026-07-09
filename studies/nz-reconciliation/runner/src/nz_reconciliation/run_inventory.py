"""Scaffold runner: validate inventory and emit a dry-run plan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from nz_reconciliation.inventory import DEFAULT_INVENTORY, load_inventory, select_cases


def main(argv: list[str] | None = None) -> int:
    """Print inventory summary and optional filtered case list."""
    parser = argparse.ArgumentParser(description="NZ reconciliation inventory runner scaffold.")
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument(
        "--domain",
        action="append",
        dest="domains",
        choices=["income_tax", "acc_earners_levy", "kiwisaver"],
        help="Filter to one or more domains (repeatable).",
    )
    parser.add_argument(
        "--exclude-blocked",
        action="store_true",
        help="Exclude RuleSpec cases currently blocked from compile (e.g. KiwiSaver).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit full selected case list as JSON.",
    )
    args = parser.parse_args(argv)

    inventory = load_inventory(args.inventory)
    domains = set(args.domains) if args.domains else None
    cases = select_cases(
        inventory,
        domains=domains,
        include_blocked=not args.exclude_blocked,
    )
    summary = {
        "inventoryId": inventory.get("inventoryId"),
        "caseCount": len(cases),
        "targetMinCases": inventory.get("targetMinCases"),
        "meetsTarget": len(cases) >= int(inventory.get("targetMinCases") or 15),
        "domains": {
            domain: sum(1 for case in cases if case.get("domain") == domain)
            for domain in ("income_tax", "acc_earners_levy", "kiwisaver")
        },
        "blockedRulespec": [
            case["caseId"]
            for case in cases
            if (case.get("rulespec") or {}).get("compileStatus") != "ok"
        ],
        "openfiscaRepo": inventory.get("openfiscaAotearoaRepo"),
        "pinnedRulespecCommit": inventory.get("pinnedRulespecCommit"),
    }
    if args.json:
        print(json.dumps({"summary": summary, "cases": cases}, indent=2))
    else:
        print(json.dumps(summary, indent=2))
    return 0 if summary["meetsTarget"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
