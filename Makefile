.PHONY: help install lint type test cov check run docker docker-test clean

help:
	@echo "Targets:"
	@echo "  install     install the package with dev extras"
	@echo "  lint        ruff lint"
	@echo "  type        mypy type check"
	@echo "  test        run the test suite"
	@echo "  cov         run tests with coverage"
	@echo "  check       lint + type + test (what CI runs)"
	@echo "  run         show the harness status banner"
	@echo "  docker      build the runtime image"
	@echo "  docker-test build the test stage (runs tests in-image)"
	@echo "  clean       remove caches and build artifacts"

install:
	pip install -e ".[dev]"

lint:
	ruff check .

type:
	mypy

test:
	pytest -q

cov:
	pytest --cov --cov-report=term-missing

check: lint type test

run:
	python -m harness.interfaces.cli status

docker:
	docker build --target runtime -t cybersecurity-harness:latest .

docker-test:
	docker build --target test -t cybersecurity-harness:test .

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov build dist *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
