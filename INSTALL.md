# HUMMBL Prototype - Installation & Quick Start

## Setup Instructions

```bash
# Navigate to project directory
cd /Users/others/Documents/GitHub/hummbl-prototype

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

```bash
# Run all tests with verbose output
pytest tests/test_decomposition.py -v

# Run with coverage
pytest tests/test_decomposition.py -v --cov=transformations

# Run all tests in tests directory
pytest tests/ -v
```

## Running Validation

```bash
# Run the HUMMBL project validation example
python test_hummbl_project.py
```

This will decompose the actual HUMMBL prototype project and display:
- Component breakdown
- Critical path
- Parallelizable work
- Reasoning trace
- Warnings

Score the output 1-10 to determine if the operator is useful enough to proceed.

## Deactivate Environment

```bash
deactivate
```
