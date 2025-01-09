# Development Guide

## Setting Up Development Environment

1. Fork the repository on GitHub
2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/auto-docs-demo.git
```

3. Set up pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```

## Code Style

We use the following tools to maintain code quality:

- **Black**: Code formatting
  ```bash
  black src tests
  ```

- **isort**: Import sorting
  ```bash
  isort src tests
  ```

- **mypy**: Type checking
  ```bash
  mypy src
  ```

## Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=src

# Run specific test file
pytest tests/test_calculator.py

# Run tests matching specific pattern
pytest -k "add"
```

## Building Documentation

```bash
# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Release Process

1. Update version in `setup.py`
2. Update CHANGELOG.md
3. Create a new git tag
4. Push to GitHub
5. Create a GitHub release