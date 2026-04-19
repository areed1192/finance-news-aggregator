---
name: test-coverage-review
description: >
  Audit, plan, write, and verify unit tests for Python projects using pytest. Use this skill
  whenever someone asks to review test coverage, write tests, add missing tests, check if
  code is properly tested, improve test quality, or ensure new features have tests. Trigger
  on phrases like "write tests for this", "add unit tests", "check my test coverage",
  "review my tests", "are my tests good enough", "this needs tests", "test this module",
  or any request involving pytest, unittest, test files, mocking, fixtures, or code coverage
  in a Python project. Also trigger when someone finishes writing a feature and needs tests
  before the work is considered complete, or when they ask about testing best practices.
---

# Test Coverage Review

This skill audits test coverage in Python projects, identifies gaps, writes new tests,
and verifies that the test suite passes — all following pytest best practices.

## Before you start

Read the best-practices reference file to ground your work:

```
cat references/best-practices.md
```

Use the practices and source citations in that file as your authoritative checklist.

## Modes of operation

Determine the mode from the user's request.

---

### Mode 1 — Audit existing test coverage

Use when the user says "review my tests", "check my coverage", or "are my tests
good enough".

**Step 1: Discover the project structure**

Identify:
- The package name and layout (flat or `src/` layout)
- The test directory (`tests/`, `test/`, or co-located)
- The test framework in use (pytest, unittest, or both)
- Any `conftest.py` files and shared fixtures
- Coverage configuration in `pyproject.toml`, `setup.cfg`, or `.coveragerc`

**Step 2: Map source modules to test files**

For every public module in the package, check whether a corresponding test file
exists. Flag modules with no test file at all.

| Source module       | Test file                | Status  |
|---------------------|--------------------------|---------|
| `mypackage/api.py`  | `tests/test_api.py`      | ✅ exists |
| `mypackage/parser.py` | —                       | ❌ missing |

**Step 3: Audit test quality**

For each existing test file, check against the reference checklist:

1. **Naming** — File named `test_<module>.py`, classes prefixed `Test`,
   methods prefixed `test_`.
2. **Docstrings** — Module-level docstring, class docstring, method docstrings.
3. **Structure** — Tests grouped in classes by the unit under test, with
   section dividers between classes.
4. **Isolation** — No test depends on another test's state or execution order.
5. **Mock boundaries** — External I/O (HTTP, filesystem, database) is mocked.
   Internal methods are tested directly, not mocked.
6. **Fixtures** — Shared setup uses `@pytest.fixture`, not `setUp()` or
   duplicated code.
7. **Sample data** — Test data defined as module-level constants (not buried
   inside fixtures or test methods).
8. **Edge cases** — Empty inputs, invalid inputs, boundary conditions, and
   error paths are tested.
9. **Assertions** — Each test has clear, specific assertions. No tests that
   only check "does not raise".
10. **Coverage** — Every public method/function has at least one test.
    Every branch (if/else, try/except) has coverage.

**Step 4: Run coverage (if possible)**

```bash
pytest tests/ --cov=<package> --cov-report=term-missing --tb=short -q
```

Report:
- Overall coverage percentage
- Specific lines/branches not covered
- Which modules are below the project's coverage threshold

**Step 5: Produce the audit report**

Output a markdown table of findings:

| File | Issue | Severity | Source |
|------|-------|----------|--------|
| `tests/test_api.py` | No tests for error paths in `fetch()` | critical | [PYTEST-GOOD] |
| `tests/test_parser.py` | `_parse()` mocked instead of tested directly | warning | [MOCK-BOUND] |
| — | No test file for `mypackage/utils.py` | critical | [COVERAGE] |

Severity levels:
- **critical** — Public code with no tests, untested error paths, missing
  test files, live API calls in tests.
- **warning** — Missing docstrings, over-mocking, duplicated setup code,
  missing edge cases.
- **info** — Style suggestions, parametrize opportunities, fixture improvements.

---

### Mode 2 — Write tests for new code

Use when the user says "write tests for this", "add tests for this module",
or has just finished a feature.

**Step 1: Analyze the code under test**

Read the module and identify:
- Every public class and its public methods
- Every public function
- Constructor parameters and their types
- Return types and possible exceptions
- External dependencies (HTTP calls, file I/O, database, etc.)
- Edge cases (empty inputs, None values, invalid types, boundary conditions)

**Step 2: Plan test categories**

For each public class or function, plan tests in these categories:

| Category            | What to test                                             |
|---------------------|----------------------------------------------------------|
| **Happy path**      | Normal inputs produce expected outputs                   |
| **Edge cases**      | Empty inputs, None, zero, boundary values                |
| **Error handling**  | Invalid inputs raise expected exceptions                 |
| **Return types**    | Return values have correct types and structure           |
| **Side effects**    | External calls are made with correct arguments           |
| **State changes**   | Object state changes correctly after method calls        |

Present the plan to the user before writing.

**Step 3: Write the test file**

Follow this structure:

```python
"""Tests for <module description>."""

from unittest.mock import patch, MagicMock

import pytest

from <package>.<module> import <Class>, <function>


# ---------------------------------------------------------------------------
# Sample data
# ---------------------------------------------------------------------------

SAMPLE_DATA = ...  # Module-level test data constants


# ---------------------------------------------------------------------------
# <ClassName> tests
# ---------------------------------------------------------------------------


class Test<ClassName>:
    """Tests for the <ClassName> <type>."""

    def test_<behavior>(self):
        """Verify <what is being tested>."""
        # Arrange
        ...
        # Act
        ...
        # Assert
        ...
```

Rules:
- One test file per source module: `test_<module>.py`
- Group related tests in `class Test<Name>:` with class docstrings
- Docstring on every test method: `"""Verify <what>."""`
- Section dividers (`# ---`) between test classes
- Follow Arrange-Act-Assert pattern within each test
- Sample data as module-level constants, not inside tests
- Shared setup in `@pytest.fixture`, not `setUp()`

**Step 4: Mock at the boundary**

Mock external dependencies only:
- `requests.get` / `requests.post` for HTTP calls
- `open` / `pathlib.Path` for file I/O
- Database connections and cursors
- Third-party API clients
- `time.sleep`, `datetime.now` when testing time-dependent logic

Do NOT mock:
- Internal methods of the class under test
- Private helper functions
- Data transformation logic
- Anything that can be tested directly with sample data

```python
# CORRECT — mock the HTTP boundary
@patch("mypackage.api.requests.get")
def test_fetch_sends_timeout(self, mock_get):
    mock_get.return_value = MagicMock(status_code=200, json=lambda: {})
    client = APIClient()
    client.fetch("https://example.com")
    _, kwargs = mock_get.call_args
    assert kwargs["timeout"] == 10

# WRONG — don't mock internal methods
@patch.object(Parser, "_transform")  # ← test this directly instead
def test_parse(self, mock_transform):
    ...
```

**Step 5: Run and verify**

After writing tests:

```bash
# Run the new tests
pytest tests/test_<module>.py -v --tb=short

# Run the full suite to check for regressions
pytest tests/ --tb=short -q

# Check coverage of the new module
pytest tests/ --cov=<package>.<module> --cov-report=term-missing
```

Report the test count and pass/fail status. Note the count for the
changelog entry:
```markdown
- **tests/test_<module>.py**: N unit tests for <description>.
```

---

### Mode 3 — Fill coverage gaps

Use when the user says "improve my coverage", "fill the gaps", or coverage
reports show low percentages.

**Step 1: Identify uncovered code**

Run coverage and parse the `Missing` column to identify:
- Untested functions/methods
- Untested branches (if/else paths, try/except handlers)
- Untested error paths
- Dead code (code that can never be reached — flag for removal)

**Step 2: Prioritize by risk**

Write tests for gaps in this order:
1. **Error handlers** — untested `except` blocks, validation failures
2. **Public API methods** — any public method with zero tests
3. **Branch coverage** — untested `if/else` paths
4. **Edge cases** — boundary conditions in already-tested functions
5. **Private methods** — only if they contain complex logic

**Step 3: Write gap-filling tests**

Add tests to existing test files (don't create new files if a test file
already exists for that module). Follow the same structure and conventions
as the existing tests.

**Step 4: Re-run coverage and report**

Show before/after coverage numbers for the affected modules.

---

## Constraints

- **Always use pytest** unless the project explicitly uses a different framework.
  Do not introduce unittest-style classes (`TestCase`, `self.assertEqual`) into
  a pytest-native project.
- **Never make live API/network calls** — all tests must run offline with mocks.
- **Never modify source code to make it testable** — if something is hard to test,
  note it as a finding but don't refactor the source.
- **One behavior per test** — each test method should verify one specific behavior.
  If a test has many unrelated assertions, split it.
- **Tests must be deterministic** — no random data, no time-dependent assertions,
  no ordering dependencies between tests.
- **Preserve existing tests** — when filling gaps, add to existing test files.
  Do not restructure or rename existing tests unless the user requests it.
