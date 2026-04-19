"""Tests for Phase 4 features: serialization, filtering, caching, async client."""

import csv
import io
import json
import time
import unittest
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

from finnews.article import NewsArticle, NewsFeed
from finnews.parser import (
    NewsParser,
    _response_cache,
    clear_cache,
)


# ---------------------------------------------------------------------------
# Sample data
# ---------------------------------------------------------------------------

ARTICLES = [
    {
        "title": "Markets Rally on Fed Decision",
        "link": "https://example.com/1",
        "description": "Stocks climbed after the Fed held rates.",
        "pubDate": "Sat, 19 Apr 2026 14:00:00 +0000",
        "category": "Markets",
    },
    {
        "title": "Tech Earnings Beat Expectations",
        "link": "https://example.com/2",
        "description": "Major tech firms reported strong Q1.",
        "pubDate": "Fri, 18 Apr 2026 09:00:00 +0000",
    },
    {
        "title": "Oil Prices Surge",
        "link": "https://example.com/3",
        "description": "Crude oil hit a 6-month high.",
        "pubDate": "Thu, 17 Apr 2026 06:00:00 +0000",
    },
]


# ---------------------------------------------------------------------------
# NewsArticle serialization tests
# ---------------------------------------------------------------------------


class TestNewsArticleToDict(unittest.TestCase):
    """Tests for NewsArticle.to_dict()."""

    def test_to_dict_includes_standard_fields(self):
        """Verify all standard fields appear in the dict."""

        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        d = article.to_dict()
        self.assertEqual(d["title"], "Markets Rally on Fed Decision")
        self.assertEqual(d["link"], "https://example.com/1")
        self.assertEqual(d["source"], "cnbc")
        self.assertIn("published", d)

    def test_to_dict_merges_extra(self):
        """Verify extra fields are merged into the dict."""

        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        d = article.to_dict()
        self.assertEqual(d["category"], "Markets")

    def test_to_json_returns_valid_json(self):
        """Verify to_json produces valid JSON."""

        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        result = article.to_json()
        parsed = json.loads(result)
        self.assertEqual(parsed["title"], "Markets Rally on Fed Decision")

    def test_to_json_passes_kwargs(self):
        """Verify kwargs are forwarded to json.dumps."""

        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        result = article.to_json(indent=2)
        self.assertIn("\n", result)


# ---------------------------------------------------------------------------
# NewsFeed serialization tests
# ---------------------------------------------------------------------------


class TestNewsFeedSerialization(unittest.TestCase):
    """Tests for NewsFeed.to_json(), to_csv(), to_dataframe()."""

    def setUp(self):
        self.feed = NewsFeed.from_dicts(ARTICLES, source="test")

    def test_to_json_returns_array(self):
        """Verify to_json returns a JSON array of article dicts."""

        result = self.feed.to_json()
        parsed = json.loads(result)
        self.assertIsInstance(parsed, list)
        self.assertEqual(len(parsed), 3)
        self.assertEqual(parsed[0]["title"], "Markets Rally on Fed Decision")

    def test_to_json_indent(self):
        """Verify indent kwarg is passed through."""

        result = self.feed.to_json(indent=4)
        self.assertIn("    ", result)

    def test_to_csv_has_header(self):
        """Verify CSV output starts with a header row."""

        result = self.feed.to_csv()
        reader = csv.reader(io.StringIO(result))
        header = next(reader)
        self.assertEqual(
            header, ["title", "link", "description", "published", "source"]
        )

    def test_to_csv_has_all_rows(self):
        """Verify CSV has one row per article plus header."""

        result = self.feed.to_csv()
        lines = result.strip().split("\n")
        self.assertEqual(len(lines), 4)  # header + 3 articles

    def test_to_csv_content(self):
        """Verify CSV row content matches article data."""

        result = self.feed.to_csv()
        reader = csv.reader(io.StringIO(result))
        next(reader)  # skip header
        first_row = next(reader)
        self.assertEqual(first_row[0], "Markets Rally on Fed Decision")
        self.assertEqual(first_row[4], "test")

    def test_to_dataframe_requires_pandas(self):
        """Verify to_dataframe raises ImportError when pandas is missing."""

        with patch.dict("sys.modules", {"pandas": None}):
            with self.assertRaises(ImportError) as ctx:
                self.feed.to_dataframe()
            self.assertIn("pip install fin-news[pandas]", str(ctx.exception))

    def test_to_dataframe_returns_dataframe(self):
        """Verify to_dataframe returns a DataFrame when pandas is available."""

        try:
            import pandas  # noqa: F401
        except ImportError:
            self.skipTest("pandas not installed")

        df = self.feed.to_dataframe()
        self.assertEqual(len(df), 3)
        self.assertIn("title", df.columns)
        self.assertIn("source", df.columns)

    def test_empty_feed_to_json(self):
        """Verify empty feed serializes to empty JSON array."""

        feed = NewsFeed.from_dicts([])
        self.assertEqual(feed.to_json(), "[]")

    def test_empty_feed_to_csv(self):
        """Verify empty feed CSV has only header."""

        feed = NewsFeed.from_dicts([])
        result = feed.to_csv()
        lines = result.strip().split("\n")
        self.assertEqual(len(lines), 1)


# ---------------------------------------------------------------------------
# NewsFeed.filter() tests
# ---------------------------------------------------------------------------


class TestNewsFeedFilter(unittest.TestCase):
    """Tests for NewsFeed.filter() with since, until, max_results."""

    def setUp(self):
        self.feed = NewsFeed.from_dicts(ARTICLES, source="test")

    def test_max_results(self):
        """Verify max_results limits article count."""

        filtered = self.feed.filter(max_results=2)
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0].title, "Markets Rally on Fed Decision")

    def test_max_results_larger_than_feed(self):
        """Verify max_results > len returns all articles."""

        filtered = self.feed.filter(max_results=100)
        self.assertEqual(len(filtered), 3)

    def test_since_filter(self):
        """Verify since keeps only articles published at or after the date."""

        cutoff = datetime(2026, 4, 18, 0, 0, 0, tzinfo=timezone.utc)
        filtered = self.feed.filter(since=cutoff)
        self.assertEqual(len(filtered), 2)
        titles = [a.title for a in filtered]
        self.assertIn("Markets Rally on Fed Decision", titles)
        self.assertIn("Tech Earnings Beat Expectations", titles)

    def test_until_filter(self):
        """Verify until keeps only articles published at or before the date."""

        cutoff = datetime(2026, 4, 18, 0, 0, 0, tzinfo=timezone.utc)
        filtered = self.feed.filter(until=cutoff)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Oil Prices Surge")

    def test_since_and_until_combined(self):
        """Verify both since and until can be used together."""

        since = datetime(2026, 4, 17, 12, 0, 0, tzinfo=timezone.utc)
        until = datetime(2026, 4, 19, 0, 0, 0, tzinfo=timezone.utc)
        filtered = self.feed.filter(since=since, until=until)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Tech Earnings Beat Expectations")

    def test_filter_with_max_results_after_date(self):
        """Verify max_results applies after date filtering."""

        cutoff = datetime(2026, 4, 17, 0, 0, 0, tzinfo=timezone.utc)
        filtered = self.feed.filter(since=cutoff, max_results=1)
        self.assertEqual(len(filtered), 1)

    def test_filter_keeps_unparseable_dates(self):
        """Verify articles with invalid dates are kept, not dropped."""

        items = [
            {"title": "No date", "link": "https://example.com/x"},
            ARTICLES[0],
        ]
        feed = NewsFeed.from_dicts(items, source="test")
        cutoff = datetime(2026, 4, 20, 0, 0, 0, tzinfo=timezone.utc)
        filtered = feed.filter(since=cutoff)
        # The "No date" article has empty published — should be kept.
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "No date")

    def test_filter_naive_datetime_treated_as_utc(self):
        """Verify naive datetimes are treated as UTC."""

        cutoff = datetime(2026, 4, 18, 0, 0, 0)  # no tzinfo
        filtered = self.feed.filter(since=cutoff)
        self.assertEqual(len(filtered), 2)

    def test_filter_returns_new_feed(self):
        """Verify filter returns a new NewsFeed, not a mutation."""

        filtered = self.feed.filter(max_results=1)
        self.assertIsNot(filtered, self.feed)
        self.assertEqual(len(self.feed), 3)
        self.assertEqual(filtered.source, self.feed.source)


# ---------------------------------------------------------------------------
# TTL cache tests
# ---------------------------------------------------------------------------


SAMPLE_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <item>
      <title>Cached Article</title>
      <link>https://example.com/cached</link>
    </item>
  </channel>
</rss>"""


class TestTTLCache(unittest.TestCase):
    """Tests for the in-memory TTL response cache."""

    def setUp(self):
        clear_cache()

    def tearDown(self):
        clear_cache()

    @patch("finnews.parser.requests.Session")
    def test_cache_stores_and_returns(self, mock_session_cls):
        """Verify a cached response is reused on the second call."""

        mock_response = MagicMock()
        mock_response.content = SAMPLE_XML
        mock_response.raise_for_status = MagicMock()
        mock_session_cls.return_value.get.return_value = mock_response

        parser = NewsParser(client="cnbc", cache_ttl=60)
        url = "https://example.com/feed"

        # First call — should hit the network.
        result1 = parser.make_request(url=url)
        self.assertEqual(mock_session_cls.return_value.get.call_count, 1)

        # Second call — should come from cache.
        result2 = parser.make_request(url=url)
        self.assertEqual(mock_session_cls.return_value.get.call_count, 1)
        self.assertEqual(result1, result2)

    @patch("finnews.parser.requests.Session")
    def test_cache_expires(self, mock_session_cls):
        """Verify cache entry expires after TTL."""

        mock_response = MagicMock()
        mock_response.content = SAMPLE_XML
        mock_response.raise_for_status = MagicMock()
        mock_session_cls.return_value.get.return_value = mock_response

        parser = NewsParser(client="cnbc", cache_ttl=1)
        url = "https://example.com/feed-expire"

        parser.make_request(url=url)
        self.assertEqual(mock_session_cls.return_value.get.call_count, 1)

        # Expire the cache entry by manipulating the timestamp.
        for key in list(_response_cache):
            ts, data = _response_cache[key]
            _response_cache[key] = (ts - 10, data)

        parser.make_request(url=url)
        self.assertEqual(mock_session_cls.return_value.get.call_count, 2)

    @patch("finnews.parser.requests.Session")
    def test_no_cache_when_ttl_zero(self, mock_session_cls):
        """Verify caching is disabled when cache_ttl=0."""

        mock_response = MagicMock()
        mock_response.content = SAMPLE_XML
        mock_response.raise_for_status = MagicMock()
        mock_session_cls.return_value.get.return_value = mock_response

        parser = NewsParser(client="cnbc", cache_ttl=0)
        url = "https://example.com/feed-nocache"

        parser.make_request(url=url)
        parser.make_request(url=url)
        self.assertEqual(mock_session_cls.return_value.get.call_count, 2)

    def test_clear_cache(self):
        """Verify clear_cache empties the cache dict."""

        _response_cache["test_key"] = (time.time(), [{"title": "test"}])
        self.assertEqual(len(_response_cache), 1)
        clear_cache()
        self.assertEqual(len(_response_cache), 0)

    def test_cache_ttl_on_news_client(self):
        """Verify News(cache_ttl=60) propagates to provider parsers."""

        from finnews.client import News

        client = News(cache_ttl=120)
        cnbc = client.cnbc
        self.assertEqual(cnbc.news_parser.cache_ttl, 120)

    def test_cache_key_with_params(self):
        """Verify cache keys differ based on query params."""

        from finnews.parser import _cache_key

        key1 = _cache_key("https://example.com", {"a": "1", "b": "2"})
        key2 = _cache_key("https://example.com", {"b": "2", "a": "1"})
        key3 = _cache_key("https://example.com", None)

        # Same params in different order → same key.
        self.assertEqual(key1, key2)
        # No params → different key.
        self.assertNotEqual(key1, key3)


# ---------------------------------------------------------------------------
# Async client tests
# ---------------------------------------------------------------------------


class TestAsyncClientImport(unittest.TestCase):
    """Tests for the async client module availability."""

    def test_async_news_importable(self):
        """Verify AsyncNews can be imported."""

        from finnews.async_client import AsyncNews
        client = AsyncNews()
        self.assertIsNotNone(client)

    def test_async_news_requires_context_manager(self):
        """Verify fetch raises RuntimeError outside context manager."""

        import asyncio
        from finnews.async_client import AsyncNews

        async def _run():
            client = AsyncNews()
            with self.assertRaises(RuntimeError):
                await client.fetch("https://example.com")

        asyncio.run(_run())


if __name__ == "__main__":
    unittest.main()
