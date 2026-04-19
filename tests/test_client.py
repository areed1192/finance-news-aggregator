"""Tests for the News facade client and provider instance creation."""

from finnews.client import News
from finnews.cnbc import CNBC
from finnews.cnn_finance import CNNFinance
from finnews.market_watch import MarketWatch
from finnews.nasdaq import NASDAQ
from finnews.seeking_alpha import SeekingAlpha
from finnews.sp_global import SPGlobal
from finnews.wsj import WallStreetJournal
from finnews.yahoo_finance import YahooFinance


# ---------------------------------------------------------------------------
# Provider instance creation tests
# ---------------------------------------------------------------------------


class TestNewsClient:
    """Tests for the News facade client."""

    def test_creates_instance_of_session(self, news_client):
        """Verify News() creates a News instance."""
        assert isinstance(news_client, News)

    def test_creates_cnbc_instance(self, news_client):
        """Verify .cnbc returns a CNBC instance."""
        assert isinstance(news_client.cnbc, CNBC)

    def test_creates_nasdaq_instance(self, news_client):
        """Verify .nasdaq returns a NASDAQ instance."""
        assert isinstance(news_client.nasdaq, NASDAQ)

    def test_creates_market_watch_instance(self, news_client):
        """Verify .market_watch returns a MarketWatch instance."""
        assert isinstance(news_client.market_watch, MarketWatch)

    def test_creates_sp_global_instance(self, news_client):
        """Verify .sp_global returns a SPGlobal instance."""
        assert isinstance(news_client.sp_global, SPGlobal)

    def test_creates_seeking_alpha_instance(self, news_client):
        """Verify .seeking_alpha returns a SeekingAlpha instance."""
        assert isinstance(news_client.seeking_alpha, SeekingAlpha)

    def test_creates_cnn_finance_instance(self, news_client):
        """Verify .cnn_finance returns a CNNFinance instance."""
        assert isinstance(news_client.cnn_finance, CNNFinance)

    def test_creates_wsj_instance(self, news_client):
        """Verify .wsj returns a WallStreetJournal instance."""
        assert isinstance(news_client.wsj, WallStreetJournal)

    def test_creates_yahoo_finance_instance(self, news_client):
        """Verify .yahoo_finance returns a YahooFinance instance."""
        assert isinstance(news_client.yahoo_finance, YahooFinance)


# ---------------------------------------------------------------------------
# Property caching tests
# ---------------------------------------------------------------------------


class TestClientPropertyCaching:
    """Tests that News properties cache and return the same instance."""

    def test_cnbc_cached(self, news_client):
        """Verify .cnbc returns the same instance on repeated access."""
        assert news_client.cnbc is news_client.cnbc

    def test_nasdaq_cached(self, news_client):
        """Verify .nasdaq returns the same instance on repeated access."""
        assert news_client.nasdaq is news_client.nasdaq

    def test_market_watch_cached(self, news_client):
        """Verify .market_watch returns the same instance on repeated access."""
        assert news_client.market_watch is news_client.market_watch

    def test_sp_global_cached(self, news_client):
        """Verify .sp_global returns the same instance on repeated access."""
        assert news_client.sp_global is news_client.sp_global

    def test_seeking_alpha_cached(self, news_client):
        """Verify .seeking_alpha returns the same instance on repeated access."""
        assert news_client.seeking_alpha is news_client.seeking_alpha

    def test_cnn_finance_cached(self, news_client):
        """Verify .cnn_finance returns the same instance on repeated access."""
        assert news_client.cnn_finance is news_client.cnn_finance

    def test_wsj_cached(self, news_client):
        """Verify .wsj returns the same instance on repeated access."""
        assert news_client.wsj is news_client.wsj

    def test_yahoo_finance_cached(self, news_client):
        """Verify .yahoo_finance returns the same instance on repeated access."""
        assert news_client.yahoo_finance is news_client.yahoo_finance

    def test_cache_ttl_propagates_to_parser(self, news_client_cached):
        """Verify News(cache_ttl=120) propagates to provider parsers."""
        cnbc = news_client_cached.cnbc
        assert cnbc.news_parser.cache_ttl == 120
