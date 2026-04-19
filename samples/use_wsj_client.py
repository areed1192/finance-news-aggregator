"""Sample script demonstrating the Wall Street Journal news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed

# Create a new instance of the News Client.
news_client = News()

# Grab the Wall Street Journal News Client.
wsj_client = news_client.wsj

# ---------------------------------------------------------------------------
# Section: List available feeds.
# ---------------------------------------------------------------------------

# Print the available feed methods.
print("Available feeds:", wsj_client.feeds)

# ---------------------------------------------------------------------------
# Section: Fetch a feed and wrap in structured models.
# ---------------------------------------------------------------------------

# Grab the Market News Feed.
market_news = wsj_client.market_news()

# Wrap the results in a NewsFeed.
feed = NewsFeed.from_dicts(market_news, source='wsj')
print(f"\nMarket news articles: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# Convert a single result to a NewsArticle.
if market_news:
    article = NewsArticle.from_dict(market_news[0], source='wsj')
    print(f"\nFirst article: {article.title}")
    print(f"  Link: {article.link}")

# ---------------------------------------------------------------------------
# Section: Fetch additional feeds.
# ---------------------------------------------------------------------------

# Grab the Opinions Feed.
opinions = wsj_client.opinions()
pprint(opinions)

# Grab the World News Feed.
world_news = wsj_client.world_news()
pprint(world_news)

# Grab the US Business News Feed.
us_business_news = wsj_client.us_business_news()
pprint(us_business_news)

# Grab the Technology News Feed.
technology_news = wsj_client.technology_news()
pprint(technology_news)

# Grab the Lifestyle Feed.
lifestyle = wsj_client.lifestyle()
pprint(lifestyle)
