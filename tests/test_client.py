"""Tests for the News facade client and provider instance creation."""

import unittest

from unittest import TestCase
from finnews.client import News
from finnews.cnbc import CNBC
from finnews.nasdaq import NASDAQ
from finnews.market_watch import MarketWatch
from finnews.sp_global import SPGlobal
from finnews.seeking_alpha import SeekingAlpha
from finnews.cnn_finance import CNNFinance
from finnews.wsj import WallStreetJournal
from finnews.yahoo_finance import YahooFinance


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
        cnbc_client = self.news_client.cnbc

        # Make sure it's a CNBC client.
        self.assertIsInstance(cnbc_client, CNBC)

    def test_creates_nasdaq_instance(self):
        """Create an instance and make sure it's a `NASDAQ` client."""

        # Grab the client.
        nasdaq_client = self.news_client.nasdaq

        # Make sure it's a NASDAQ client.
        self.assertIsInstance(nasdaq_client, NASDAQ)

    def test_creates_market_watch_instance(self):
        """Create an instance and make sure it's a `MarketWatch` client."""

        # Grab the client.
        market_watch_client = self.news_client.market_watch

        # Make sure it's a `MarketWatch` client.
        self.assertIsInstance(market_watch_client, MarketWatch)

    def test_creates_sp_global_instance(self):
        """Create an instance and make sure it's a `SPGlobal` client."""

        # Grab the client.
        sp_global_client = self.news_client.sp_global

        # Make sure it's a `SPGlobal` client.
        self.assertIsInstance(sp_global_client, SPGlobal)

    def test_creates_seeking_alpha_instance(self):
        """Create an instance and make sure it's a `SeekingAlpha` client."""

        # Grab the client.
        seeking_alpha_client = self.news_client.seeking_alpha

        # Make sure it's a `SeekingAlpha` client.
        self.assertIsInstance(seeking_alpha_client, SeekingAlpha)

    def test_creates_cnn_finance_instance(self):
        """Create an instance and make sure it's a `CNNFinance` client."""

        # Grab the client.
        cnn_finance_client = self.news_client.cnn_finance

        # Make sure it's a `CNNFinance` client.
        self.assertIsInstance(cnn_finance_client, CNNFinance)

    def test_creates_wsj_instance(self):
        """Create an instance and make sure it's a `WallStreetJournal` client."""

        # Grab the client.
        wsj_client = self.news_client.wsj

        # Make sure it's a `WallStreetJournal` client.
        self.assertIsInstance(wsj_client, WallStreetJournal)

    def test_creates_yahoo_finance_instance(self):
        """Create an instance and make sure it's a `YahooFinance` client."""

        # Grab the client.
        yahoo_finance_client = self.news_client.yahoo_finance

        # Make sure it's a `YahooFinance` client.
        self.assertIsInstance(yahoo_finance_client, YahooFinance)

    def tearDown(self) -> None:
        """Teardown the `NewsClient`."""

        del self.news_client


if __name__ == "__main__":
    unittest.main()
