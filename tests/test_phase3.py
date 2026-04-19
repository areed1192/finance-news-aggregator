"""Tests for Phase 3 features: topics/feeds properties, NewsArticle, NewsFeed."""

import unittest

from finnews.cnbc import CNBC
from finnews.market_watch import MarketWatch
from finnews.nasdaq import NASDAQ
from finnews.sp_global import SPGlobal
from finnews.seeking_alpha import SeekingAlpha
from finnews.cnn_finance import CNNFinance
from finnews.wsj import WallStreetJournal
from finnews.yahoo_finance import YahooFinance
from finnews.article import NewsArticle, NewsFeed


# ---------------------------------------------------------------------------
# Sample data
# ---------------------------------------------------------------------------

SAMPLE_ARTICLE_DICT = {
    "title": "Markets Rally on Fed Decision",
    "link": "https://example.com/article/1",
    "description": "Stocks climbed after the Federal Reserve held rates.",
    "pubDate": "Sat, 19 Apr 2026 12:00:00 GMT",
    "category": "Markets",
    "guid": "https://example.com/article/1",
}

SAMPLE_ARTICLE_PUBLISHED = {
    "title": "Tech Earnings Beat",
    "link": "https://example.com/article/2",
    "description": "Major tech firms reported strong Q1 results.",
    "published": "Fri, 18 Apr 2026 09:00:00 GMT",
}


# ---------------------------------------------------------------------------
# Topics / feeds property tests
# ---------------------------------------------------------------------------


class TestTopicsProperty(unittest.TestCase):
    """Tests for the topics property on topic-based providers."""

    def test_cnbc_topics_returns_sorted_list(self):
        """Verify CNBC topics returns a sorted list of strings."""

        cnbc = CNBC()
        topics = cnbc.topics
        self.assertIsInstance(topics, list)
        self.assertEqual(topics, sorted(topics))
        self.assertIn("top_news", topics)
        self.assertIn("investing", topics)

    def test_market_watch_topics_returns_sorted_list(self):
        """Verify MarketWatch topics returns a sorted list of strings."""

        mw = MarketWatch()
        topics = mw.topics
        self.assertIsInstance(topics, list)
        self.assertEqual(topics, sorted(topics))
        self.assertIn("top_stories", topics)
        self.assertIn("bulletins", topics)
        self.assertEqual(len(topics), 4)


class TestFeedsProperty(unittest.TestCase):
    """Tests for the feeds property on method-based providers."""

    def test_nasdaq_feeds(self):
        """Verify NASDAQ feeds list is sorted and contains known methods."""

        nasdaq = NASDAQ()
        feeds = nasdaq.feeds
        self.assertIsInstance(feeds, list)
        self.assertEqual(feeds, sorted(feeds))
        self.assertIn("artificial_intelligence_feed", feeds)
        self.assertIn("commodities_feed", feeds)

    def test_sp_global_feeds(self):
        """Verify S&P Global feeds list is sorted and contains known methods."""

        sp = SPGlobal()
        feeds = sp.feeds
        self.assertEqual(feeds, sorted(feeds))
        self.assertIn("all_indices", feeds)
        self.assertIn("research", feeds)
        self.assertIn("daily_index_insights", feeds)
        self.assertIn("case_shiller_home_price_indices", feeds)
        self.assertEqual(len(feeds), 14)

    def test_cnn_finance_feeds(self):
        """Verify CNN Finance feeds list is sorted and contains known methods."""

        cnn = CNNFinance()
        feeds = cnn.feeds
        self.assertEqual(feeds, sorted(feeds))
        self.assertIn("technology", feeds)
        self.assertIn("top_stories", feeds)

    def test_seeking_alpha_feeds(self):
        """Verify Seeking Alpha feeds list is sorted and contains known methods."""

        sa = SeekingAlpha()
        feeds = sa.feeds
        self.assertEqual(feeds, sorted(feeds))
        self.assertIn("stocks", feeds)
        self.assertIn("latest_articles", feeds)

    def test_wsj_feeds(self):
        """Verify WSJ feeds list is sorted and contains known methods."""

        wsj = WallStreetJournal()
        feeds = wsj.feeds
        self.assertEqual(feeds, sorted(feeds))
        self.assertIn("opinions", feeds)
        self.assertEqual(len(feeds), 6)

    def test_yahoo_finance_feeds(self):
        """Verify Yahoo Finance feeds list is sorted and contains known methods."""

        yahoo = YahooFinance()
        feeds = yahoo.feeds
        self.assertEqual(feeds, sorted(feeds))
        self.assertIn("news", feeds)
        self.assertEqual(len(feeds), 2)


# ---------------------------------------------------------------------------
# NewsArticle tests
# ---------------------------------------------------------------------------


class TestNewsArticle(unittest.TestCase):
    """Tests for the NewsArticle dataclass."""

    def test_from_dict_maps_standard_fields(self):
        """Verify from_dict extracts title, link, description, pubDate."""

        article = NewsArticle.from_dict(SAMPLE_ARTICLE_DICT, source="cnbc")
        self.assertEqual(article.title, "Markets Rally on Fed Decision")
        self.assertEqual(article.link, "https://example.com/article/1")
        self.assertEqual(
            article.description, "Stocks climbed after the Federal Reserve held rates."
        )
        self.assertEqual(article.published, "Sat, 19 Apr 2026 12:00:00 GMT")
        self.assertEqual(article.source, "cnbc")

    def test_from_dict_uses_published_fallback(self):
        """Verify from_dict falls back to 'published' key when 'pubDate' is absent."""

        article = NewsArticle.from_dict(SAMPLE_ARTICLE_PUBLISHED, source="nasdaq")
        self.assertEqual(article.published, "Fri, 18 Apr 2026 09:00:00 GMT")

    def test_from_dict_stores_extra_fields(self):
        """Verify extra RSS fields are stored in the extra dict."""

        article = NewsArticle.from_dict(SAMPLE_ARTICLE_DICT, source="cnbc")
        self.assertIn("category", article.extra)
        self.assertIn("guid", article.extra)
        self.assertNotIn("title", article.extra)

    def test_from_dict_empty_dict(self):
        """Verify from_dict handles empty dictionary gracefully."""

        article = NewsArticle.from_dict({})
        self.assertEqual(article.title, "")
        self.assertEqual(article.link, "")
        self.assertEqual(article.source, "")

    def test_repr_html_returns_html_string(self):
        """Verify _repr_html_ returns valid HTML with escaped content."""

        article = NewsArticle.from_dict(SAMPLE_ARTICLE_DICT, source="cnbc")
        html_str = article._repr_html_()  # pylint: disable=protected-access
        self.assertIn("Markets Rally on Fed Decision", html_str)
        self.assertIn("https://example.com/article/1", html_str)
        self.assertIn("<div", html_str)

    def test_repr_html_escapes_special_chars(self):
        """Verify _repr_html_ escapes HTML special characters."""

        data = {"title": "<script>alert('xss')</script>", "link": "https://example.com"}
        article = NewsArticle.from_dict(data)
        html_str = article._repr_html_()  # pylint: disable=protected-access
        self.assertNotIn("<script>", html_str)
        self.assertIn("&lt;script&gt;", html_str)


# ---------------------------------------------------------------------------
# NewsFeed tests
# ---------------------------------------------------------------------------


class TestNewsFeed(unittest.TestCase):
    """Tests for the NewsFeed collection dataclass."""

    def test_from_dicts_creates_articles(self):
        """Verify from_dicts converts a list of dicts to NewsArticle instances."""

        feed = NewsFeed.from_dicts(
            [SAMPLE_ARTICLE_DICT, SAMPLE_ARTICLE_PUBLISHED],
            source="cnbc",
        )
        self.assertEqual(len(feed), 2)
        self.assertIsInstance(feed.articles[0], NewsArticle)
        self.assertEqual(feed.source, "cnbc")

    def test_from_dicts_empty_list(self):
        """Verify from_dicts handles empty list."""

        feed = NewsFeed.from_dicts([])
        self.assertEqual(len(feed), 0)

    def test_iterable(self):
        """Verify NewsFeed is iterable."""

        feed = NewsFeed.from_dicts([SAMPLE_ARTICLE_DICT], source="test")
        articles = list(feed)
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, "Markets Rally on Fed Decision")

    def test_indexable(self):
        """Verify NewsFeed supports indexing."""

        feed = NewsFeed.from_dicts(
            [SAMPLE_ARTICLE_DICT, SAMPLE_ARTICLE_PUBLISHED],
            source="test",
        )
        self.assertEqual(feed[0].title, "Markets Rally on Fed Decision")
        self.assertEqual(feed[1].title, "Tech Earnings Beat")

    def test_repr_html_returns_table(self):
        """Verify _repr_html_ returns an HTML table."""

        feed = NewsFeed.from_dicts([SAMPLE_ARTICLE_DICT], source="cnbc")
        html_str = feed._repr_html_()  # pylint: disable=protected-access
        self.assertIn("<table", html_str)
        self.assertIn("Markets Rally on Fed Decision", html_str)
        self.assertIn("1 articles", html_str)


if __name__ == "__main__":
    unittest.main()
