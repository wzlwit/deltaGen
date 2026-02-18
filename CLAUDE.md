# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

deltaGen is a Python tool for reading various file formats (CSV, Parquet, Delta tables) and saving them as Delta tables with configurable partitioning strategies.

## Tech Stack

- Python with PySpark and delta-spark
- Poetry for dependency management

## Common Commands

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run single test
poetry run pytest tests/test_file.py::test_name -v

# Run the CLI (once implemented)
poetry run deltagen <input_path> <output_path>
```

## Architecture

- **readers/**: File format readers (CSV, Parquet, Delta)
- **writers/**: Delta table writer with partitioning logic
- **partitioners/**: Partitioning strategy implementations
- **cli.py**: Command-line interface entry point
