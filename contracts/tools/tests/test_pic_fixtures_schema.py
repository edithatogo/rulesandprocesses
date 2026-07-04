from pathlib import Path

from pic_contracts.schema_utils import CONTRACTS_ROOT, load_json, validator_for

BASE = CONTRACTS_ROOT / "pic-fixtures" / "0.1.0" / "examples"


def test_valid_fixtures_validate() -> None:
    validator = validator_for("pic-fixtures")
    for path in sorted((BASE / "valid").glob("*.json")):
        validator.validate(load_json(path))


def test_value_state_only_not_provided_input_is_accepted() -> None:
    validator = validator_for("pic-fixtures")
    doc = load_json(BASE / "valid" / "missingness.json")
    receipt = doc["cases"][0]["inputs"]["nz-oia/variable.receipt_date"]
    assert receipt == {"valueState": "not_provided"}
    validator.validate(doc)


def test_tolerance_is_decimal_string() -> None:
    validator = validator_for("pic-fixtures")
    valid = load_json(BASE / "valid" / "plain.json")
    validator.validate(valid)
    tolerance = valid["cases"][0]["expected"]["us-snap/variable.net_income"]["tolerance"]
    assert tolerance == "1.00"

    invalid_errors = list(validator.iter_errors(load_json(BASE / "invalid" / "bad-tolerance.json")))
    assert invalid_errors
    assert any(Path(*map(str, error.path)).name == "tolerance" for error in invalid_errors)


def test_invalid_fixtures_fail_for_intended_reason() -> None:
    validator = validator_for("pic-fixtures")
    expected: dict[str, tuple[Path, str]] = {
        "float-money.json": (
            Path("cases/0/inputs/us-snap/variable.gross_income/value"),
            "not valid",
        ),
        "missing-curator.json": (Path("provenance"), "is a required property"),
    }
    for filename, (error_path, message) in expected.items():
        errors = list(validator.iter_errors(load_json(BASE / "invalid" / filename)))
        assert errors
        assert any(Path(*map(str, error.path)) == error_path for error in errors)
        assert any(message in error.message for error in errors)
