# Python Testing Best Practices Reference

This file is the authoritative checklist for the test-coverage-review skill.
Every audit finding and test-writing decision should trace back to a practice here.

## Source abbreviations

| Tag              | Source                                                              |
|------------------|---------------------------------------------------------------------|
| [PYTEST-DOCS]    | pytest official documentation (docs.pytest.org)                     |
| [PYTEST-GOOD]    | pytest — Good Integration Practices (docs.pytest.org)               |
| [REAL-PYTHON]    | Real Python — Effective Python Testing with pytest                  |
| [UNITTEST-DOCS]  | Python docs — `unittest` module reference                           |
| [COVERAGE-DOCS]  | Coverage.py documentation (coverage.readthedocs.io)                 |
| [AAA]            | Arrange-Act-Assert pattern (widely cited testing pattern)           |
| [MOCK-BOUND]     | Mock boundaries principle (from testing literature)                 |
| [PEP-8]          | PEP 8 — Style Guide for Python Code                                |

---

## 1. Project Layout & Discovery

### 1.1 Test directory structure
Place tests in a dedicated `tests/` directory at the project root, separate
from application code. This is the most common and recommended layout.

```
project/
├── pyproject.toml
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── api.py
│       └── parser.py
└── tests/
    ├── conftest.py
    ├── test_api.py
    └── test_parser.py
```

Alternative: co-located tests alongside source files. This works for smaller
projects but can make packaging harder.

**Source:** [PYTEST-GOOD] — "Putting tests into an extra directory outside your
actual application code might be useful… often a good idea"

### 1.2 File naming
Test files must start with `test_` or end with `_test.py`. The `test_` prefix
is more common and recommended.

Name test files to mirror source modules: `test_<module_name>.py`. If a module
is large, split by concern: `test_parser_xml.py`, `test_parser_json.py`.

**Anti-patterns to flag:**
- Test files not matching any source module
- Multiple source modules tested in a single test file (becomes unmaintainable)
- Test files without the `test_` prefix (won't be discovered)

**Source:** [PYTEST-DOCS] — "search for `test_*.py` or `*_test.py` files"

### 1.3 conftest.py
Shared fixtures, hooks, and plugins go in `conftest.py`. pytest automatically
discovers and loads `conftest.py` files — no imports needed.

Place `conftest.py` at the level where fixtures need to be shared:
- `tests/conftest.py` — shared across all test files
- `tests/integration/conftest.py` — shared within integration tests only

**Anti-patterns to flag:**
- Duplicated fixture code across multiple test files (move to conftest)
- Importing fixtures manually instead of using conftest auto-discovery

**Source:** [PYTEST-DOCS]

---

## 2. Test Structure & Naming

### 2.1 Class-based grouping
Group related tests in `class Test<ClassName>:` where the class name matches
the unit under test. Classes must NOT have `__init__` methods.

```python
class TestParser:
    """Tests for the Parser class."""

    def test_parse_valid_xml(self):
        """Verify parse returns a list from valid XML."""
        ...

    def test_parse_empty_feed(self):
        """Verify parse returns empty list for feed with no items."""
        ...
```

Use section dividers between test classes for readability:
```python
# ---------------------------------------------------------------------------
# Parser tests
# ---------------------------------------------------------------------------

class TestParser:
    ...

# ---------------------------------------------------------------------------
# Client tests
# ---------------------------------------------------------------------------

class TestClient:
    ...
```

Function-based tests (no class) are also perfectly valid for testing standalone
functions. The key is consistency within a project.

**Source:** [PYTEST-DOCS] — "Test prefixed test classes (without an `__init__` method)"

### 2.2 Naming conventions
- Test functions: `test_<behavior_being_tested>`
- Test classes: `Test<UnitUnderTest>`
- Use descriptive names that explain what is being verified, not how

**Good names:**
```python
def test_parse_returns_list_from_valid_xml(self): ...
def test_fetch_raises_on_404_response(self): ...
def test_save_writes_json_to_file(self): ...
```

**Bad names (flag these):**
```python
def test_1(self): ...           # Meaningless
def test_parser(self): ...      # What about the parser?
def test_it_works(self): ...    # What works?
def testParse(self): ...        # camelCase, not PEP 8
```

**Source:** [PEP-8], [PYTEST-DOCS]

### 2.3 Docstrings
Every test file, class, and method should have a docstring:

- **Module level:** One sentence describing what the file tests.
  `"""Tests for the RSS feed parser."""`
- **Class level:** What unit is being tested.
  `"""Tests for the Parser class."""`
- **Method level:** What specific behavior is verified.
  `"""Verify parse returns empty list when feed has no items."""`

**Why it matters:** Docstrings appear in test output with `pytest -v` and make
failure reports self-explanatory. They also serve as documentation for future
test maintainers.

**Anti-patterns to flag:**
- Test methods with no docstring
- Docstrings that repeat the method name without adding context

**Source:** [PEP-8]

---

## 3. Arrange-Act-Assert (AAA) Pattern

### 3.1 Structure every test as AAA
Every test should follow three distinct phases:

```python
def test_parse_returns_list_from_valid_xml(self):
    """Verify parse returns a list of dicts from valid XML."""
    # Arrange — set up inputs and expected state
    xml = SAMPLE_XML
    parser = Parser()

    # Act — call the method under test
    result = parser.parse(xml)

    # Assert — verify the outcome
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["title"] == "Sample headline"
```

**Why it matters:** AAA makes tests readable at a glance — you can immediately
see what's being set up, what's being called, and what's being checked.

**Anti-patterns to flag:**
- Tests with assertions scattered throughout (interleaving act and assert)
- Tests with no clear separation between setup and action
- Tests that assert on things set up in the arrange phase (testing the test)

**Source:** [AAA]

### 3.2 One behavior per test
Each test method should verify one specific behavior. If a test has multiple
unrelated assertions, split it into separate tests.

**Good:**
```python
def test_parse_extracts_title(self): ...
def test_parse_extracts_link(self): ...
def test_parse_extracts_date(self): ...
```

**Bad (flag this):**
```python
def test_parse(self):
    # Tests title, link, date, description, error handling all in one
    ...
```

Multiple related assertions in one test are fine (e.g., checking several
fields of the same returned object). The rule is about logical behaviors,
not assertion count.

**Source:** [AAA], [REAL-PYTHON]

---

## 4. Test Data & Fixtures

### 4.1 Module-level sample data
Define test data as module-level constants, not inside fixtures or test methods.
This makes data visible, reusable, and easy to understand.

```python
# ---------------------------------------------------------------------------
# Sample data
# ---------------------------------------------------------------------------

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<root>
  <item><title>Test</title></item>
</root>"""

SAMPLE_JSON = {"key": "value", "items": [1, 2, 3]}

EMPTY_RESPONSE = b""
```

**Anti-patterns to flag:**
- Large data blobs defined inside test methods (hard to read, duplicated)
- Test data loaded from external files without justification
- Magic values (unexplained numbers, strings) in assertions

**Source:** [REAL-PYTHON]

### 4.2 Fixtures for shared setup
Use `@pytest.fixture` for setup that multiple tests share. Prefer fixtures
over `setUp()` / `tearDown()` (those are unittest patterns).

```python
@pytest.fixture
def parser():
    """Create a Parser instance with default config."""
    return Parser(timeout=10, retries=3)

@pytest.fixture
def mock_response():
    """Create a mock HTTP response with sample data."""
    response = MagicMock()
    response.status_code = 200
    response.content = SAMPLE_XML.encode()
    return response
```

Fixture scope controls lifetime:
- `scope="function"` (default) — fresh for each test
- `scope="class"` — shared across a test class
- `scope="module"` — shared across a test file
- `scope="session"` — shared across the entire test run

**Anti-patterns to flag:**
- Using `unittest.TestCase.setUp()` in a pytest-native project
- Duplicated setup code across multiple test methods
- Fixtures with side effects that leak between tests

**Source:** [PYTEST-DOCS], [REAL-PYTHON]

### 4.3 Parametrize for multiple inputs
Use `@pytest.mark.parametrize` to test the same behavior with different inputs
instead of writing separate near-identical test functions.

```python
@pytest.mark.parametrize("topic,expected_url", [
    ("markets", "https://example.com/markets"),
    ("tech", "https://example.com/tech"),
    ("world", "https://example.com/world"),
])
def test_get_url_returns_correct_url(self, topic, expected_url):
    """Verify get_url returns the expected URL for each topic."""
    assert client.get_url(topic) == expected_url
```

**When to use:** Three or more inputs testing the same logic path.

**When NOT to use:** Tests that differ in behavior (not just input). Different
behaviors deserve separate named test methods.

**Source:** [PYTEST-DOCS], [REAL-PYTHON]

---

## 5. Mocking

### 5.1 Mock at the boundary
Mock external I/O — the things that make tests slow, flaky, or require
network access:

| Boundary               | What to mock                                  |
|------------------------|-----------------------------------------------|
| **HTTP**               | `requests.get`, `requests.post`, `httpx.get`  |
| **File system**        | `builtins.open`, `pathlib.Path.read_text`     |
| **Database**           | Connection objects, cursors, ORM queries       |
| **Time**               | `time.sleep`, `datetime.now`, `time.time`     |
| **Randomness**         | `random.random`, `uuid.uuid4`                 |
| **Third-party APIs**   | SDK client methods                            |
| **Environment**        | `os.environ`, `os.getenv`                     |

**Source:** [MOCK-BOUND]

### 5.2 Do NOT mock internal logic
Test internal methods, private helpers, and data transformations directly
with sample data. Mocking them hides bugs and tests the mocking framework
instead of the code.

```python
# WRONG — mocking the thing you should be testing
@patch.object(Parser, "_transform_data")
def test_parse(self, mock_transform):
    mock_transform.return_value = [{"title": "test"}]
    result = parser.parse(SAMPLE_XML)
    assert result == [{"title": "test"}]  # This tests nothing

# CORRECT — test _transform_data directly
def test_transform_data_extracts_fields(self):
    result = parser._transform_data(SAMPLE_XML)
    assert result[0]["title"] == "Sample headline"
```

**Anti-patterns to flag:**
- Mocking methods on the class under test
- Mocking pure functions that have no side effects
- Tests where the mock setup is more complex than the code it replaces

**Source:** [MOCK-BOUND]

### 5.3 Patch the right target
When using `@patch`, patch where the object is *used*, not where it's *defined*:

```python
# If api.py does: import requests
# Patch in the module that uses it:
@patch("mypackage.api.requests.get")  # ← correct
def test_fetch(self, mock_get): ...

# NOT where requests is defined:
@patch("requests.get")  # ← wrong, patches it globally
def test_fetch(self, mock_get): ...
```

**Source:** [UNITTEST-DOCS] — "patch() acts as a decorator, class decorator, or
context manager. In all cases you pass the target as a string of the form
'package.module.ClassName'"

### 5.4 Verify mock interactions
When mocking, assert that the mock was called with the expected arguments:

```python
@patch("mypackage.api.requests.get")
def test_fetch_sends_correct_headers(self, mock_get):
    mock_get.return_value = MagicMock(status_code=200)
    client = APIClient()
    client.fetch("https://api.example.com/data")

    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert kwargs["timeout"] == 10
    assert "User-Agent" in kwargs["headers"]
```

**Source:** [UNITTEST-DOCS]

---

## 6. Test Categories

Every public class or function should have tests covering these categories.
Not every category applies to every unit — use judgment.

### 6.1 Happy path
Normal, expected inputs produce correct outputs. This is the minimum
every public method needs.

### 6.2 Edge cases
Boundary conditions and unusual but valid inputs:
- Empty collections (`[]`, `{}`, `""`)
- `None` values (when allowed by the API)
- Zero, negative numbers, very large numbers
- Unicode strings, strings with special characters
- Single-element collections
- Maximum/minimum allowed values

### 6.3 Error handling
Invalid inputs and error conditions:
- Wrong types (string where int expected)
- Out-of-range values
- Missing required arguments
- Expected exceptions are raised with correct types and messages
- HTTP error codes (4xx, 5xx) propagate correctly

```python
def test_parse_raises_on_invalid_xml(self):
    """Verify parse raises ParseError on malformed XML."""
    with pytest.raises(ParseError):
        parser.parse("not valid xml <<<<")
```

### 6.4 Return types and structure
Verify that return values have the expected type and shape:

```python
def test_fetch_returns_list_of_dicts(self):
    """Verify fetch returns a list of dicts with expected keys."""
    result = client.fetch()
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)
    assert all("title" in item for item in result)
```

### 6.5 Side effects
For methods that call external services or modify state, verify the
interaction occurred correctly using mock assertions.

### 6.6 Security / validation
When applicable, test that the code rejects dangerous inputs:
- Path traversal (`../../../etc/passwd`)
- SQL injection patterns
- Oversized inputs
- Malicious encoding

---

## 7. Coverage

### 7.1 Running coverage
```bash
# Basic coverage report
pytest tests/ --cov=<package> --cov-report=term-missing --tb=short -q

# HTML coverage report (for detailed line-by-line view)
pytest tests/ --cov=<package> --cov-report=html

# Coverage for a single module
pytest tests/test_parser.py --cov=<package>.parser --cov-report=term-missing

# Fail if coverage drops below threshold
pytest tests/ --cov=<package> --cov-fail-under=80
```

**Source:** [COVERAGE-DOCS]

### 7.2 What coverage means
- **Line coverage** — which lines of code were executed during tests.
- **Branch coverage** — which branches of conditional logic were taken.
  Enable with `--cov-branch`.
- **Missing lines** — the `term-missing` report shows which specific lines
  have no coverage.

Coverage percentage is a useful signal but not a goal in itself. 100% line
coverage doesn't mean the code is well-tested — you also need meaningful
assertions and edge case coverage.

**Anti-patterns to flag:**
- Tests that execute code but don't assert anything (inflates coverage)
- Excluding large chunks of code from coverage without justification
- Using `# pragma: no cover` to hide untested code

**Source:** [COVERAGE-DOCS]

### 7.3 Coverage targets
Common targets (adjust per project):
- **New code:** 100% line coverage for newly added modules
- **Overall project:** 80%+ is a common baseline
- **Critical paths:** Error handling, validation, security code should be 100%

### 7.4 Tracking test counts
When adding tests, note the count for changelog entries:
```markdown
- **tests/test_parser.py**: 12 unit tests for `Parser` parsing and request logic.
```

Run `pytest tests/ --tb=short -q` and confirm the total passes before
marking work complete.

---

## 8. Test Execution

### 8.1 Standard commands
```bash
# Quick run
pytest tests/ --tb=short -q

# Verbose (shows each test name)
pytest tests/ -v

# Stop on first failure
pytest tests/ -x

# Run a single file
pytest tests/test_parser.py -v

# Run a single class
pytest tests/test_parser.py::TestParser -v

# Run a single test
pytest tests/test_parser.py::TestParser::test_parse_valid_xml -v

# With coverage
pytest tests/ --cov=<package> --cov-report=term-missing
```

### 8.2 Run the full suite after changes
After writing or modifying tests, always run the full test suite to check
for regressions:
```bash
pytest tests/ --tb=short -q
```

This catches unintended interactions between tests (shared state, import
side effects, fixture conflicts).

**Source:** [PYTEST-DOCS]

---

## 9. Anti-Patterns Checklist

### Always flag (critical)
- Public module with no test file
- Public method/function with zero tests
- Tests that make live network/API calls
- Tests that depend on execution order
- `except: pass` in test code (swallowed test errors)
- Tests with no assertions
- Mocking the class under test

### Flag with context (warning)
- Missing docstrings on test methods
- Duplicated setup code (should be a fixture)
- `setUp()` / `tearDown()` in a pytest-native project
- Test data defined inline instead of as module constants
- Over-mocking (mocking more than the boundary)
- Tests that test implementation details rather than behavior

### Note approvingly (good practice)
- `@pytest.fixture` for shared setup
- `@pytest.mark.parametrize` for data-driven tests
- Section dividers between test classes
- Descriptive test names that read like specifications
- `conftest.py` for shared fixtures
- Coverage configured in `pyproject.toml`
- `# Arrange / Act / Assert` comments in complex tests
