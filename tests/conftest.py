"""Shared fixtures and sample data for the finnews test suite."""

import pytest

from finnews.client import News


# ---------------------------------------------------------------------------
# Sample RSS XML
# ---------------------------------------------------------------------------

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

MALFORMED_XML = b"""<rss><channel><item><title>Broken"""

SAMPLE_RSS_DUPLICATE_TAGS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <item>
      <title>Article</title>
      <link>https://example.com/article</link>
      <category>Finance</category>
      <category>Markets</category>
      <category>Stocks</category>
    </item>
  </channel>
</rss>
"""

SAMPLE_CACHE_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <item>
      <title>Cached Article</title>
      <link>https://example.com/cached</link>
    </item>
  </channel>
</rss>"""


# ---------------------------------------------------------------------------
# Sample article dictionaries
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

ARTICLES = [
    {
        "title": "Markets Rally on Fed Decision",
        "link": "https://example.com/1",
        "description": "Stocks climbed after the Fed held rates.",
        "pubDate": "Sat, 19 Apr 2026 14:00:00 +0000",
        "category": "Markets",
    },
    {
        "title": "Tech Earnings Beat Expectations",
        "link": "https://example.com/2",
        "description": "Major tech firms reported strong Q1.",
        "pubDate": "Fri, 18 Apr 2026 09:00:00 +0000",
    },
    {
        "title": "Oil Prices Surge",
        "link": "https://example.com/3",
        "description": "Crude oil hit a 6-month high.",
        "pubDate": "Thu, 17 Apr 2026 06:00:00 +0000",
    },
]


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def news_client():
    """Create a fresh News client."""
    return News()


@pytest.fixture()
def news_client_cached():
    """Create a News client with TTL caching enabled."""
    return News(cache_ttl=120)
