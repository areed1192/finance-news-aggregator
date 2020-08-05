import unittest

from unittest import TestCase
from finnews.client import News
from finnews.cnbc import CNBC
from finnews.nasdaq import NASDAQ
from finnews.market_watch import MarketWatch


class TestNewsClient(TestCase):

    """Will perform a unit test for the `NewsClient` session."""

    def setUp(self) -> None:
        """Set up the Client."""

        self.news_client = News()

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `News` client."""

        self.assertIsInstance(self.news_client, News)

    def test_creates_cnbc_instance(self):
        """Create an instance and make sure it's a `CNBC` client."""

        # Grab the client.
        self.cnbc_client = self.news_client.cnbc

        # Make sure it's a CNBC client.
        self.assertIsInstance(self.cnbc_client, CNBC)
        self.assertIsNotNone(self.news_client._cnbc_client)

    def test_creates_nasdaq_instance(self):
        """Create an instance and make sure it's a `NASDAQ` client."""

        # Grab the client.
        self.nasdaq_client = self.news_client.nasdaq

        # Make sure it's a NASDAQ client.
        self.assertIsInstance(self.nasdaq_client, NASDAQ)
        self.assertIsNotNone(self.news_client._nasdaq_client)

    def test_creates_market_watch_instance(self):
        """Create an instance and make sure it's a `MarketWatch` client."""

        # Grab the client.
        self.market_watch_client = self.news_client.market_Watch

        # Make sure it's a NASDAQ client.
        self.assertIsInstance(self.market_watch_client, MarketWatch)
        self.assertIsNotNone(self.news_client._market_watch_client)

    def tearDown(self) -> None:
        """Teardown the `NewsClient`."""

        del self.news_client


if __name__ == '__main__':
    unittest.main()
