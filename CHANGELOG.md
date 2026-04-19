# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- **finnews/article.py**: `NewsArticle` and `NewsFeed` dataclasses for structured responses.
  - `NewsArticle.from_dict()` maps common RSS tags; extra fields stored in `extra` dict.
  - `NewsFeed.from_dicts()` creates a collection from raw dictionaries.
  - Both include `_repr_html_()` for Jupyter notebook rendering.
  - `NewsFeed` supports `len()`, iteration, and indexing.
- **finnews/article.py**: `NewsArticle.to_dict()` and `NewsArticle.to_json()` serialization methods.
- **finnews/article.py**: `NewsFeed.to_json()`, `NewsFeed.to_csv()`, and `NewsFeed.to_dataframe()` serialization methods.
  - `to_dataframe()` requires optional `pandas` dependency: `pip install fin-news[pandas]`.
- **finnews/article.py**: `NewsFeed.filter(since=, until=, max_results=)` for date-range and result-count filtering.
  - Accepts `datetime` objects for `since`/`until`; naive datetimes treated as UTC.
  - Articles with unparseable dates are kept (never silently dropped).
- **finnews/parser.py**: In-memory TTL cache for feed responses.
  - `cache_ttl` parameter on `NewsParser.__init__()` (default 0 = disabled).
  - Module-level `clear_cache()` function to reset the cache.
- **finnews/client.py**: `News(cache_ttl=N)` parameter propagates to all provider parsers.
- **finnews/async_client.py**: Async client using `httpx` for concurrent feed fetching.
  - `AsyncNews` context manager with `fetch()` and `fetch_multiple()` methods.
  - Requires optional `httpx` dependency: `pip install fin-news[async]`.
  - Shares the same TTL cache as the synchronous client.
- **pyproject.toml**: Optional dependency extras `[pandas]` and `[async]`.
- **tests/test_article.py**: 34 tests for `NewsArticle`/`NewsFeed` construction, serialization, and filtering.
- **tests/test_async_client.py**: 2 tests for `AsyncNews` import and context-manager enforcement.
- **samples/use_advanced_features.py**: Sample demonstrating serialization (`to_json`, `to_csv`, `to_dataframe`), filtering (`since`, `until`, `max_results`), TTL caching, and async client.
- **finnews/cnbc.py**, **finnews/market_watch.py**: `topics` property returning sorted list of available topic keys.
- **finnews/cnn_finance.py**, **finnews/nasdaq.py**, **finnews/sp_global.py**, **finnews/seeking_alpha.py**, **finnews/wsj.py**, **finnews/yahoo_finance.py**: `feeds` property returning sorted list of available feed method names.
- **finnews/sp_global.py**: Added `daily_index_insights()` and `case_shiller_home_price_indices()` feed methods (14 feeds total).
- **finnews/\_\_init\_\_.py**: Exports `NewsArticle` and `NewsFeed` in `__all__`.
- **CONTRIBUTING.md**: Developer setup, testing, linting, and PR guidelines.
- **tests/test_exceptions.py**: 4 tests for the custom exception hierarchy.
- **tests/test_deprecations.py**: 5 tests for deprecated method aliases.
- **tests/conftest.py**: Shared fixtures and sample data for the test suite.
- **finnews/exceptions.py**: Custom exception hierarchy — `FinnewsError` (base), `InvalidTopicError`, `FeedRequestError`, `FeedParseError`.
  - `InvalidTopicError` also inherits from `KeyError` for backward compatibility.
- **finnews/py.typed**: PEP 561 marker file for static type checker support.
- **finnews/news_enum.py**: Renamed all enum classes to PascalCase (`CNBCTopNews`, `CNBCInvesting`, `CNBCBlogs`, `CNBCTVVideoAndTV`, `CNBCTVProgramsEurope`, `CNBCTVProgramsAsia`, `MarketWatch`).

### Changed

- **README.md**: Full rewrite with badges, installation, quick-start for all 8 providers, API reference table, structured models docs, enum guide, and comparison with alternatives.
- **samples/use_sp_global_client.py**: Updated to use `all_indices()`, `index_announcements()`, `new_consultations()` instead of deprecated typos.
- **samples/use_nasdaq_client.py**: Updated to use `artificial_intelligence_feed()` instead of deprecated typo.
- **samples/use_cnn_finance.py**: Updated to use `technology()` instead of deprecated typo.
- **samples/**: All 9 sample scripts updated to demonstrate `topics`/`feeds` properties, `NewsArticle`/`NewsFeed` structured models, enum usage, and section dividers.
- All modules: Added module-level docstrings.
- All 8 provider classes: Added `cache_ttl` parameter to `__init__()`, passed through to `NewsParser`.
- **finnews/parser.py**: Renamed `_make_request` → `make_request` and `_parse_response` → `parse_response` (public API).
- **finnews/parser.py**: `make_request` now uses a `requests.Session` with `urllib3.util.Retry` (3 retries, 0.5 s backoff, retries on 429/500/502/503/504).
- **finnews/parser.py**: HTTP errors wrapped in `FeedRequestError`; XML parse errors wrapped in `FeedParseError`.
- **finnews/parser.py**: `parse_response` now collects duplicate XML tags into lists instead of silently overwriting.
- **finnews/parser.py**: Added `from __future__ import annotations` and type hints on public methods.
- **finnews/cnbc.py**: `_check_key` raises `InvalidTopicError` (with valid-topics list) instead of plain `KeyError`.
- **finnews/cnbc.py**: Replaced `print()` calls with `logging.debug()`.
- **finnews/cnbc.py**: Fixed no-else-return in `_check_key`.
- **finnews/market_watch.py**: `_check_key` raises `InvalidTopicError` and accepts `Enum` values via `isinstance` check.
- **finnews/market_watch.py**: Replaced `print()` calls with `logging.debug()`.
- **finnews/market_watch.py**: Fixed no-else-return in `_check_key`.
- **finnews/client.py**: All 8 provider `@property` methods now cache (return same instance on repeated access).
- **finnews/\_\_init\_\_.py**: `__all__` now exports exception classes alongside `News`.
- **finnews/cnn_finance.py**, **finnews/nasdaq.py**, **finnews/sp_global.py**: Moved `import warnings` to module top level.
- All modules: Added `from __future__ import annotations` for modern type-hint syntax.
- All provider modules: Updated calls from `_make_request` to `make_request`.
- **pyproject.toml**: Added `[tool.pylint."messages control"]` disabling `duplicate-code`.
- **tests/**: Reorganized test suite from 6 files to 8 module-aligned files; migrated from `unittest.TestCase` to pytest-native style.
  - Deleted `test_enhancements.py`, `test_phase3.py`, `test_phase4.py`.
  - Merged tests into `test_client.py`, `test_parser.py`, `test_topics.py`, `test_article.py`, `test_exceptions.py`, `test_deprecations.py`, `test_async_client.py`.
  - Extracted shared sample data and fixtures to `conftest.py`.
- **finnews/market_watch.py**: Updated RSS feed URLs to current endpoints (`feeds.content.dowjones.io` for top stories, real-time headlines, and market pulse; `feeds.marketwatch.com` for bulletins). Reduced active feeds from 13 to 4.
- **finnews/fields.py**: Updated `market_watch_rss_feeds_id` to 4 active feed mappings.
- **finnews/news_enum.py**: `MarketWatch` enum reduced from 13 to 4 members matching active feeds.

### Deprecated

- **finnews/cnn_finance.py**: `techonology()` → use `technology()`. Old name emits `DeprecationWarning`.
- **finnews/nasdaq.py**: `artifical_intelligence_feed()` → use `artificial_intelligence_feed()`. Old name emits `DeprecationWarning`.
- **finnews/sp_global.py**: `all_indicies()` → `all_indices()`, `index_announcments()` → `index_announcements()`, `new_counsultations()` → `new_consultations()`. Old names emit `DeprecationWarning`.
- **finnews/market_watch.py**: 9 defunct feed methods now emit `DeprecationWarning` and return `[]`: `personal_finance()`, `stocks_to_watch()`, `internet_stories()`, `mutual_funds()`, `software_stories()`, `banking_and_finance()`, `commentary()`, `newsletter_and_research()`, `auto_reviews()`.

### Fixed

- **finnews/client.py**: Fixed docstring typo `market_Watch` → `market_watch`.
- **finnews/sp_global.py**: Fixed RSS feed name typos in URL parameters: `all-indicies` → `all-indices`, `index-announcments` → `index-news-announcements`, `new-counsultations` → `consultations`.
- **.github/workflows/python-package.yml**: Added `pip install -e .` so the `finnews` package is importable during CI test runs.

## [0.1.3] - 2026-04-19

### Added

- **finnews/\_\_init\_\_.py**: Package init with `__version__` and top-level `News` import.
  - `from finnews import News` now works as a convenience import.
- **pyproject.toml**: PEP 621 project metadata, replacing legacy `setup.py` as the primary config.
  - Includes `[project.optional-dependencies] dev` with pytest, pytest-cov, responses, flake8.
  - Configures `[tool.pytest.ini_options]`, `[tool.coverage.run]`, and `[tool.coverage.report]`.
- **tests/test_parser.py**: 12 unit tests for `NewsParser`.
  - 7 tests for `_parse_response`: basic parsing, field extraction, whitespace stripping, namespace stripping, empty feeds, malformed XML, client path configuration.
  - 5 tests for `_make_request`: successful request, timeout verification, param forwarding, HTTP error propagation, user-agent header.
- **tests/test_topics.py**: 9 unit tests for topic key validation.
  - 4 tests for `CNBC._check_key`: valid topic, all topics, invalid topic, empty string.
  - 5 tests for `MarketWatch._check_key`: valid topic, URL substitution, all topics, invalid topic, empty string.
- **requirements.txt**: Added `defusedxml>=0.7.1` dependency.

### Changed

- **finnews/parser.py**: Replaced `xml.etree.ElementTree` with `defusedxml.ElementTree` to prevent XXE and billion-laughs attacks.
- **finnews/parser.py**: Added `timeout=10` to `requests.get()` in `_make_request` to prevent indefinite hangs.
- **finnews/parser.py**: Added `response.raise_for_status()` before parsing to surface HTTP errors cleanly.
- **finnews/market_watch.py**: Changed base URL from `http://` to `https://`.
- **finnews/cnn_finance.py**: Changed base URLs from `http://` to `https://` (both `url` and `url_buzz`).
- **finnews/client.py**: `save_to_file` now validates `file_name` against path traversal using `pathlib`.
- **.github/workflows/python-package.yml**: Updated Python matrix to 3.10–3.13, actions to v4/v5, switched from unittest to pytest with coverage.
- **.github/workflows/python-publish.yml**: Updated actions to v4/v5, switched from `setup.py sdist` to `python -m build`.

### Fixed

- **finnews/market_watch.py**: Fixed `_check_key` format bug — `topic_id=` → `topic=` so the URL template `{topic}` is actually substituted.
- **tests/test_client.py**: Fixed `market_Watch` → `market_watch` property name in `test_creates_market_watch_instance`.
- **.github/workflows/python-package.yml**: Fixed test filename typo (`test_clients.py` → `test_client.py`) that caused CI to silently skip all tests.

## [0.1.2] - 2020-01-01

Initial public release with support for 8 news providers:
CNBC, NASDAQ, MarketWatch, S&P Global, Seeking Alpha, CNN Finance, Wall Street Journal, Yahoo Finance.
