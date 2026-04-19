"""Sample script demonstrating the Seeking Alpha news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed

# Create a new instance of the News Client.
news_client = News()

# Grab the Seeking Alpha News Client.
seeking_alpha_client = news_client.seeking_alpha

# ---------------------------------------------------------------------------
# Section: List available feeds.
# ---------------------------------------------------------------------------

# Print the available feed methods.
print("Available feeds:", seeking_alpha_client.feeds)

# ---------------------------------------------------------------------------
# Section: Fetch a feed and wrap in structured models.
# ---------------------------------------------------------------------------

# Grab the Latest Articles Feed.
latest_articles = seeking_alpha_client.latest_articles()

# Wrap the results in a NewsFeed.
feed = NewsFeed.from_dicts(latest_articles, source='seeking_alpha')
print(f"\nLatest articles: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# Convert a single result to a NewsArticle.
if latest_articles:
    article = NewsArticle.from_dict(latest_articles[0], source='seeking_alpha')
    print(f"\nFirst article: {article.title}")
    print(f"  Link: {article.link}")

# ---------------------------------------------------------------------------
# Section: Fetch stock-specific and category feeds.
# ---------------------------------------------------------------------------

# Grab the news for TSLA (Tesla).
tsla_news = seeking_alpha_client.stocks(ticker='TSLA')
pprint(tsla_news)

# Grab the IPO Analysis Feed.
ipo_analysis = seeking_alpha_client.ipo_analysis()
pprint(ipo_analysis)

# Grab the Long Ideas Feed.
long_ideas = seeking_alpha_client.long_ideas()
pprint(long_ideas)

# Grab the Transcripts Feed.
transcripts = seeking_alpha_client.transcripts()
pprint(transcripts)

# Grab the All News Feed.
all_news = seeking_alpha_client.all_news()
pprint(all_news)

# Grab the Wall Street Breakfast Feed.
wall_street_breakfast = seeking_alpha_client.wall_street_breakfast()
pprint(wall_street_breakfast)

# Grab the Most Popular Articles Feed.
most_popular = seeking_alpha_client.most_popular_articles()
pprint(most_popular)

# Grab the Forex Articles Feed.
forex = seeking_alpha_client.forex()
pprint(forex)

# Grab the Editor Picks Articles Feed.
editors_picks = seeking_alpha_client.editors_picks()
pprint(editors_picks)

# Grab the ETFs Feed.
etfs = seeking_alpha_client.etfs()
pprint(etfs)

# Grab the France Global Market Feed.
france_markets = seeking_alpha_client.global_markets(country='france')
pprint(france_markets)

# Grab the Financial Sector Feed.
financial_sector = seeking_alpha_client.sectors(sector='financial')
pprint(financial_sector)
