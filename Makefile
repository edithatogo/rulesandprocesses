.PHONY: check lint test validate-examples

check: lint test validate-examples

lint:
	cd contracts/tools && uv run --with ruff ruff check .

test:
	cd contracts/tools && uv run --with pytest pytest

validate-examples:
	cd contracts/tools && uv run python -m pic_contracts.validate_examples ../../contracts
