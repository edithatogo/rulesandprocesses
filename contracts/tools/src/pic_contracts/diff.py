"""Parameter diffing for PIC parameter files."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pic_contracts.schema_utils import load_json


@dataclass(frozen=True)
class ParameterChange:
    kind: str
    parameter_id: str
    detail: str


def _parameters_by_id(doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {parameter["id"]: parameter for parameter in doc.get("parameters", [])}


def _period_key(period: dict[str, Any]) -> tuple[str, str | None]:
    return period.get("from", ""), period.get("to")


def diff_parameters(before: dict[str, Any], after: dict[str, Any]) -> list[ParameterChange]:
    before_params = _parameters_by_id(before)
    after_params = _parameters_by_id(after)
    changes: list[ParameterChange] = []

    for parameter_id in sorted(before_params.keys() - after_params.keys()):
        changes.append(ParameterChange("removed_parameter", parameter_id, "parameter removed"))
    for parameter_id in sorted(after_params.keys() - before_params.keys()):
        changes.append(ParameterChange("new_parameter", parameter_id, "parameter added"))

    for parameter_id in sorted(before_params.keys() & after_params.keys()):
        before_periods = {
            _period_key(period): period for period in before_params[parameter_id]["values"]
        }
        after_periods = {
            _period_key(period): period for period in after_params[parameter_id]["values"]
        }
        for period_key in sorted(before_periods.keys() - after_periods.keys()):
            changes.append(
                ParameterChange(
                    "removed_period",
                    parameter_id,
                    f"period removed: {period_key[0]} to {period_key[1]}",
                )
            )
        for period_key in sorted(after_periods.keys() - before_periods.keys()):
            changes.append(
                ParameterChange(
                    "new_period",
                    parameter_id,
                    f"period added: {period_key[0]} to {period_key[1]}",
                )
            )
        for period_key in sorted(before_periods.keys() & after_periods.keys()):
            before_value = before_periods[period_key].get("value")
            after_value = after_periods[period_key].get("value")
            if before_value != after_value:
                changes.append(
                    ParameterChange(
                        "value_change",
                        parameter_id,
                        f"{period_key[0]} to {period_key[1]}: {before_value!r} -> {after_value!r}",
                    )
                )
    return changes


def changes_to_json(changes: list[ParameterChange]) -> str:
    return json.dumps([change.__dict__ for change in changes], indent=2)


def changes_to_markdown(changes: list[ParameterChange]) -> str:
    if not changes:
        return "# PIC Parameter Diff\n\nNo changes.\n"
    lines = [
        "# PIC Parameter Diff",
        "",
        "| Kind | Parameter | Detail |",
        "|---|---|---|",
    ]
    for change in changes:
        lines.append(f"| `{change.kind}` | `{change.parameter_id}` | {change.detail} |")
    lines.append("")
    return "\n".join(lines)


def diff_files(before_path: Path, after_path: Path) -> list[ParameterChange]:
    return diff_parameters(load_json(before_path), load_json(after_path))
