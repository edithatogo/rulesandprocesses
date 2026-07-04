from decimal import Decimal
from racx_validator.expression import evaluate


def test_basic_eligibility_expression():
    expr = {
        "and": [
            {">=": [{"var": "age"}, 18]},
            {"<": [{"var": "adjusted_household_income"}, {"param": "racx:parameter.income_threshold"}]},
        ]
    }
    params = {"racx:parameter.income_threshold": Decimal("40000.00")}
    assert evaluate(expr, {"age": 18, "adjusted_household_income": Decimal("39999.99")}, params) is True
    assert evaluate(expr, {"age": 18, "adjusted_household_income": Decimal("40000.00")}, params) is False
    assert evaluate(expr, {"age": 17, "adjusted_household_income": Decimal("30000.00")}, params) is False
