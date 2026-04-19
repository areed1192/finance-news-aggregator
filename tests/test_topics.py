"""Tests for CNBC._check_key and MarketWatch._check_key topic validation."""
# pylint: disable=protected-access

import unittest

from finnews.cnbc import CNBC
from finnews.market_watch import MarketWatch


class TestCNBCCheckKey(unittest.TestCase):
    """Tests for CNBC topic key validation."""

    def setUp(self):
        self.client = CNBC()

    def test_valid_topic_returns_url(self):
        """A valid topic should return a fully-formed URL."""
        url = self.client._check_key(topic_id='top_news')
        self.assertIn('100003114', url)
        self.assertTrue(url.startswith('https://www.cnbc.com/id/'))

    def test_multiple_valid_topics(self):
        """All topics in the category dict should resolve to a URL."""
        for topic in self.client.topic_categories:
            url = self.client._check_key(topic_id=topic)
            self.assertIsInstance(url, str)
            self.assertTrue(url.startswith('https://'))

    def test_invalid_topic_raises_key_error(self):
        """An invalid topic should raise a KeyError."""
        with self.assertRaises(KeyError):
            self.client._check_key(topic_id='nonexistent_topic')

    def test_empty_string_raises_key_error(self):
        """An empty string topic should raise a KeyError."""
        with self.assertRaises(KeyError):
            self.client._check_key(topic_id='')


class TestMarketWatchCheckKey(unittest.TestCase):
    """Tests for MarketWatch topic key validation."""

    def setUp(self):
        self.client = MarketWatch()

    def test_valid_topic_returns_url(self):
        """A valid topic should return a fully-formed URL."""
        url = self.client._check_key(topic_id='top_stories')
        self.assertIn('mw_topstories', url)
        self.assertTrue(url.startswith('https://'))

    def test_url_contains_topic_value(self):
        """The returned URL should contain the mapped topic value, not the key."""
        url = self.client._check_key(topic_id='real_time_headlines')
        self.assertIn('mw_realtimeheadlines', url)
        # Ensure the {topic} placeholder was actually substituted.
        self.assertNotIn('{topic}', url)

    def test_multiple_valid_topics(self):
        """All topics in the category dict should resolve to a URL."""
        for topic in self.client.topic_categories:
            url = self.client._check_key(topic_id=topic)
            self.assertIsInstance(url, str)
            self.assertNotIn('{topic}', url)

    def test_invalid_topic_raises_key_error(self):
        """An invalid topic should raise a KeyError."""
        with self.assertRaises(KeyError):
            self.client._check_key(topic_id='nonexistent_topic')

    def test_empty_string_raises_key_error(self):
        """An empty string topic should raise a KeyError."""
        with self.assertRaises(KeyError):
            self.client._check_key(topic_id='')


if __name__ == '__main__':
    unittest.main()
