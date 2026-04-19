"""Tests for the NewsParser class."""

import time
from unittest.mock import patch, MagicMock

import pytest
import requests

from finnews.parser import NewsParser, _response_cache, clear_cache
from finnews.exceptions import FeedRequestError, FeedParseError
from conftest import (
    SAMPLE_RSS_XML,
    SAMPLE_RSS_XML_WITH_NAMESPACE,
    MALFORMED_XML,
    SAMPLE_RSS_DUPLICATE_TAGS,
    SAMPLE_CACHE_XML,
)


# ---------------------------------------------------------------------------
# parse_response tests
# ---------------------------------------------------------------------------


class TestParseResponse:
    """Tests for NewsParser.parse_response."""

    def test_parses_basic_rss_items(self):
        """Verify two items are parsed from a standard RSS feed."""
        parser = NewsParser(client="cnbc")
        result = parser.parse_response(SAMPLE_RSS_XML)

        assert isinstance(result, list)
        assert len(result) == 2

    def test_item_contains_expected_fields(self):
        """Verify each item contains title, link, description, pubDate."""
        parser = NewsParser(client="cnbc")
        result = parser.parse_response(SAMPLE_RSS_XML)
        first = result[0]

        assert first["title"] == "Article One"
        assert first["link"] == "https://example.com/article-one"
        assert first["description"] == "First article description."
        assert "pubDate" in first

    def test_strips_whitespace_from_values(self):
        """Verify text values are stripped of surrounding whitespace."""
        parser = NewsParser(client="cnbc")
        result = parser.parse_response(SAMPLE_RSS_XML)

        for item in result:
            for value in item.values():
                if value:
                    assert value == value.strip()

    def test_namespace_stripping(self):
        """Verify namespace prefixes are removed from tag names."""
        parser = NewsParser(client="cnbc")
        result = parser.parse_response(SAMPLE_RSS_XML_WITH_NAMESPACE)

        assert len(result) == 1
        assert "type" in result[0]
        assert result[0]["type"] == "news"

    def test_empty_feed_returns_empty_list(self):
        """Verify a feed with no items returns an empty list."""
        parser = NewsParser(client="cnbc")
        empty_rss = b"""<?xml version="1.0"?>
        <rss version="2.0"><channel><title>Empty</title></channel></rss>"""
        result = parser.parse_response(empty_rss)

        assert result == []

    def test_malformed_xml_raises(self):
        """Verify malformed XML raises an exception."""
        parser = NewsParser(client="cnbc")

        with pytest.raises(Exception):
            parser.parse_response(MALFORMED_XML)

    def test_all_client_paths_are_configured(self):
        """Verify every supported client has a path and namespace entry."""
        expected_clients = [
            "cnbc", "nasdaq", "market_watch", "sp_global",
            "seeking_alpha", "cnn_finance", "wsj", "yahoo",
        ]
        parser = NewsParser(client="cnbc")

        for client_name in expected_clients:
            assert client_name in parser.paths
            assert client_name in parser.namespaces

    def test_duplicate_tags_become_list(self):
        """Verify multiple same-name tags are collected into a list."""
        parser = NewsParser(client="cnbc")
        result = parser.parse_response(SAMPLE_RSS_DUPLICATE_TAGS)

        assert len(result) == 1
        assert isinstance(result[0]["category"], list)
        assert result[0]["category"] == ["Finance", "Markets", "Stocks"]

    def test_single_tags_remain_string(self):
        """Verify tags that appear only once remain a plain string."""
        parser = NewsParser(client="cnbc")
        result = parser.parse_response(SAMPLE_RSS_DUPLICATE_TAGS)

        assert isinstance(result[0]["title"], str)
        assert result[0]["title"] == "Article"


# ---------------------------------------------------------------------------
# make_request tests
# ---------------------------------------------------------------------------


class TestMakeRequest:
    """Tests for NewsParser.make_request using mocked HTTP responses."""

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_successful_request_returns_parsed_data(self, mock_ua_class, mock_session_class):
        """Verify a successful HTTP request returns parsed items."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        parser = NewsParser(client="cnbc")
        result = parser.make_request(url="https://example.com/feed")

        assert len(result) == 2
        mock_session.get.assert_called_once()
        mock_response.raise_for_status.assert_called_once()

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_request_uses_timeout(self, mock_ua_class, mock_session_class):
        """Verify HTTP request includes a timeout parameter."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        parser = NewsParser(client="cnbc")
        parser.make_request(url="https://example.com/feed")

        call_kwargs = mock_session.get.call_args
        assert "timeout" in call_kwargs.kwargs
        assert call_kwargs.kwargs["timeout"] == 10

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_request_passes_params(self, mock_ua_class, mock_session_class):
        """Verify query parameters are forwarded to session.get."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        parser = NewsParser(client="cnbc")
        params = {"category": "Stocks"}
        parser.make_request(url="https://example.com/feed", params=params)

        call_kwargs = mock_session.get.call_args
        assert call_kwargs.kwargs["params"] == params

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_http_error_raises_feed_request_error(self, mock_ua_class, mock_session_class):
        """Verify an HTTP error raises FeedRequestError."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_session.get.return_value = mock_response

        parser = NewsParser(client="cnbc")

        with pytest.raises(FeedRequestError):
            parser.make_request(url="https://example.com/bad-feed")

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_request_sets_user_agent_header(self, mock_ua_class, mock_session_class):
        """Verify request includes a user-agent header."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        parser = NewsParser(client="cnbc")
        parser.make_request(url="https://example.com/feed")

        call_kwargs = mock_session.get.call_args
        assert "user-agent" in call_kwargs.kwargs["headers"]
        assert call_kwargs.kwargs["headers"]["user-agent"] == "FakeAgent/1.0"

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_session_mounts_retry_adapter(self, mock_ua_class, mock_session_class):
        """Verify session has retry adapters mounted for https and http."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = b"<rss><channel></channel></rss>"
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        parser = NewsParser(client="cnbc")
        parser.make_request(url="https://example.com/feed")

        mount_calls = [call[0][0] for call in mock_session.mount.call_args_list]
        assert "https://" in mount_calls
        assert "http://" in mount_calls

    @patch("finnews.parser.requests.Session")
    @patch("finnews.parser.UserAgent")
    def test_malformed_response_raises_feed_parse_error(
        self, mock_ua_class, mock_session_class
    ):
        """Verify malformed XML in a successful response raises FeedParseError."""
        mock_ua_class.return_value.edge = "FakeAgent/1.0"
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = b"<rss><channel><item><title>Broken"
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        parser = NewsParser(client="cnbc")

        with pytest.raises(FeedParseError):
            parser.make_request(url="https://example.com/feed")


# ---------------------------------------------------------------------------
# TTL cache tests
# ---------------------------------------------------------------------------


class TestTTLCache:
    """Tests for the in-memory TTL response cache."""

    def setup_method(self):
        """Clear the cache before each test."""
        clear_cache()

    def teardown_method(self):
        """Clear the cache after each test."""
        clear_cache()

    @patch("finnews.parser.requests.Session")
    def test_cache_stores_and_returns(self, mock_session_cls):
        """Verify a cached response is reused on the second call."""
        mock_response = MagicMock()
        mock_response.content = SAMPLE_CACHE_XML
        mock_response.raise_for_status = MagicMock()
        mock_session_cls.return_value.get.return_value = mock_response

        parser = NewsParser(client="cnbc", cache_ttl=60)
        url = "https://example.com/feed"

        result1 = parser.make_request(url=url)
        assert mock_session_cls.return_value.get.call_count == 1

        result2 = parser.make_request(url=url)
        assert mock_session_cls.return_value.get.call_count == 1
        assert result1 == result2

    @patch("finnews.parser.requests.Session")
    def test_cache_expires(self, mock_session_cls):
        """Verify cache entry expires after TTL."""
        mock_response = MagicMock()
        mock_response.content = SAMPLE_CACHE_XML
        mock_response.raise_for_status = MagicMock()
        mock_session_cls.return_value.get.return_value = mock_response

        parser = NewsParser(client="cnbc", cache_ttl=1)
        url = "https://example.com/feed-expire"

        parser.make_request(url=url)
        assert mock_session_cls.return_value.get.call_count == 1

        # Expire the cache entry by manipulating the timestamp.
        for key in list(_response_cache):
            ts, data = _response_cache[key]
            _response_cache[key] = (ts - 10, data)

        parser.make_request(url=url)
        assert mock_session_cls.return_value.get.call_count == 2

    @patch("finnews.parser.requests.Session")
    def test_no_cache_when_ttl_zero(self, mock_session_cls):
        """Verify caching is disabled when cache_ttl=0."""
        mock_response = MagicMock()
        mock_response.content = SAMPLE_CACHE_XML
        mock_response.raise_for_status = MagicMock()
        mock_session_cls.return_value.get.return_value = mock_response

        parser = NewsParser(client="cnbc", cache_ttl=0)
        url = "https://example.com/feed-nocache"

        parser.make_request(url=url)
        parser.make_request(url=url)
        assert mock_session_cls.return_value.get.call_count == 2

    def test_clear_cache(self):
        """Verify clear_cache empties the cache dict."""
        _response_cache["test_key"] = (time.time(), [{"title": "test"}])
        assert len(_response_cache) == 1

        clear_cache()
        assert len(_response_cache) == 0

    def test_cache_key_with_params(self):
        """Verify cache keys differ based on query params."""
        from finnews.parser import _cache_key

        key1 = _cache_key("https://example.com", {"a": "1", "b": "2"})
        key2 = _cache_key("https://example.com", {"b": "2", "a": "1"})
        key3 = _cache_key("https://example.com", None)

        # Same params in different order produce the same key.
        assert key1 == key2
        # No params produce a different key.
        assert key1 != key3
