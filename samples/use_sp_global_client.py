"""Sample script demonstrating the S&P Global news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed

# Create a new instance of the News Client.
news_client = News()

# Grab the SPGlobal News Client.
sp_global_client = news_client.sp_global

# ---------------------------------------------------------------------------
# Section: List available feeds.
# ---------------------------------------------------------------------------

# Print the available feed methods.
print("Available feeds:", sp_global_client.feeds)

# ---------------------------------------------------------------------------
# Section: Fetch a feed and wrap in structured models.
# ---------------------------------------------------------------------------

# Grab the Research Feed.
research = sp_global_client.research()

# Wrap the results in a NewsFeed.
feed = NewsFeed.from_dicts(research, source='sp_global')
print(f"\nResearch articles: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# Convert a single result to a NewsArticle.
if research:
    article = NewsArticle.from_dict(research[0], source='sp_global')
    print(f"\nFirst article: {article.title}")
    print(f"  Link: {article.link}")

# ---------------------------------------------------------------------------
# Section: Fetch additional feeds.
# ---------------------------------------------------------------------------

# Grab the Methodologies Feed.
methodologies = sp_global_client.methodologies()
pprint(methodologies)

# Grab the All Indices Feed.
all_indices = sp_global_client.all_indices()
pprint(all_indices)

# Grab the Market Commentary Feed.
market_commentary = sp_global_client.market_commentary()
pprint(market_commentary)

# Grab the Education Feed.
education = sp_global_client.education()
pprint(education)

# Grab the Performance Reports Feed.
performance_reports = sp_global_client.performance_reports()
pprint(performance_reports)

# Grab the SPIVA Feed.
spiva = sp_global_client.spiva()
pprint(spiva)

# Grab the Index TV Feed.
index_tv = sp_global_client.index_tv()
pprint(index_tv)

# Grab the Corporate News Feed.
corporate_news = sp_global_client.corporate_news()
pprint(corporate_news)

# Grab the Index Launches Feed.
index_launches = sp_global_client.index_launches()
pprint(index_launches)

# Grab the Index Announcements Feed.
index_announcements = sp_global_client.index_announcements()
pprint(index_announcements)

# Grab the New Consultations Feed.
new_consultations = sp_global_client.new_consultations()
pprint(new_consultations)

# Grab the Daily Index Insights Feed.
daily_index_insights = sp_global_client.daily_index_insights()
pprint(daily_index_insights)

# Grab the S&P CoreLogic Case-Shiller Home Price Indices Feed.
case_shiller = sp_global_client.case_shiller_home_price_indices()
pprint(case_shiller)
