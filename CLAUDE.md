# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

deltaGen is a Python tool for reading various file formats (CSV, Parquet, Delta tables) and saving them as Delta tables with configurable partitioning strategies. It includes both a GUI (PyQt6) and CLI interface.

## Tech Stack

- Python 3.13+ with PyQt6 for GUI
- PySpark and delta-spark for data processing (planned)
- setuptools for packaging

## Common Commands

```bash
# Install dependencies
pip install -e .

# Run the GUI
python src/main.py
# or after install:
deltagen-gui

# Run tests
pytest tests/ -v

# Run single test
pytest tests/test_file.py::test_name -v
```

## Architecture

### GUI (`src/`)
- **main.py**: PyQt6 application entry point with `MainWindow`
- **widgets/**: Custom PyQt6 widget classes
- **dialogs/**: Dialog window classes
- **resources/**: QSS stylesheets and assets

### Backend (planned)
- **readers/**: File format readers (CSV, Parquet, Delta)
- **writers/**: Delta table writer with partitioning logic
- **partitioners/**: Partitioning strategy implementations
