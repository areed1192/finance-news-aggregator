"""Structured data models for news articles and feed collections."""

from __future__ import annotations

import csv
import html
import io
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime


@dataclass
class NewsArticle:
    """A single news article parsed from an RSS feed.

    ### Attributes:
    ----
    title (str): The article headline.
    link (str): URL to the full article.
    description (str): Summary or excerpt text.
    published (str): Publication date string from the feed.
    source (str): The news provider name (e.g. 'cnbc', 'nasdaq').
    extra (dict): Any additional fields from the RSS item that
        don't map to the standard attributes above.
    """

    title: str = ""
    link: str = ""
    description: str = ""
    published: str = ""
    source: str = ""
    extra: dict = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict, source: str = "") -> NewsArticle:
        """Create a ``NewsArticle`` from a raw parsed dictionary.

        Maps common RSS tag names (``title``, ``link``, ``description``,
        ``pubDate``, ``published``) to the dataclass fields. Remaining
        keys are stored in ``extra``.

        ### Arguments:
        ----
        data (dict): A single article dictionary as returned by
            ``NewsParser.parse_response``.
        source (str): The provider name to attach.

        ### Returns:
        ----
        NewsArticle: A populated article instance.
        """

        known_keys = {"title", "link", "description", "pubDate", "published"}
        extra = {k: v for k, v in data.items() if k not in known_keys}

        return cls(
            title=data.get("title", ""),
            link=data.get("link", ""),
            description=data.get("description", ""),
            published=data.get("pubDate", data.get("published", "")),
            source=source,
            extra=extra,
        )

    def _repr_html_(self) -> str:
        """Jupyter-friendly HTML representation of the article.

        ### Returns:
        ----
        str: An HTML string suitable for ``IPython.display``.
        """

        safe_title = html.escape(self.title)
        safe_link = html.escape(self.link)
        safe_desc = html.escape(self.description)
        safe_source = html.escape(self.source)
        safe_pub = html.escape(self.published)

        return (
            '<div style="border:1px solid #ddd;padding:10px;margin:6px 0;'
            'border-radius:4px;font-family:sans-serif">'
            f'<h4 style="margin:0 0 4px"><a href="{safe_link}">{safe_title}</a></h4>'
            f'<p style="margin:0 0 4px;color:#555;font-size:0.9em">{safe_desc}</p>'
            f'<small style="color:#888">{safe_source} &middot; {safe_pub}</small>'
            '</div>'
        )

    def to_dict(self) -> dict:
        """Convert to a plain dictionary.

        Standard fields are at the top level.  Extra fields are merged in.

        ### Returns:
        ----
        dict: A flat dictionary of all article data.
        """

        base = {
            "title": self.title,
            "link": self.link,
            "description": self.description,
            "published": self.published,
            "source": self.source,
        }
        base.update(self.extra)
        return base

    def to_json(self, **kwargs) -> str:
        """Serialize to a JSON string.

        ### Arguments:
        ----
        **kwargs: Additional keyword arguments passed to ``json.dumps``.

        ### Returns:
        ----
        str: A JSON string representation of the article.
        """

        return json.dumps(self.to_dict(), **kwargs)


@dataclass
class NewsFeed:
    """A collection of news articles from a single feed request.

    ### Attributes:
    ----
    articles (list[NewsArticle]): The parsed articles.
    source (str): The news provider name.
    """

    articles: list[NewsArticle] = field(default_factory=list)
    source: str = ""

    @classmethod
    def from_dicts(cls, items: list[dict], source: str = "") -> NewsFeed:
        """Create a ``NewsFeed`` from a list of raw dictionaries.

        ### Arguments:
        ----
        items (list[dict]): Article dictionaries as returned by
            ``NewsParser.parse_response``.
        source (str): The provider name to attach.

        ### Returns:
        ----
        NewsFeed: A populated feed collection.
        """

        articles = [NewsArticle.from_dict(d, source=source) for d in items]
        return cls(articles=articles, source=source)

    def _repr_html_(self) -> str:
        """Jupyter-friendly HTML table of all articles in the feed.

        ### Returns:
        ----
        str: An HTML table string.
        """

        safe_source = html.escape(self.source)
        rows = []
        for art in self.articles:
            safe_title = html.escape(art.title)
            safe_link = html.escape(art.link)
            safe_pub = html.escape(art.published)
            rows.append(
                f'<tr><td><a href="{safe_link}">{safe_title}</a></td>'
                f'<td>{safe_pub}</td></tr>'
            )
        body = "\n".join(rows)

        return (
            f'<h3>{safe_source} Feed ({len(self.articles)} articles)</h3>'
            '<table style="border-collapse:collapse;width:100%;font-family:sans-serif">'
            '<thead><tr>'
            '<th style="text-align:left;border-bottom:2px solid #ddd;padding:6px">Title</th>'
            '<th style="text-align:left;border-bottom:2px solid #ddd;padding:6px">Published</th>'
            '</tr></thead>'
            f'<tbody>{body}</tbody></table>'
        )

    def to_json(self, **kwargs) -> str:
        """Serialize the feed to a JSON string.

        ### Arguments:
        ----
        **kwargs: Additional keyword arguments passed to ``json.dumps``
            (e.g. ``indent=2``).

        ### Returns:
        ----
        str: A JSON array of article dictionaries.
        """

        return json.dumps(
            [art.to_dict() for art in self.articles], **kwargs
        )

    def to_csv(self) -> str:
        """Serialize the feed to a CSV string.

        Columns: title, link, description, published, source.

        ### Returns:
        ----
        str: A CSV-formatted string with a header row.
        """

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["title", "link", "description", "published", "source"])
        for art in self.articles:
            writer.writerow([
                art.title, art.link, art.description,
                art.published, art.source,
            ])
        return output.getvalue()

    def to_dataframe(self):
        """Convert to a ``pandas.DataFrame``.

        Requires ``pandas``: ``pip install fin-news[pandas]``

        ### Returns:
        ----
        pandas.DataFrame: A DataFrame with one row per article.

        ### Raises:
        ----
        ImportError: If pandas is not installed.
        """

        try:
            import pandas as pd  # pylint: disable=import-outside-toplevel
        except ImportError as exc:
            raise ImportError(
                "pandas is required for to_dataframe(). "
                "Install it with: pip install fin-news[pandas]"
            ) from exc

        return pd.DataFrame([art.to_dict() for art in self.articles])

    def filter(
        self,
        *,
        since: datetime | None = None,
        until: datetime | None = None,
        max_results: int | None = None,
    ) -> NewsFeed:
        """Return a new ``NewsFeed`` filtered by date range and/or count.

        Articles whose ``published`` date cannot be parsed are always
        kept (never silently dropped).

        ### Arguments:
        ----
        since (datetime | None): Keep articles published at or after
            this time.  Naive datetimes are treated as UTC.
        until (datetime | None): Keep articles published at or before
            this time.  Naive datetimes are treated as UTC.
        max_results (int | None): Maximum number of articles to return
            after date filtering.

        ### Returns:
        ----
        NewsFeed: A new feed containing only the matching articles.
        """

        if since is not None and since.tzinfo is None:
            since = since.replace(tzinfo=timezone.utc)
        if until is not None and until.tzinfo is None:
            until = until.replace(tzinfo=timezone.utc)

        filtered = list(self.articles)

        if since is not None or until is not None:
            result = []
            for art in filtered:
                try:
                    pub_dt = parsedate_to_datetime(art.published)
                except (TypeError, ValueError):
                    result.append(art)
                    continue
                if since is not None and pub_dt < since:
                    continue
                if until is not None and pub_dt > until:
                    continue
                result.append(art)
            filtered = result

        if max_results is not None:
            filtered = filtered[:max_results]

        return NewsFeed(articles=filtered, source=self.source)

    def __len__(self) -> int:
        return len(self.articles)

    def __iter__(self):
        return iter(self.articles)

    def __getitem__(self, index):
        return self.articles[index]
