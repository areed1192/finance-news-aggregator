"""Sample: Phase 4 features — serialization, filtering, caching, and async."""

from datetime import datetime, timezone

from finnews.client import News
from finnews.article import NewsFeed

# Create a News Client with 5-minute response caching enabled.
news_client = News(cache_ttl=300)

# Grab the CNBC News Client (parser inherits the 300s TTL).
cnbc_client = news_client.cnbc

# ---------------------------------------------------------------------------
# Section: Fetch articles and wrap in structured models.
# ---------------------------------------------------------------------------

# Fetch the raw article dicts.
raw_articles = cnbc_client.news_feed(topic='top_news')

# Wrap them in a NewsFeed for structured access.
feed = NewsFeed.from_dicts(raw_articles, source='cnbc')
print(f"Fetched {len(feed)} articles from CNBC top news.\n")

# ---------------------------------------------------------------------------
# Section: to_json() — serialize the feed to JSON.
# ---------------------------------------------------------------------------

json_str = feed.to_json(indent=2)
print("=== JSON (first 500 chars) ===")
print(json_str[:500])
print()

# ---------------------------------------------------------------------------
# Section: to_csv() — serialize the feed to CSV.
# ---------------------------------------------------------------------------

csv_str = feed.to_csv()
print("=== CSV (first 500 chars) ===")
print(csv_str[:500])
print()

# ---------------------------------------------------------------------------
# Section: Single article serialization.
# ---------------------------------------------------------------------------

if len(feed) > 0:
    first_article = feed[0]
    print("=== Single article as JSON ===")
    print(first_article.to_json(indent=2))
    print()

# ---------------------------------------------------------------------------
# Section: filter() — limit results by count.
# ---------------------------------------------------------------------------

top_3 = feed.filter(max_results=3)
print(f"=== Top 3 articles (max_results=3) — got {len(top_3)} ===")
for article in top_3:
    print(f"  - {article.title}")
print()

# ---------------------------------------------------------------------------
# Section: filter() — date-range filtering with since/until.
# ---------------------------------------------------------------------------

# Keep only articles from the last 24 hours (example cutoff).
yesterday = datetime(2026, 4, 18, 0, 0, 0, tzinfo=timezone.utc)
recent = feed.filter(since=yesterday)
print(f"=== Articles since {yesterday.date()} — got {len(recent)} ===")
for article in recent:
    print(f"  - {article.title} ({article.published})")
print()

# Combine date filtering with max_results.
recent_top_2 = feed.filter(since=yesterday, max_results=2)
print(f"=== Recent top 2 — got {len(recent_top_2)} ===")
for article in recent_top_2:
    print(f"  - {article.title}")
print()

# ---------------------------------------------------------------------------
# Section: TTL caching — second call is served from cache.
# ---------------------------------------------------------------------------

# This call reuses the cached response (no HTTP request).
raw_articles_cached = cnbc_client.news_feed(topic='top_news')
print(f"Cached call returned {len(raw_articles_cached)} articles (same data, no HTTP).\n")

# ---------------------------------------------------------------------------
# Section: to_dataframe() — optional pandas integration.
# ---------------------------------------------------------------------------

try:
    df = feed.to_dataframe()
    print("=== DataFrame (first 3 rows) ===")
    print(df[['title', 'published', 'source']].head(3).to_string(index=False))
    print()
except ImportError:
    print("pandas not installed — skipping to_dataframe() demo.")
    print("Install with: pip install fin-news[pandas]\n")

# ---------------------------------------------------------------------------
# Section: Save output.
# ---------------------------------------------------------------------------

news_client.save_to_file(
    content=raw_articles,
    file_name='cnbc_phase4_demo'
)
print("Saved results to samples/responses/cnbc_phase4_demo.jsonc")
