# Makefile for Statistics Toolkit CLI

.PHONY: install test run demo clean help

# Installation
install:
	pip install -r requirements.txt

dev-install:
	pip install -r requirements.txt
	pip install -e .

# Running
run:
	python stats_cli.py

demo:
	python stats_cli.py --demo

# Testing
test:
	python -m pytest tests/ -v

test-basic:
	python tests/test_basic.py

# Data
sample-data:
	cd examples && python create_sample_data.py

# Cleanup
clean:
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	rm -rf build/ dist/ *.egg-info/

# Help
help:
	@echo "Available commands:"
	@echo "  install      - Install dependencies"
	@echo "  dev-install  - Install for development"
	@echo "  run          - Run the CLI tool"
	@echo "  demo         - Run sample data demo"
	@echo "  test         - Run all tests"
	@echo "  test-basic   - Run basic tests"
	@echo "  sample-data  - Generate sample datasets"
	@echo "  clean        - Clean build artifacts"
	@echo "  help         - Show this help"
