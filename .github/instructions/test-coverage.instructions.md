# Test Coverage

Every new feature, provider, or public method **must** have unit tests before the work is considered complete.

## File Naming

- `tests/test_<module_name>.py` — one test file per logical module.
- If a module is large, split by concern: `tests/test_parser.py`, `tests/test_topics.py`.

## Required Structure

```python
"""Tests for <description>."""

from unittest.mock import patch, MagicMock

import pytest

from finnews.<module> import <Class>


# ---------------------------------------------------------------------------
# Sample data fixtures
# ---------------------------------------------------------------------------

SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <item>
      <title>Sample headline</title>
      <link>https://example.com/article</link>
    </item>
  </channel>
</rss>"""


# ---------------------------------------------------------------------------
# <ClassName> tests
# ---------------------------------------------------------------------------


class Test<ClassName>:
    """Tests for the <ClassName> <type>."""

    def test_<behavior>(self):
        """Verify <what is being tested>."""
        ...
```

## Test Categories

Every new class or public method needs tests in these categories:

### For the parser (`NewsParser`)

| Category          | What to test                                                      |
| ----------------- | ----------------------------------------------------------------- |
| **Parse success** | `_parse_response` returns list of dicts from valid RSS XML        |
| **Field mapping** | `<title>`, `<link>`, `<description>`, `<pubDate>` are extracted   |
| **Namespace**     | XML namespaces are stripped so tags parse cleanly                  |
| **Empty feed**    | A `<channel>` with no `<item>` returns an empty list              |
| **Malformed XML** | Raises `ParseError` on invalid XML                                |
| **HTTP request**  | `_make_request` sends correct URL, params, headers, timeout       |
| **HTTP errors**   | `raise_for_status()` propagates `HTTPError` on 4xx/5xx           |

### For provider clients (CNBC, MarketWatch, etc.)

| Category           | What to test                                                    |
| ------------------ | --------------------------------------------------------------- |
| **Valid topic**    | `_check_key` returns the correct URL for a known topic key      |
| **All topics**     | Passing `"all"` or equivalent returns the full feed dict        |
| **Invalid topic**  | Unknown topic key raises `KeyError`                             |
| **URL format**     | The returned URL contains the expected domain and path          |
| **Feed methods**   | `news_feed()`, `investing_feeds()`, etc. call `_make_request`   |

### For the News client (`client.py`)

| Category           | What to test                                                    |
| ------------------ | --------------------------------------------------------------- |
| **Provider props** | Each `@property` returns the correct provider class instance    |
| **save_to_file**   | File is written with correct JSON content                       |
| **Path traversal** | Filenames containing `..` or `/` are rejected                   |

## Mock Boundaries

Mock at the HTTP boundary to keep tests fast and offline:

```python
# Mock requests.get for parser tests
@patch("finnews.parser.requests.get")
def test_make_request_sends_timeout(self, mock_get):
    mock_get.return_value = MagicMock(status_code=200, content=b"<rss/>")
    parser = NewsParser(...)
    parser._make_request("https://example.com")
    _, kwargs = mock_get.call_args
    assert kwargs["timeout"] == 10

# Mock UserAgent for header tests
@patch("finnews.parser.UserAgent")
def test_user_agent_header(self, mock_ua_class):
    mock_ua_class.return_value.random = "TestAgent/1.0"
    ...
```

Do **not** mock internal methods like `_parse_response` or `_check_key` — test them directly with sample data.

## Rules

1. **Module-level docstring** — one sentence describing what the file tests.
2. **Class-based grouping** — group related tests in `class Test<Name>:` with a class docstring.
3. **Docstring on every test** — `"""Verify <what>."""` on each test method.
4. **Section dividers** — use `# ---` comment blocks between test classes.
5. **Mock at the boundary** — mock `requests.get` or `UserAgent`, not internal methods.
6. **Sample data at module level** — define `SAMPLE_XML` and similar constants as module-level strings, not inside fixtures.
7. **Fixtures use `@pytest.fixture`** — shared setup goes in fixtures, not `setUp()`.
8. **No live API calls** — all tests must run offline with mocked HTTP responses.
9. **Run the full suite** — after writing tests, run `pytest tests/ --tb=short -q` to verify no regressions.
10. **Check coverage** — run `pytest tests/ --cov=finnews --cov-report=term-missing` and confirm new code is covered.

## Running Tests

```bash
# Quick run:
pytest tests/ --tb=short -q

# With coverage:
pytest tests/ --cov=finnews --cov-report=term-missing

# Single file:
pytest tests/test_parser.py -v
```

## Test Count Tracking

When adding tests, note the count in the changelog entry:

```markdown
- **tests/test_parser.py**: 12 unit tests for `NewsParser` parsing and request logic.
```

Run `pytest tests/ --tb=short -q` and confirm the total passes before marking work complete.
