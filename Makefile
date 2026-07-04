.PHONY: check lint test validate-examples converter-lint converter-test corpus-report-check harness-lint harness-test

check: lint test validate-examples converter-lint converter-test corpus-report-check harness-lint harness-test

lint:
	cd contracts/tools && uv run --with ruff ruff check .

test:
	cd contracts/tools && uv run --with pytest --with pytest-cov pytest --cov=pic_contracts --cov-report=term-missing

validate-examples:
	cd contracts/tools && uv run python -m pic_contracts.validate_examples ../../contracts

converter-lint:
	uv run --directory converters/fixtures --with ruff ruff check .

converter-test:
	uv run --directory converters/fixtures --with pytest --with pytest-cov pytest --cov=pic_fixture_converters --cov-report=term-missing

corpus-report-check:
	PYTHONPATH=converters/fixtures/src uv run --with PyYAML python -m pic_fixture_converters.corpus_report --check

harness-lint:
	PYTHONPATH=harness:contracts/tools/src uv run --with ruff ruff check harness

harness-test:
	PYTHONPATH=harness:contracts/tools/src uv run --with pytest --with jsonschema pytest harness/tests
