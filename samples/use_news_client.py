"""Sample script demonstrating the unified News client with enum support."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed
from finnews.news_enum import CNBCInvesting

# Create a new instance of the News Client.
news_client = News()

# ---------------------------------------------------------------------------
# Section: CNBC — enum-based topic selection.
# ---------------------------------------------------------------------------

# Grab the CNBC News Client.
cnbc_client = news_client.cnbc

# List available topics.
print("CNBC topics:", cnbc_client.topics)

# Grab all the investing articles by string key.
investing_articles = cnbc_client.investing_feeds(topic='investing')

# Grab personal finance articles using the enum.
personal_finance_articles = cnbc_client.investing_feeds(
    topic=CNBCInvesting.PERSONAL_FINANCE
)

# Wrap raw results into structured models.
feed = NewsFeed.from_dicts(personal_finance_articles, source='cnbc')
print(f"\nPersonal finance articles: {len(feed)}")
for article in feed:
    print(f"  - {article.title}")

# ---------------------------------------------------------------------------
# Section: S&P Global — feeds property and NewsArticle.
# ---------------------------------------------------------------------------

# Grab the S&P Global News Client.
sp_global_client = news_client.sp_global

# List available feed methods.
print("\nS&P Global feeds:", sp_global_client.feeds)

# Grab the research articles.
research_articles = sp_global_client.research()

# Convert the first result to a NewsArticle.
if research_articles:
    article = NewsArticle.from_dict(research_articles[0], source='sp_global')
    print(f"\nFirst research article: {article.title}")
    print(f"  Link: {article.link}")

pprint(research_articles)
