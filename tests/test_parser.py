"""Tests for the NewsParser class."""

import unittest
from unittest.mock import patch, MagicMock

import requests

from finnews.parser import NewsParser
from finnews.exceptions import FeedRequestError


# Minimal valid RSS XML for testing parsing logic.
SAMPLE_RSS_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Test Feed</title>
    <item>
      <title>Article One</title>
      <link>https://example.com/article-one</link>
      <description>First article description.</description>
      <pubDate>Sat, 19 Apr 2026 12:00:00 GMT</pubDate>
    </item>
    <item>
      <title>Article Two</title>
      <link>https://example.com/article-two</link>
      <description>Second article description.</description>
      <pubDate>Sat, 19 Apr 2026 13:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>
"""

# RSS with a CNBC-style namespace.
SAMPLE_RSS_XML_WITH_NAMESPACE = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:cnbc="http://search.cnbc.com/rss/2.0/modules/siteContentMetadata">
  <channel>
    <item>
      <title>Namespaced Article</title>
      <link>https://example.com/ns-article</link>
      <cnbc:type>news</cnbc:type>
    </item>
  </channel>
</rss>
"""

# Malformed XML for testing error handling.
MALFORMED_XML = b"""<rss><channel><item><title>Broken"""


class TestParseResponse(unittest.TestCase):
    """Tests for NewsParser._parse_response."""

    def setUp(self):
        self.parser = NewsParser(client='cnbc')

    def test_parses_basic_rss_items(self):
        """Should parse two items from a standard RSS feed."""
        result = self.parser.parse_response(SAMPLE_RSS_XML)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)

    def test_item_contains_expected_fields(self):
        """Each parsed item should contain title, link, description, pubDate."""
        result = self.parser.parse_response(SAMPLE_RSS_XML)
        first = result[0]

        self.assertEqual(first['title'], 'Article One')
        self.assertEqual(first['link'], 'https://example.com/article-one')
        self.assertEqual(first['description'], 'First article description.')
        self.assertIn('pubDate', first)

    def test_strips_whitespace_from_values(self):
        """Text values should be stripped of surrounding whitespace."""
        result = self.parser.parse_response(SAMPLE_RSS_XML)
        for item in result:
            for value in item.values():
                if value:
                    self.assertEqual(value, value.strip())

    def test_namespace_stripping(self):
        """CNBC namespace prefixes should be removed from tag names."""
        result = self.parser.parse_response(SAMPLE_RSS_XML_WITH_NAMESPACE)
        self.assertEqual(len(result), 1)
        # The cnbc:type tag should have its namespace stripped.
        self.assertIn('type', result[0])
        self.assertEqual(result[0]['type'], 'news')

    def test_empty_feed_returns_empty_list(self):
        """An RSS feed with no items should return an empty list."""
        empty_rss = b"""<?xml version="1.0"?>
        <rss version="2.0"><channel><title>Empty</title></channel></rss>"""
        result = self.parser.parse_response(empty_rss)
        self.assertEqual(result, [])

    def test_malformed_xml_raises(self):
        """Malformed XML should raise an exception."""
        with self.assertRaises(Exception):
            self.parser.parse_response(MALFORMED_XML)

    def test_all_client_paths_are_configured(self):
        """Every supported client should have a path and namespace entry."""
        expected_clients = [
            'cnbc', 'nasdaq', 'market_watch', 'sp_global',
            'seeking_alpha', 'cnn_finance', 'wsj', 'yahoo'
        ]
        parser = NewsParser(client='cnbc')
        for client_name in expected_clients:
            self.assertIn(client_name, parser.paths)
            self.assertIn(client_name, parser.namespaces)


class TestMakeRequest(unittest.TestCase):
    """Tests for NewsParser._make_request using mocked HTTP responses."""

    def setUp(self):
        self.parser = NewsParser(client='cnbc')

    @patch('finnews.parser.requests.Session')
    @patch('finnews.parser.UserAgent')
    def test_successful_request_returns_parsed_data(self, mock_ua_class, mock_session_class):
        """A successful HTTP request should return parsed items."""
        mock_ua_class.return_value.edge = 'FakeAgent/1.0'
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        result = self.parser.make_request(url='https://example.com/feed')

        self.assertEqual(len(result), 2)
        mock_session.get.assert_called_once()
        mock_response.raise_for_status.assert_called_once()

    @patch('finnews.parser.requests.Session')
    @patch('finnews.parser.UserAgent')
    def test_request_uses_timeout(self, mock_ua_class, mock_session_class):
        """HTTP request should include a timeout parameter."""
        mock_ua_class.return_value.edge = 'FakeAgent/1.0'
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        self.parser.make_request(url='https://example.com/feed')

        call_kwargs = mock_session.get.call_args
        self.assertIn('timeout', call_kwargs.kwargs)
        self.assertEqual(call_kwargs.kwargs['timeout'], 10)

    @patch('finnews.parser.requests.Session')
    @patch('finnews.parser.UserAgent')
    def test_request_passes_params(self, mock_ua_class, mock_session_class):
        """Query parameters should be forwarded to session.get."""
        mock_ua_class.return_value.edge = 'FakeAgent/1.0'
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        params = {'category': 'Stocks'}
        self.parser.make_request(url='https://example.com/feed', params=params)

        call_kwargs = mock_session.get.call_args
        self.assertEqual(call_kwargs.kwargs['params'], params)

    @patch('finnews.parser.requests.Session')
    @patch('finnews.parser.UserAgent')
    def test_http_error_raises_feed_request_error(self, mock_ua_class, mock_session_class):
        """An HTTP error should raise FeedRequestError."""
        mock_ua_class.return_value.edge = 'FakeAgent/1.0'
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_session.get.return_value = mock_response

        with self.assertRaises(FeedRequestError):
            self.parser.make_request(url='https://example.com/bad-feed')

    @patch('finnews.parser.requests.Session')
    @patch('finnews.parser.UserAgent')
    def test_request_sets_user_agent_header(self, mock_ua_class, mock_session_class):
        """Request should include a user-agent header."""
        mock_ua_class.return_value.edge = 'FakeAgent/1.0'
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.content = SAMPLE_RSS_XML
        mock_response.raise_for_status = MagicMock()
        mock_session.get.return_value = mock_response

        self.parser.make_request(url='https://example.com/feed')

        call_kwargs = mock_session.get.call_args
        self.assertIn('user-agent', call_kwargs.kwargs['headers'])
        self.assertEqual(call_kwargs.kwargs['headers']['user-agent'], 'FakeAgent/1.0')


if __name__ == '__main__':
    unittest.main()
