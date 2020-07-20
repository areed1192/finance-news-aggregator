import unittest

from unittest import TestCase
from finnews.client import News
from finnews.cnbc import CNBC


class TestNewsClient(TestCase):

    """Will perform a unit test for the `NewsClient` session."""

    def setUp(self) -> None:
        """Set up the Client."""

        self.news_client = News()

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a `NewsClient`."""

        self.assertIsInstance(self.news_client, News)

    def test_creates_cnbc_instance(self):
        """Create an instance and make sure it's a `CNBCClient`."""

        # Grab the client.
        self.cnbc_client = self.news_client.cnbc

        # Make sure it's a CNBC client.
        self.assertIsInstance(self.cnbc_client, CNBC)
        self.assertIsNotNone(self.news_client._cnbc_client)

    def tearDown(self) -> None:
        """Teardown the `NewsClient`."""

        del self.news_client


if __name__ == '__main__':
    unittest.main()
