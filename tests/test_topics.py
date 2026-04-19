"""Tests for topic/feed validation, topics/feeds properties, and enum support."""

# pylint: disable=protected-access

import pytest

from finnews.cnbc import CNBC
from finnews.cnn_finance import CNNFinance
from finnews.market_watch import MarketWatch
from finnews.nasdaq import NASDAQ
from finnews.seeking_alpha import SeekingAlpha
from finnews.sp_global import SPGlobal
from finnews.wsj import WallStreetJournal
from finnews.yahoo_finance import YahooFinance
from finnews.exceptions import InvalidTopicError
from finnews.news_enum import MarketWatch as MarketWatchEnum


# ---------------------------------------------------------------------------
# CNBC _check_key tests
# ---------------------------------------------------------------------------


class TestCNBCCheckKey:
    """Tests for CNBC topic key validation."""

    def test_valid_topic_returns_url(self):
        """Verify a valid topic returns a fully-formed URL."""
        client = CNBC()
        url = client._check_key(topic_id="top_news")

        assert "100003114" in url
        assert url.startswith("https://www.cnbc.com/id/")

    def test_multiple_valid_topics(self):
        """Verify all topics in the category dict resolve to a URL."""
        client = CNBC()

        for topic in client.topic_categories:
            url = client._check_key(topic_id=topic)
            assert isinstance(url, str)
            assert url.startswith("https://")

    def test_invalid_topic_raises_invalid_topic_error(self):
        """Verify an invalid topic raises InvalidTopicError."""
        client = CNBC()

        with pytest.raises(InvalidTopicError):
            client._check_key(topic_id="nonexistent_topic")

    def test_empty_string_raises_invalid_topic_error(self):
        """Verify an empty string raises InvalidTopicError."""
        client = CNBC()

        with pytest.raises(InvalidTopicError):
            client._check_key(topic_id="")

    def test_error_message_contains_valid_topics(self):
        """Verify the error message lists valid topic keys."""
        client = CNBC()

        with pytest.raises(InvalidTopicError, match="top_news"):
            client._check_key(topic_id="nonexistent")


# ---------------------------------------------------------------------------
# MarketWatch _check_key tests
# ---------------------------------------------------------------------------


class TestMarketWatchCheckKey:
    """Tests for MarketWatch topic key validation."""

    def test_valid_topic_returns_url(self):
        """Verify a valid topic returns a fully-formed URL."""
        client = MarketWatch()
        url = client._check_key(topic_id="top_stories")

        assert "mw_topstories" in url
        assert url.startswith("https://")

    def test_url_contains_topic_value(self):
        """Verify the URL contains the mapped value, not a placeholder."""
        client = MarketWatch()
        url = client._check_key(topic_id="real_time_headlines")

        assert "mw_realtimeheadlines" in url
        assert "{topic}" not in url

    def test_multiple_valid_topics(self):
        """Verify all topics in the category dict resolve to a URL."""
        client = MarketWatch()

        for topic in client.topic_categories:
            url = client._check_key(topic_id=topic)
            assert isinstance(url, str)
            assert "{topic}" not in url

    def test_invalid_topic_raises_invalid_topic_error(self):
        """Verify an invalid topic raises InvalidTopicError."""
        client = MarketWatch()

        with pytest.raises(InvalidTopicError):
            client._check_key(topic_id="nonexistent_topic")

    def test_empty_string_raises_invalid_topic_error(self):
        """Verify an empty string raises InvalidTopicError."""
        client = MarketWatch()

        with pytest.raises(InvalidTopicError):
            client._check_key(topic_id="")

    def test_error_message_contains_valid_topics(self):
        """Verify the error message lists valid topic keys."""
        client = MarketWatch()

        with pytest.raises(InvalidTopicError, match="top_stories"):
            client._check_key(topic_id="nonexistent")


# ---------------------------------------------------------------------------
# topics property tests
# ---------------------------------------------------------------------------


class TestTopicsProperty:
    """Tests for the topics property on topic-based providers."""

    def test_cnbc_topics_returns_sorted_list(self):
        """Verify CNBC topics returns a sorted list of strings."""
        topics = CNBC().topics

        assert isinstance(topics, list)
        assert topics == sorted(topics)
        assert "top_news" in topics
        assert "investing" in topics

    def test_market_watch_topics_returns_sorted_list(self):
        """Verify MarketWatch topics returns a sorted list with 4 entries."""
        topics = MarketWatch().topics

        assert isinstance(topics, list)
        assert topics == sorted(topics)
        assert "top_stories" in topics
        assert "bulletins" in topics
        assert len(topics) == 4


# ---------------------------------------------------------------------------
# feeds property tests
# ---------------------------------------------------------------------------


class TestFeedsProperty:
    """Tests for the feeds property on method-based providers."""

    def test_nasdaq_feeds(self):
        """Verify NASDAQ feeds list is sorted and contains known methods."""
        feeds = NASDAQ().feeds

        assert isinstance(feeds, list)
        assert feeds == sorted(feeds)
        assert "artificial_intelligence_feed" in feeds
        assert "commodities_feed" in feeds

    def test_sp_global_feeds(self):
        """Verify S&P Global feeds list has 14 entries with known methods."""
        feeds = SPGlobal().feeds

        assert feeds == sorted(feeds)
        assert "all_indices" in feeds
        assert "research" in feeds
        assert "daily_index_insights" in feeds
        assert "case_shiller_home_price_indices" in feeds
        assert len(feeds) == 14

    def test_cnn_finance_feeds(self):
        """Verify CNN Finance feeds list is sorted and contains known methods."""
        feeds = CNNFinance().feeds

        assert feeds == sorted(feeds)
        assert "technology" in feeds
        assert "top_stories" in feeds

    def test_seeking_alpha_feeds(self):
        """Verify Seeking Alpha feeds list is sorted and contains known methods."""
        feeds = SeekingAlpha().feeds

        assert feeds == sorted(feeds)
        assert "stocks" in feeds
        assert "latest_articles" in feeds

    def test_wsj_feeds(self):
        """Verify WSJ feeds list is sorted with 6 entries."""
        feeds = WallStreetJournal().feeds

        assert feeds == sorted(feeds)
        assert "opinions" in feeds
        assert len(feeds) == 6

    def test_yahoo_finance_feeds(self):
        """Verify Yahoo Finance feeds list is sorted with 2 entries."""
        feeds = YahooFinance().feeds

        assert feeds == sorted(feeds)
        assert "news" in feeds
        assert len(feeds) == 2


# ---------------------------------------------------------------------------
# MarketWatch enum support tests
# ---------------------------------------------------------------------------


class TestMarketWatchEnumSupport:
    """Tests that MarketWatch._check_key accepts Enum values."""

    def test_enum_resolves_to_url(self):
        """Verify passing a MarketWatch Enum resolves to a valid URL."""
        client = MarketWatch()
        url = client._check_key(topic_id=MarketWatchEnum.TOP_STORIES)

        assert "mw_topstories" in url
        assert "{topic}" not in url

    def test_all_enum_members_resolve(self):
        """Verify every MarketWatch enum member produces a URL."""
        client = MarketWatch()

        for member in MarketWatchEnum:
            url = client._check_key(topic_id=member)
            assert isinstance(url, str)
            assert "{topic}" not in url
