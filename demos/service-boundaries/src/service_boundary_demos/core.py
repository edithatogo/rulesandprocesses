from __future__ import annotations

from datetime import date
from pathlib import Path
import sys
from typing import Any, Mapping

from jsonschema import FormatChecker, validate


DOCASSEMBLE_REQUEST_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "receipt_date": {"type": "string", "format": "date"},
        "holiday_dates": {
            "type": "array",
            "items": {"type": "string", "format": "date"},
            "default": [],
        },
    },
    "required": ["receipt_date"],
}

DOCASSEMBLE_RESPONSE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "decision_id": {"type": "string"},
        "output": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "value": {"type": ["string", "null"]},
                "valueState": {"type": "string"},
            },
            "required": ["value", "valueState"],
        },
        "trace": {
            "type": "object",
            "additionalProperties": True,
            "properties": {
                "adapter": {"type": "string"},
                "stepId": {"type": "string"},
                "kind": {"type": "string"},
                "inputsUsed": {"type": "array", "items": {"type": "string"}},
                "parameterVersions": {"type": "array"},
                "result": {"type": "object"},
                "sourceRefs": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["adapter", "stepId", "kind", "inputsUsed", "parameterVersions", "result", "sourceRefs"],
        },
    },
    "required": ["decision_id", "output", "trace"],
}

CIVIFORM_REQUEST_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "program": {"type": "string"},
        "applicant_id": {"type": "string"},
        "receipt_date": {"type": "string", "format": "date"},
        "holiday_dates": {
            "type": "array",
            "items": {"type": "string", "format": "date"},
            "default": [],
        },
    },
    "required": ["program", "applicant_id", "receipt_date"],
}

CIVIFORM_RESPONSE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "result": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "decision_id": {"type": "string"},
                "output": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "value": {"type": ["string", "null"]},
                        "valueState": {"type": "string"},
                    },
                    "required": ["value", "valueState"],
                },
            },
            "required": ["decision_id", "output"],
        },
        "trace_summary": {
            "type": "object",
            "additionalProperties": True,
            "properties": {
                "adapter": {"type": "string"},
                "stepId": {"type": "string"},
                "kind": {"type": "string"},
                "inputsUsed": {"type": "array", "items": {"type": "string"}},
                "parameterVersions": {"type": "array"},
                "result": {"type": "object"},
                "sourceRefs": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["adapter", "stepId", "kind", "inputsUsed", "parameterVersions", "result", "sourceRefs"],
        },
    },
    "required": ["result", "trace_summary"],
}

_FORMAT_CHECKER = FormatChecker()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def _ensure_foi_o_on_path() -> None:
    foi_o_src = _repo_root() / "external" / "foi-o" / "src"
    path = str(foi_o_src)
    if foi_o_src.exists() and path not in sys.path:
        sys.path.insert(0, path)


def _validate(instance: Mapping[str, Any], schema: dict[str, Any]) -> None:
    validate(instance=dict(instance), schema=schema, format_checker=_FORMAT_CHECKER)


def validate_docassemble_request(request: Mapping[str, Any]) -> None:
    _validate(request, DOCASSEMBLE_REQUEST_SCHEMA)


def validate_civiform_request(request: Mapping[str, Any]) -> None:
    _validate(request, CIVIFORM_REQUEST_SCHEMA)


def _parse_holidays(holiday_dates: list[str] | None) -> list[date]:
    return [date.fromisoformat(holiday) for holiday in holiday_dates or []]


def _load_rule_result(receipt_date: str, holiday_dates: list[str] | None = None):
    _ensure_foi_o_on_path()
    from foi_o_nz.oia_rules import RuleInvocation, ValueObject, evaluate_invocation

    invocation = RuleInvocation(
        decision_id="nz-oia/decision.response_deadline",
        inputs={
            "nz-oia/variable.receipt_date": ValueObject(value=receipt_date, valueState="known"),
        },
        parameter_set="0.1.0",
        invoked_by="service-boundary-demo",
    )
    return evaluate_invocation(invocation, holidays=_parse_holidays(holiday_dates))


def _trace_with_adapter(rule_result, adapter: str) -> dict[str, Any]:
    trace = dict(rule_result.trace_step)
    trace["adapter"] = adapter
    return trace


def render_docassemble_demo(receipt_date: str, holiday_dates: list[str] | None = None) -> dict[str, Any]:
    rule_result = _load_rule_result(receipt_date, holiday_dates)
    output = rule_result.outputs["nz-oia/decision.response_deadline"]
    return {
        "decision_id": "nz-oia/decision.response_deadline",
        "output": {
            "value": output.value,
            "valueState": output.valueState,
        },
        "trace": _trace_with_adapter(rule_result, "docassemble-mock"),
    }


def render_civiform_demo(request: Mapping[str, Any]) -> dict[str, Any]:
    validate_civiform_request(request)
    rule_result = _load_rule_result(
        request["receipt_date"],
        request.get("holiday_dates"),
    )
    output = rule_result.outputs["nz-oia/decision.response_deadline"]
    trace = _trace_with_adapter(rule_result, "civiform-mock")
    return {
        "result": {
            "decision_id": "nz-oia/decision.response_deadline",
            "output": {
                "value": output.value,
                "valueState": output.valueState,
            },
        },
        "trace_summary": trace,
    }
