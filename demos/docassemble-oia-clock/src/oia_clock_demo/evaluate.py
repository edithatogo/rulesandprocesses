"""Pure-Python OIA clock helper for the Docassemble interview demo."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import sys
from typing import Any


def _ensure_foi_o_on_path() -> None:
    # demos/docassemble-oia-clock/src/oia_clock_demo/evaluate.py → repo root
    repo_root = Path(__file__).resolve().parents[4]
    foi_o_src = repo_root / "external" / "foi-o" / "src"
    path = str(foi_o_src)
    if foi_o_src.exists() and path not in sys.path:
        sys.path.insert(0, path)


def evaluate_response_deadline(
    receipt_date: str,
    holiday_dates: list[str] | None = None,
    *,
    invoked_by: str = "docassemble-oia-clock",
) -> dict[str, Any]:
    """Return a JSON-serialisable deadline + trace for a receipt date.

    ``receipt_date`` and ``holiday_dates`` are ISO ``YYYY-MM-DD`` strings.
    """
    _ensure_foi_o_on_path()
    from foi_o_nz.oia_rules import RuleInvocation, ValueObject, evaluate_invocation

    holidays = [date.fromisoformat(h) for h in holiday_dates or []]
    result = evaluate_invocation(
        RuleInvocation(
            decision_id="nz-oia/decision.response_deadline",
            inputs={
                "nz-oia/variable.receipt_date": ValueObject(
                    value=receipt_date,
                    valueState="known",
                ),
            },
            parameter_set="0.1.0",
            invoked_by=invoked_by,
        ),
        holidays=holidays,
    )
    output = result.outputs["nz-oia/decision.response_deadline"]
    trace = dict(result.trace_step)
    trace["adapter"] = "docassemble-oia-clock"
    return {
        "decision_id": "nz-oia/decision.response_deadline",
        "output": {
            "value": output.value,
            "valueState": output.valueState,
        },
        "trace": trace,
        "disclaimer": (
            "Indicative working-day clock only; not legal advice and not a "
            "certified agency decision."
        ),
    }
