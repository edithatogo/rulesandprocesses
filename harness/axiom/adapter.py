from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from typing import Any, Literal
import decimal

from pydantic import BaseModel, Field

# We reuse the schemas we discovered from axiom-rules-engine
class Interval(BaseModel):
    start: date
    end: date

class ScalarValue(BaseModel):
    kind: Literal["bool", "integer", "decimal", "text", "date"]
    value: bool | int | str

class InputRecord(BaseModel):
    name: str
    entity: str
    entity_id: str
    interval: Interval
    value: ScalarValue

class RelationRecord(BaseModel):
    name: str
    tuple: list[str]
    interval: Interval

class Dataset(BaseModel):
    inputs: list[InputRecord] = Field(default_factory=list)
    relations: list[RelationRecord] = Field(default_factory=list)

class Period(BaseModel):
    period_kind: str
    start: date
    end: date
    name: str | None = None

class ExecutionQuery(BaseModel):
    entity_id: str
    period: Period
    outputs: list[str]
    assessment_date: date | None = None

class Program(BaseModel):
    units: list[dict[str, Any]] = Field(default_factory=list)
    relations: list[dict[str, Any]] = Field(default_factory=list)
    parameters: list[dict[str, Any]] = Field(default_factory=list)
    derived: list[dict[str, Any]] = Field(default_factory=list)

class ExecutionRequest(BaseModel):
    mode: Literal["explain", "fast"]
    program: Program
    dataset: Dataset
    queries: list[ExecutionQuery]

class ScalarOutput(BaseModel):
    kind: Literal["scalar"]
    name: str
    id: str | None = None
    dtype: str
    unit: str | None = None
    value: ScalarValue

class JudgmentOutput(BaseModel):
    kind: Literal["judgment"]
    name: str
    id: str | None = None
    unit: str | None = None
    outcome: Literal["holds", "not_holds", "undetermined"]

class ScalarTraceNode(BaseModel):
    kind: Literal["scalar"]
    name: str
    id: str | None = None
    dtype: str
    unit: str | None = None
    value: ScalarValue
    source: str | None = None
    source_url: str | None = None
    dependencies: list[str] = Field(default_factory=list)

class JudgmentTraceNode(BaseModel):
    kind: Literal["judgment"]
    name: str
    id: str | None = None
    unit: str | None = None
    outcome: Literal["holds", "not_holds", "undetermined"]
    source: str | None = None
    source_url: str | None = None
    dependencies: list[str] = Field(default_factory=list)

class QueryResult(BaseModel):
    entity_id: str
    period: Period
    assessment_date: date | None = None
    outputs: dict[str, ScalarOutput | JudgmentOutput]
    trace: dict[str, ScalarTraceNode | JudgmentTraceNode] = Field(default_factory=dict)

class ExecutionMetadata(BaseModel):
    requested_mode: str
    actual_mode: str
    fallback_reason: str | None = None

class ExecutionResponse(BaseModel):
    metadata: ExecutionMetadata
    results: list[QueryResult]


class AxiomAdapter:
    """Adapts PIC fixtures to/from Axiom Rules Engine format."""

    def __init__(self, program: Program | None = None) -> None:
        self.program = program or Program()

    def parse_period(self, period_str: str) -> Period:
        # Expecting format YYYY-MM
        if len(period_str) == 7 and period_str[4] == "-":
            year = int(period_str[:4])
            month = int(period_str[5:])
            start_date = date(year, month, 1)
            # Find last day of month
            if month == 12:
                end_date = date(year, 12, 31)
            else:
                end_date = date(year, month + 1, 1) - timedelta(days=1)
            return Period(period_kind="Month", start=start_date, end=end_date, name=period_str)
        else:
            # Fallback to annual or direct parsing
            try:
                dt = datetime.strptime(period_str, "%Y")
                return Period(period_kind="Year", start=date(dt.year, 1, 1), end=date(dt.year, 12, 31), name=period_str)
            except ValueError:
                pass
            start_date = date.fromisoformat(period_str)
            return Period(period_kind="Day", start=start_date, end=start_date, name=period_str)

    def convert_pic_value_to_axiom(self, val: Any) -> ScalarValue:
        if isinstance(val, bool):
            return ScalarValue(kind="bool", value=val)
        elif isinstance(val, int):
            return ScalarValue(kind="integer", value=val)
        elif isinstance(val, float) or isinstance(val, decimal.Decimal):
            return ScalarValue(kind="decimal", value=str(val))
        elif isinstance(val, str):
            # Attempt parsing age/integers/floats/booleans
            if val.lower() == "true":
                return ScalarValue(kind="bool", value=True)
            if val.lower() == "false":
                return ScalarValue(kind="bool", value=False)
            try:
                int_val = int(val)
                return ScalarValue(kind="integer", value=int_val)
            except ValueError:
                pass
            try:
                decimal.Decimal(val)
                return ScalarValue(kind="decimal", value=val)
            except (ValueError, decimal.InvalidOperation):
                pass
            return ScalarValue(kind="text", value=val)
        raise ValueError(f"Unsupported python value type for Axiom serialization: {type(val)}")

    def build_execution_request(
        self, pic_case: dict[str, Any], entity_id: str = "household"
    ) -> ExecutionRequest:
        period = self.parse_period(pic_case["period"])
        interval = Interval(start=period.start, end=period.end)

        inputs = []
        for var_name, var_info in pic_case.get("inputs", {}).items():
            axiom_val = self.convert_pic_value_to_axiom(var_info["value"])
            # Remove namespace prefixes from var_name if any (Axiom variables are simple strings)
            clean_name = var_name.split(".")[-1]
            inputs.append(
                InputRecord(
                    name=clean_name,
                    entity=entity_id,
                    entity_id=entity_id,
                    interval=interval,
                    value=axiom_val,
                )
            )

        dataset = Dataset(inputs=inputs)
        
        # Prepare queries for expected outputs
        expected_outputs = [
            var_name.split(".")[-1]
            for var_name in pic_case.get("expected", {}).keys()
        ]
        
        queries = [
            ExecutionQuery(
                entity_id=entity_id,
                period=period,
                outputs=expected_outputs,
            )
        ]

        return ExecutionRequest(
            mode="explain",
            program=self.program,
            dataset=dataset,
            queries=queries,
        )

    def normalize_execution_response(
        self, response: ExecutionResponse, pic_case: dict[str, Any]
    ) -> dict[str, Any]:
        """Normalizes Axiom execution response back to a dictionary of results."""
        results = {}
        for res in response.results:
            for out_name, out_val in res.outputs.items():
                if out_val.kind == "scalar":
                    val = out_val.value.value
                    # Convert to decimal string if decimal kind
                    if out_val.value.kind == "decimal":
                        val = str(val)
                    results[out_name] = val
                elif out_val.kind == "judgment":
                    results[out_name] = out_val.outcome == "holds"
        return results

from datetime import timedelta
