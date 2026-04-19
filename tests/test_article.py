"""Tests for NewsArticle and NewsFeed dataclasses: construction, serialization, filtering."""

import csv
import io
import json
from datetime import datetime, timezone
from unittest.mock import patch

import pytest

from conftest import SAMPLE_ARTICLE_DICT, SAMPLE_ARTICLE_PUBLISHED, ARTICLES
from finnews.article import NewsArticle, NewsFeed


# ---------------------------------------------------------------------------
# NewsArticle construction tests
# ---------------------------------------------------------------------------


class TestNewsArticle:
    """Tests for the NewsArticle dataclass."""

    def test_from_dict_maps_standard_fields(self):
        """Verify from_dict extracts title, link, description, pubDate."""
        article = NewsArticle.from_dict(SAMPLE_ARTICLE_DICT, source="cnbc")

        assert article.title == "Markets Rally on Fed Decision"
        assert article.link == "https://example.com/article/1"
        assert article.description == "Stocks climbed after the Federal Reserve held rates."
        assert article.published == "Sat, 19 Apr 2026 12:00:00 GMT"
        assert article.source == "cnbc"

    def test_from_dict_uses_published_fallback(self):
        """Verify from_dict falls back to 'published' key when 'pubDate' absent."""
        article = NewsArticle.from_dict(SAMPLE_ARTICLE_PUBLISHED, source="nasdaq")

        assert article.published == "Fri, 18 Apr 2026 09:00:00 GMT"

    def test_from_dict_stores_extra_fields(self):
        """Verify extra RSS fields are stored in the extra dict."""
        article = NewsArticle.from_dict(SAMPLE_ARTICLE_DICT, source="cnbc")

        assert "category" in article.extra
        assert "guid" in article.extra
        assert "title" not in article.extra

    def test_from_dict_empty_dict(self):
        """Verify from_dict handles empty dictionary gracefully."""
        article = NewsArticle.from_dict({})

        assert article.title == ""
        assert article.link == ""
        assert article.source == ""

    def test_repr_html_returns_html_string(self):
        """Verify _repr_html_ returns valid HTML with article content."""
        article = NewsArticle.from_dict(SAMPLE_ARTICLE_DICT, source="cnbc")
        html_str = article._repr_html_()  # pylint: disable=protected-access

        assert "Markets Rally on Fed Decision" in html_str
        assert "https://example.com/article/1" in html_str
        assert "<div" in html_str

    def test_repr_html_escapes_special_chars(self):
        """Verify _repr_html_ escapes HTML special characters."""
        data = {"title": "<script>alert('xss')</script>", "link": "https://example.com"}
        article = NewsArticle.from_dict(data)
        html_str = article._repr_html_()  # pylint: disable=protected-access

        assert "<script>" not in html_str
        assert "&lt;script&gt;" in html_str


# ---------------------------------------------------------------------------
# NewsArticle serialization tests
# ---------------------------------------------------------------------------


class TestNewsArticleToDict:
    """Tests for NewsArticle.to_dict() and to_json()."""

    def test_to_dict_includes_standard_fields(self):
        """Verify all standard fields appear in the dict."""
        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        result = article.to_dict()

        assert result["title"] == "Markets Rally on Fed Decision"
        assert result["link"] == "https://example.com/1"
        assert result["source"] == "cnbc"
        assert "published" in result

    def test_to_dict_merges_extra(self):
        """Verify extra fields are merged into the dict."""
        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        result = article.to_dict()

        assert result["category"] == "Markets"

    def test_to_json_returns_valid_json(self):
        """Verify to_json produces valid JSON."""
        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        result = article.to_json()
        parsed = json.loads(result)

        assert parsed["title"] == "Markets Rally on Fed Decision"

    def test_to_json_passes_kwargs(self):
        """Verify kwargs are forwarded to json.dumps."""
        article = NewsArticle.from_dict(ARTICLES[0], source="cnbc")
        result = article.to_json(indent=2)

        assert "\n" in result


# ---------------------------------------------------------------------------
# NewsFeed construction tests
# ---------------------------------------------------------------------------


class TestNewsFeed:
    """Tests for the NewsFeed collection dataclass."""

    def test_from_dicts_creates_articles(self):
        """Verify from_dicts converts a list of dicts to NewsArticle instances."""
        feed = NewsFeed.from_dicts(
            [SAMPLE_ARTICLE_DICT, SAMPLE_ARTICLE_PUBLISHED],
            source="cnbc",
        )

        assert len(feed) == 2
        assert isinstance(feed.articles[0], NewsArticle)
        assert feed.source == "cnbc"

    def test_from_dicts_empty_list(self):
        """Verify from_dicts handles empty list."""
        feed = NewsFeed.from_dicts([])

        assert len(feed) == 0

    def test_iterable(self):
        """Verify NewsFeed is iterable."""
        feed = NewsFeed.from_dicts([SAMPLE_ARTICLE_DICT], source="test")
        articles = list(feed)

        assert len(articles) == 1
        assert articles[0].title == "Markets Rally on Fed Decision"

    def test_indexable(self):
        """Verify NewsFeed supports indexing."""
        feed = NewsFeed.from_dicts(
            [SAMPLE_ARTICLE_DICT, SAMPLE_ARTICLE_PUBLISHED],
            source="test",
        )

        assert feed[0].title == "Markets Rally on Fed Decision"
        assert feed[1].title == "Tech Earnings Beat"

    def test_repr_html_returns_table(self):
        """Verify _repr_html_ returns an HTML table."""
        feed = NewsFeed.from_dicts([SAMPLE_ARTICLE_DICT], source="cnbc")
        html_str = feed._repr_html_()  # pylint: disable=protected-access

        assert "<table" in html_str
        assert "Markets Rally on Fed Decision" in html_str
        assert "1 articles" in html_str


# ---------------------------------------------------------------------------
# NewsFeed serialization tests
# ---------------------------------------------------------------------------


class TestNewsFeedSerialization:
    """Tests for NewsFeed.to_json(), to_csv(), to_dataframe()."""

    def test_to_json_returns_array(self):
        """Verify to_json returns a JSON array of article dicts."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        result = feed.to_json()
        parsed = json.loads(result)

        assert isinstance(parsed, list)
        assert len(parsed) == 3
        assert parsed[0]["title"] == "Markets Rally on Fed Decision"

    def test_to_json_indent(self):
        """Verify indent kwarg is passed through."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        result = feed.to_json(indent=4)

        assert "    " in result

    def test_to_csv_has_header(self):
        """Verify CSV output starts with a header row."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        result = feed.to_csv()
        reader = csv.reader(io.StringIO(result))
        header = next(reader)

        assert header == ["title", "link", "description", "published", "source"]

    def test_to_csv_has_all_rows(self):
        """Verify CSV has one row per article plus header."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        result = feed.to_csv()
        lines = result.strip().split("\n")

        assert len(lines) == 4  # header + 3 articles

    def test_to_csv_content(self):
        """Verify CSV row content matches article data."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        result = feed.to_csv()
        reader = csv.reader(io.StringIO(result))
        next(reader)  # skip header
        first_row = next(reader)

        assert first_row[0] == "Markets Rally on Fed Decision"
        assert first_row[4] == "test"

    def test_to_dataframe_requires_pandas(self):
        """Verify to_dataframe raises ImportError when pandas is missing."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")

        with patch.dict("sys.modules", {"pandas": None}):
            with pytest.raises(ImportError, match="pip install fin-news"):
                feed.to_dataframe()

    def test_to_dataframe_returns_dataframe(self):
        """Verify to_dataframe returns a DataFrame when pandas is available."""

        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        df = feed.to_dataframe()

        assert len(df) == 3
        assert "title" in df.columns
        assert "source" in df.columns

    def test_empty_feed_to_json(self):
        """Verify empty feed serializes to empty JSON array."""
        feed = NewsFeed.from_dicts([])

        assert feed.to_json() == "[]"

    def test_empty_feed_to_csv(self):
        """Verify empty feed CSV has only the header row."""
        feed = NewsFeed.from_dicts([])
        result = feed.to_csv()
        lines = result.strip().split("\n")

        assert len(lines) == 1


# ---------------------------------------------------------------------------
# NewsFeed.filter() tests
# ---------------------------------------------------------------------------


class TestNewsFeedFilter:
    """Tests for NewsFeed.filter() with since, until, max_results."""

    def test_max_results(self):
        """Verify max_results limits article count."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        filtered = feed.filter(max_results=2)

        assert len(filtered) == 2
        assert filtered[0].title == "Markets Rally on Fed Decision"

    def test_max_results_larger_than_feed(self):
        """Verify max_results > len returns all articles."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        filtered = feed.filter(max_results=100)

        assert len(filtered) == 3

    def test_since_filter(self):
        """Verify since keeps only articles published at or after the date."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        cutoff = datetime(2026, 4, 18, 0, 0, 0, tzinfo=timezone.utc)
        filtered = feed.filter(since=cutoff)

        assert len(filtered) == 2
        titles = [a.title for a in filtered]
        assert "Markets Rally on Fed Decision" in titles
        assert "Tech Earnings Beat Expectations" in titles

    def test_until_filter(self):
        """Verify until keeps only articles published at or before the date."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        cutoff = datetime(2026, 4, 18, 0, 0, 0, tzinfo=timezone.utc)
        filtered = feed.filter(until=cutoff)

        assert len(filtered) == 1
        assert filtered[0].title == "Oil Prices Surge"

    def test_since_and_until_combined(self):
        """Verify both since and until can be used together."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        since = datetime(2026, 4, 17, 12, 0, 0, tzinfo=timezone.utc)
        until = datetime(2026, 4, 19, 0, 0, 0, tzinfo=timezone.utc)
        filtered = feed.filter(since=since, until=until)

        assert len(filtered) == 1
        assert filtered[0].title == "Tech Earnings Beat Expectations"

    def test_filter_with_max_results_after_date(self):
        """Verify max_results applies after date filtering."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        cutoff = datetime(2026, 4, 17, 0, 0, 0, tzinfo=timezone.utc)
        filtered = feed.filter(since=cutoff, max_results=1)

        assert len(filtered) == 1

    def test_filter_keeps_unparseable_dates(self):
        """Verify articles with invalid dates are kept, not dropped."""
        items = [
            {"title": "No date", "link": "https://example.com/x"},
            ARTICLES[0],
        ]
        feed = NewsFeed.from_dicts(items, source="test")
        cutoff = datetime(2026, 4, 20, 0, 0, 0, tzinfo=timezone.utc)
        filtered = feed.filter(since=cutoff)

        assert len(filtered) == 1
        assert filtered[0].title == "No date"

    def test_filter_naive_datetime_treated_as_utc(self):
        """Verify naive datetimes are treated as UTC."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        cutoff = datetime(2026, 4, 18, 0, 0, 0)  # no tzinfo
        filtered = feed.filter(since=cutoff)

        assert len(filtered) == 2

    def test_filter_returns_new_feed(self):
        """Verify filter returns a new NewsFeed, not a mutation."""
        feed = NewsFeed.from_dicts(ARTICLES, source="test")
        filtered = feed.filter(max_results=1)

        assert filtered is not feed
        assert len(feed) == 3
        assert filtered.source == feed.source
