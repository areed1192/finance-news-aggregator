"""Tests for exception hierarchy, deprecation aliases, caching, logging,
enums, and duplicate XML tags."""

# pylint: disable=protected-access

import unittest
import warnings
from unittest.mock import patch, MagicMock

from finnews.client import News
from finnews.cnbc import CNBC
from finnews.cnn_finance import CNNFinance
from finnews.market_watch import MarketWatch
from finnews.nasdaq import NASDAQ
from finnews.sp_global import SPGlobal
from finnews.parser import NewsParser
from finnews.exceptions import (
    FinnewsError,
    InvalidTopicError,
    FeedRequestError,
    FeedParseError,
)
from finnews.news_enum import MarketWatch as MarketWatchEnum


# ---------------------------------------------------------------------------
# Exception hierarchy tests
# ---------------------------------------------------------------------------


class TestExceptionHierarchy(unittest.TestCase):
    """Tests for the custom exception classes."""

    def test_finnews_error_is_base(self):
        """All custom exceptions should inherit from FinnewsError."""
        self.assertTrue(issubclass(InvalidTopicError, FinnewsError))
        self.assertTrue(issubclass(FeedRequestError, FinnewsError))
        self.assertTrue(issubclass(FeedParseError, FinnewsError))

    def test_invalid_topic_error_is_key_error(self):
        """InvalidTopicError should also be a KeyError for backward compat."""
        self.assertTrue(issubclass(InvalidTopicError, KeyError))

    def test_invalid_topic_caught_by_key_error(self):
        """Existing except KeyError handlers should still catch InvalidTopicError."""
        with self.assertRaises(KeyError):
            raise InvalidTopicError("bad topic")

    def test_invalid_topic_caught_by_finnews_error(self):
        """InvalidTopicError should also be caught by FinnewsError."""
        with self.assertRaises(FinnewsError):
            raise InvalidTopicError("bad topic")


# ---------------------------------------------------------------------------
# InvalidTopicError in providers
# ---------------------------------------------------------------------------


class TestInvalidTopicInCNBC(unittest.TestCase):
    """Tests that CNBC raises InvalidTopicError with valid topics in message."""

    def setUp(self):
        self.client = CNBC()

    def test_invalid_topic_raises_invalid_topic_error(self):
        """An invalid topic should raise InvalidTopicError."""
        with self.assertRaises(InvalidTopicError):
            self.client._check_key(topic_id="nonexistent")

    def test_error_message_contains_valid_topics(self):
        """The error message should list valid topics."""
        try:
            self.client._check_key(topic_id="nonexistent")
        except InvalidTopicError as exc:
            self.assertIn("top_news", str(exc))


class TestInvalidTopicInMarketWatch(unittest.TestCase):
    """Tests that MarketWatch raises InvalidTopicError with valid topics."""

    def setUp(self):
        self.client = MarketWatch()

    def test_invalid_topic_raises_invalid_topic_error(self):
        """An invalid topic should raise InvalidTopicError."""
        with self.assertRaises(InvalidTopicError):
            self.client._check_key(topic_id="nonexistent")

    def test_error_message_contains_valid_topics(self):
        """The error message should list valid topics."""
        try:
            self.client._check_key(topic_id="nonexistent")
        except InvalidTopicError as exc:
            self.assertIn("top_stories", str(exc))


# ---------------------------------------------------------------------------
# Deprecation alias tests
# ---------------------------------------------------------------------------


class TestDeprecationAliases(unittest.TestCase):
    """Tests that old misspelled method names emit DeprecationWarning."""

    def test_cnn_techonology_warns(self):
        """CNNFinance.techonology() should warn and delegate to technology()."""
        client = CNNFinance()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "technology", return_value=[]) as mock:
                client.techonology()
                mock.assert_called_once()
            self.assertEqual(len(w), 1)
            self.assertIn("deprecated", str(w[0].message).lower())

    def test_nasdaq_artifical_intelligence_warns(self):
        """NASDAQ.artifical_intelligence_feed() should warn."""
        client = NASDAQ()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(
                client, "artificial_intelligence_feed", return_value=[]
            ) as mock:
                client.artifical_intelligence_feed()
                mock.assert_called_once()
            self.assertEqual(len(w), 1)
            self.assertIn("deprecated", str(w[0].message).lower())

    def test_sp_global_all_indicies_warns(self):
        """SPGlobal.all_indicies() should warn and delegate to all_indices()."""
        client = SPGlobal()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "all_indices", return_value=[]) as mock:
                client.all_indicies()
                mock.assert_called_once()
            self.assertEqual(len(w), 1)
            self.assertIn("deprecated", str(w[0].message).lower())

    def test_sp_global_index_announcments_warns(self):
        """SPGlobal.index_announcments() should warn."""
        client = SPGlobal()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "index_announcements", return_value=[]) as mock:
                client.index_announcments()
                mock.assert_called_once()
            self.assertEqual(len(w), 1)
            self.assertIn("deprecated", str(w[0].message).lower())

    def test_sp_global_new_counsultations_warns(self):
        """SPGlobal.new_counsultations() should warn."""
        client = SPGlobal()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            with patch.object(client, "new_consultations", return_value=[]) as mock:
                client.new_counsultations()
                mock.assert_called_once()
            self.assertEqual(len(w), 1)
            self.assertIn("deprecated", str(w[0].message).lower())


# ---------------------------------------------------------------------------
# Client property caching tests
# ---------------------------------------------------------------------------


class TestClientPropertyCaching(unittest.TestCase):
    """Tests that News properties cache and return the same instance."""

    def setUp(self):
        self.client = News()

    def test_cnbc_cached(self):
        """Accessing .cnbc twice should return the same instance."""
        first = self.client.cnbc
        second = self.client.cnbc
        self.assertIs(first, second)

    def test_nasdaq_cached(self):
        """Accessing .nasdaq twice should return the same instance."""
        first = self.client.nasdaq
        second = self.client.nasdaq
        self.assertIs(first, second)

    def test_market_watch_cached(self):
        """Accessing .market_watch twice should return the same instance."""
        first = self.client.market_watch
        second = self.client.market_watch
        self.assertIs(first, second)

    def test_sp_global_cached(self):
        """Accessing .sp_global twice should return the same instance."""
        first = self.client.sp_global
        second = self.client.sp_global
        self.assertIs(first, second)

    def test_cnn_finance_cached(self):
        """Accessing .cnn_finance twice should return the same instance."""
        first = self.client.cnn_finance
        second = self.client.cnn_finance
        self.assertIs(first, second)

    def test_wsj_cached(self):
        """Accessing .wsj twice should return the same instance."""
        first = self.client.wsj
        second = self.client.wsj
        self.assertIs(first, second)

    def test_yahoo_finance_cached(self):
        """Accessing .yahoo_finance twice should return the same instance."""
        first = self.client.yahoo_finance
        second = self.client.yahoo_finance
        self.assertIs(first, second)


# ---------------------------------------------------------------------------
# MarketWatch Enum support tests
# ---------------------------------------------------------------------------


class TestMarketWatchEnumSupport(unittest.TestCase):
    """Tests that MarketWatch._check_key accepts Enum values."""

    def setUp(self):
        self.client = MarketWatch()

    def test_enum_resolves_to_url(self):
        """Passing a market_watch Enum should resolve to a valid URL."""
        url = self.client._check_key(topic_id=MarketWatchEnum.TOP_STORIES)
        self.assertIn("mw_topstories", url)
        self.assertNotIn("{topic}", url)

    def test_all_enum_members_resolve(self):
        """Every member of the market_watch Enum should produce a URL."""
        for member in MarketWatchEnum:
            url = self.client._check_key(topic_id=member)
            self.assertIsInstance(url, str)
            self.assertNotIn("{topic}", url)


# ---------------------------------------------------------------------------
# Duplicate XML tag handling tests
# ---------------------------------------------------------------------------

SAMPLE_RSS_DUPLICATE_TAGS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <item>
      <title>Article</title>
      <link>https://example.com/article</link>
      <category>Finance</category>
      <category>Markets</category>
      <category>Stocks</category>
    </item>
  </channel>
</rss>
"""


class TestDuplicateXMLTags(unittest.TestCase):
    """Tests that duplicate XML tags are collected into lists."""

    def setUp(self):
        self.parser = NewsParser(client="cnbc")

    def test_duplicate_tags_become_list(self):
        """Multiple <category> tags should be collected into a list."""
        result = self.parser.parse_response(SAMPLE_RSS_DUPLICATE_TAGS)
        self.assertEqual(len(result), 1)
        item = result[0]
        self.assertIsInstance(item["category"], list)
        self.assertEqual(item["category"], ["Finance", "Markets", "Stocks"])

    def test_single_tags_remain_string(self):
        """Tags that appear only once should remain a plain string."""
        result = self.parser.parse_response(SAMPLE_RSS_DUPLICATE_TAGS)
        item = result[0]
        self.assertIsInstance(item["title"], str)
        self.assertEqual(item["title"], "Article")


# ---------------------------------------------------------------------------
# Retry / FeedRequestError / FeedParseError tests
# ---------------------------------------------------------------------------


class TestRetryAndErrorWrapping(unittest.TestCase):
    """Tests for retry adapter mounting and error wrapping."""

    def setUp(self):
        self.parser = NewsParser(client="cnbc")

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_session_mounts_retry_adapter(self, mock_ua_class, mock_session_class):
        """Session should have retry adapters mounted for https and http."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = b"<rss><channel></channel></rss>"
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        self.parser.make_request(url="https://example.com/feed")

        # Verify mount was called for both schemes.
        mount_calls = [call[0][0] for call in mock_session.mount.call_args_list]
        self.assertIn("https://", mount_calls)
        self.assertIn("http://", mount_calls)

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_malformed_response_raises_feed_parse_error(
        self, mock_ua_class, mock_session_class
    ):
        """Malformed XML in a successful response should raise FeedParseError."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = b"<rss><channel><item><title>Broken"
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        with self.assertRaises(FeedParseError):
            self.parser.make_request(url="https://example.com/feed")


if __name__ == "__main__":
    unittest.main()
