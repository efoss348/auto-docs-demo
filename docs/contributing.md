# Contributing Guidelines

## Setting Up Development Environment

1. Clone the repository
2. Create a virtual environment
3. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

## Development Workflow

1. Create a new branch for your feature
2. Make changes and add tests
3. Update documentation if needed
4. Submit a pull request

## Documentation Standards

- Use Google-style docstrings
- Include type hints
- Provide usage examples in docstrings
- Update relevant documentation files

## Code Style

- Follow PEP 8
- Use Black for code formatting
- Use isort for import sorting

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Update test documentation as needed