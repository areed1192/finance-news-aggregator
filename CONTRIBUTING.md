# Contributing to Finance News Aggregator

Thank you for your interest in contributing! This guide covers the development setup, testing, and pull request workflow.

---

## Development Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/areed1192/finance-news-aggregator.git
   cd finance-news-aggregator
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\activate      # Windows
   ```

3. **Install the package in editable mode with dev dependencies:**

   ```bash
   pip install -e ".[dev]"
   ```

   This installs `pytest`, `pytest-cov`, `responses`, and `flake8`.

---

## Running Tests

```bash
python -m pytest tests/ -v --cov=finnews --cov-report=term-missing
```

All tests must pass and new code should include tests. Current target: **maintain or increase** coverage.

---

## Linting

### Flake8

```bash
python -m flake8 finnews/ tests/ --max-line-length=127
```

Zero warnings required.

### Pylint

```bash
python -m pylint finnews/ tests/ --max-line-length=127
```

Score must be **10.00/10**. See `.github/instructions/pylint.instructions.md` for inline suppression rules.

---

## Code Style

- **Line length:** 127 characters max.
- **Imports:** Use `from __future__ import annotations` in every module.
- **Docstrings:** Every module, class, and public method must have a docstring.
- **Type hints:** All public method parameters and return types should be annotated.
- **Logging:** Use `logging.debug()` — never `print()` in library code.

---

## Pull Request Guidelines

1. **Branch from `master`** — create a feature branch: `git checkout -b feature/your-feature`.
2. **Keep changes focused** — one logical change per PR.
3. **Add tests** for new features or bug fixes.
4. **Update `CHANGELOG.md`** — add entries under `## [Unreleased]` following [Keep a Changelog](https://keepachangelog.com/) format.
5. **Update sample files** if you add or change a provider method (see `samples/` directory).
6. **Run linters and tests** before pushing — CI will enforce this.
7. **Write a clear PR description** explaining what changed and why.

---

## Adding a New Provider

1. Create `finnews/<provider>.py` with a class following the existing pattern.
2. Add a `@property` accessor in `finnews/client.py`.
3. Add parser paths and namespaces in `finnews/parser.py`.
4. Create `samples/use_<provider>_client.py` with usage examples.
5. Add tests in `tests/`.
6. Update `README.md` with the new provider section.

---

## Reporting Issues

Please open an issue on GitHub with:

- A clear description of the problem or feature request.
- Steps to reproduce (for bugs).
- Expected vs. actual behavior.
- Python version and OS.
