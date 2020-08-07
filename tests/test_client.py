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

        # Make sure it's a `MarketWatch` client.
        self.assertIsInstance(self.market_watch_client, MarketWatch)
        self.assertIsNotNone(self.news_client._market_watch_client)

    def test_creates_sp_global_instance(self):
        """Create an instance and make sure it's a `SPGlobal` client."""

        # Grab the client.
        self.sp_global_client = self.news_client.sp_global

        # Make sure it's a `SPGlobal` client.
        self.assertIsInstance(self.sp_global_client, SPGlobal)
        self.assertIsNotNone(self.news_client._sp_global_client)

    def test_creates_seeking_alpha_instance(self):
        """Create an instance and make sure it's a `SeekingAlpha` client."""

        # Grab the client.
        self.seeking_alpha_client = self.news_client.seeking_alpha

        # Make sure it's a `SeekingAlpha` client.
        self.assertIsInstance(self.seeking_alpha_client, SeekingAlpha)
        self.assertIsNotNone(self.news_client._seeking_alpha_client)

    def test_creates_cnn_finance_instance(self):
        """Create an instance and make sure it's a `CNNFinance` client."""

        # Grab the client.
        self.cnn_finance_client = self.news_client.cnn_finance

        # Make sure it's a `CNNFinance` client.
        self.assertIsInstance(self.cnn_finance_client, CNNFinance)
        self.assertIsNotNone(self.news_client._cnn_finance_client)

    def test_creates_wsj_instance(self):
        """Create an instance and make sure it's a `WallStreetJournal` client."""

        # Grab the client.
        self.wsj_client = self.news_client.wsj

        # Make sure it's a `WallStreetJournal` client.
        self.assertIsInstance(self.wsj_client, WallStreetJournal)
        self.assertIsNotNone(self.news_client._wsj_client)

    def tearDown(self) -> None:
        """Teardown the `NewsClient`."""

        del self.news_client


if __name__ == '__main__':
    unittest.main()
