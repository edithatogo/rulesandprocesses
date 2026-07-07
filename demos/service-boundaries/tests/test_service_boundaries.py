import json
from pathlib import Path

import pytest
from jsonschema import validate

from service_boundary_demos.core import (
    CIVIFORM_REQUEST_SCHEMA,
    CIVIFORM_RESPONSE_SCHEMA,
    DOCASSEMBLE_REQUEST_SCHEMA,
    DOCASSEMBLE_RESPONSE_SCHEMA,
    render_civiform_demo,
    render_docassemble_demo,
    validate_civiform_request,
    validate_docassemble_request,
)


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


@pytest.mark.parametrize(
    "request_path,response_path,request_schema,response_schema,renderer,trace_key,trace_adapter",
    [
        (
            EXAMPLES / "docassemble" / "request.json",
            EXAMPLES / "docassemble" / "response.json",
            DOCASSEMBLE_REQUEST_SCHEMA,
            DOCASSEMBLE_RESPONSE_SCHEMA,
            render_docassemble_demo,
            "trace",
            "docassemble-mock",
        ),
        (
            EXAMPLES / "civiform" / "request.json",
            EXAMPLES / "civiform" / "response.json",
            CIVIFORM_REQUEST_SCHEMA,
            CIVIFORM_RESPONSE_SCHEMA,
            render_civiform_demo,
            "trace_summary",
            "civiform-mock",
        ),
    ],
)
def test_examples_validate_and_render(
    request_path,
    response_path,
    request_schema,
    response_schema,
    renderer,
    trace_key,
    trace_adapter,
):
    request = load_json(request_path)
    expected = load_json(response_path)

    validate(request, request_schema)
    validate(expected, response_schema)

    if renderer is render_docassemble_demo:
        rendered = renderer(request["receipt_date"], request.get("holiday_dates", []))
    else:
        rendered = renderer(request)

    if trace_key == "trace":
        assert rendered["decision_id"] == expected["decision_id"]
        assert rendered["output"] == expected["output"]
    else:
        assert rendered["result"] == expected["result"]

    assert trace_key in rendered
    assert rendered[trace_key]["adapter"] == trace_adapter
    assert rendered[trace_key]["stepId"] == expected[trace_key]["stepId"]
    assert rendered[trace_key]["result"] == expected[trace_key]["result"]


def test_invalid_requests_are_rejected():
    with pytest.raises(Exception):
        validate_docassemble_request({})

    with pytest.raises(Exception):
        validate_civiform_request({"program": "oia-deadline-demo"})
