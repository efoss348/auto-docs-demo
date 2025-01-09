# Installation Guide

## Requirements

- Python 3.8 or higher
- pip package manager

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/efoss348/auto-docs-demo.git
cd auto-docs-demo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Verification

Run the test suite to verify your installation:
```bash
pytest
```

Build the documentation locally:
```bash
mkdocs serve
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the documentation.