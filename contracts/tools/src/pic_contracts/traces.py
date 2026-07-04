"""Trace equivalence helpers."""

from __future__ import annotations

from typing import Any


def _step_path(trace: dict[str, Any]) -> list[tuple[str, tuple[tuple[str, str], ...]]]:
    path = []
    for step in trace.get("steps", []):
        parameter_versions = tuple(
            (item.get("id", ""), item.get("effectiveFrom", ""))
            for item in step.get("parameterVersions", [])
        )
        path.append((step.get("stepId", ""), parameter_versions))
    return path


def _step_sources(trace: dict[str, Any]) -> list[tuple[str, tuple[str, ...]]]:
    return [
        (step.get("stepId", ""), tuple(step.get("sourceRefs", [])))
        for step in trace.get("steps", [])
    ]


def trace_equivalence(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    """Compare two PIC traces at output, path, and semantic levels."""

    diffs: list[dict[str, str]] = []
    output = a.get("outputs", {}) == b.get("outputs", {})
    if not output:
        diffs.append({"level": "output", "message": "outputs differ"})

    a_path = _step_path(a)
    b_path = _step_path(b)
    path = output and a_path == b_path
    if output and not path:
        diffs.append({"level": "path", "message": "step IDs or parameter versions differ"})

    a_sources = _step_sources(a)
    b_sources = _step_sources(b)
    semantic = path and a_sources == b_sources
    if path and not semantic:
        diffs.append({"level": "semantic", "message": "step source references differ"})

    return {"output": output, "path": path, "semantic": semantic, "diffs": diffs}

