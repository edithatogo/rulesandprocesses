from __future__ import annotations

from decimal import Decimal
from typing import Any, Mapping


def resolve(value: Any, data: Mapping[str, Any], params: Mapping[str, Any]) -> Any:
    if isinstance(value, dict) and "var" in value:
        return data[value["var"]]
    if isinstance(value, dict) and "param" in value:
        return params[value["param"]]
    if isinstance(value, dict) and "decimal" in value:
        return Decimal(value["decimal"])
    return value


def evaluate(expr: Any, data: Mapping[str, Any], params: Mapping[str, Any]) -> Any:
    """Tiny illustrative evaluator for the example expression profile.

    This is not a full RaCX interpreter. It exists only to show what a
    reference interpreter could look like for a constrained profile.
    """
    if not isinstance(expr, dict):
        return expr
    op, args = next(iter(expr.items()))
    if op == "var":
        return data[args]
    if op == "param":
        return params[args]
    if op == "decimal":
        return Decimal(args)
    if op == "and":
        return all(evaluate(a, data, params) for a in args)
    if op == "not":
        return not evaluate(args[0], data, params)
    if op == "if":
        condition, then_value, else_value = args
        return evaluate(then_value, data, params) if evaluate(condition, data, params) else evaluate(else_value, data, params)
    if op in {"<", ">=", ">", "<=", "=="}:
        left = evaluate(args[0], data, params) if isinstance(args[0], dict) else resolve(args[0], data, params)
        right = evaluate(args[1], data, params) if isinstance(args[1], dict) else resolve(args[1], data, params)
        if isinstance(left, str) and left.replace('.', '', 1).isdigit():
            left = Decimal(left)
        if isinstance(right, str) and right.replace('.', '', 1).isdigit():
            right = Decimal(right)
        return {
            "<": left < right,
            ">=": left >= right,
            ">": left > right,
            "<=": left <= right,
            "==": left == right,
        }[op]
    raise ValueError(f"Unsupported operator: {op}")
