from pathlib import Path

from pic_contracts.schema_utils import CONTRACTS_ROOT, load_json, validator_for

BASE = CONTRACTS_ROOT / "pic-semantics" / "0.1.0" / "examples"


def test_valid_value_objects_validate() -> None:
    validator = validator_for("pic-semantics")
    for path in sorted((BASE / "valid").glob("*.json")):
        validator.validate(load_json(path))


def test_invalid_value_objects_fail_for_intended_reason() -> None:
    validator = validator_for("pic-semantics")
    expected: dict[str, tuple[Path, str]] = {
        "bad-value-state.json": (Path("valueState"), "not one of"),
        "float-money.json": (Path("value"), "is not valid under any of the given schemas"),
        "lowercase-currency.json": (Path("currency"), "does not match"),
    }
    for filename, (error_path, message) in expected.items():
        errors = sorted(
            validator.iter_errors(load_json(BASE / "invalid" / filename)),
            key=lambda error: list(error.path),
        )
        assert errors, filename
        assert any(Path(*map(str, error.path)) == error_path for error in errors)
        assert any(message in error.message for error in errors)

