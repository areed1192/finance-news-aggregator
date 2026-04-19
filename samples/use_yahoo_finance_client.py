"""Sample script demonstrating the Yahoo Finance news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed

# Create a new instance of the News Client.
news_client = News()

# Grab the Yahoo Finance News Client.
yahoo_finance_client = news_client.yahoo_finance

# ---------------------------------------------------------------------------
# Section: List available feeds.
# ---------------------------------------------------------------------------

# Print the available feed methods.
print("Available feeds:", yahoo_finance_client.feeds)

# ---------------------------------------------------------------------------
# Section: Fetch a feed and wrap in structured models.
# ---------------------------------------------------------------------------

# Grab the News Feed.
news = yahoo_finance_client.news()

# Wrap the results in a NewsFeed.
feed = NewsFeed.from_dicts(news, source='yahoo_finance')
print(f"\nYahoo Finance articles: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# Convert a single result to a NewsArticle.
if news:
    article = NewsArticle.from_dict(news[0], source='yahoo_finance')
    print(f"\nFirst article: {article.title}")
    print(f"  Link: {article.link}")

# ---------------------------------------------------------------------------
# Section: Fetch headlines for specific symbols.
# ---------------------------------------------------------------------------

# Grab the headlines for Microsoft (MSFT) and Google (GOOG).
headlines = yahoo_finance_client.headlines(symbols=['MSFT', 'GOOG'])
pprint(headlines)
