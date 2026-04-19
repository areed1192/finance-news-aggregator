"""Sample script demonstrating the MarketWatch news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsFeed
from finnews.news_enum import MarketWatch as MarketWatchEnum

# Create a new instance of the News Client.
news_client = News()

# Grab the MarketWatch News Client.
market_watch_client = news_client.market_watch

# ---------------------------------------------------------------------------
# Section: List available topics.
# ---------------------------------------------------------------------------

# Print the available topic categories.
print("Available topics:", market_watch_client.topics)

# ---------------------------------------------------------------------------
# Section: Fetch feeds and wrap in structured models.
# ---------------------------------------------------------------------------

# Grab the Top Stories Feed.
top_stories = market_watch_client.top_stories()
pprint(top_stories)

# Wrap the results in a structured NewsFeed.
feed = NewsFeed.from_dicts(top_stories, source='market_watch')
print(f"\nTop stories: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# Show enum usage.
print(f"\nMarketWatch enum example: {MarketWatchEnum.TOP_STORIES}")

# ---------------------------------------------------------------------------
# Section: Fetch additional feeds.
# ---------------------------------------------------------------------------

# Grab the Real Time Headlines Feed.
real_time_headlines = market_watch_client.real_time_headlines()
pprint(real_time_headlines)

# Grab the Market Pulse Feed.
market_pulse = market_watch_client.market_pulse()
pprint(market_pulse)

# Grab the Breaking News Bulletins Feed.
bulletins = market_watch_client.bulletins()
pprint(bulletins)

# ---------------------------------------------------------------------------
# Section: Fetch all feeds at once.
# ---------------------------------------------------------------------------

# Grab all available feeds.
all_feeds = market_watch_client.all_feeds()
pprint(list(all_feeds.keys()))
