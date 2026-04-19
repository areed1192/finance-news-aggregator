"""Sample script demonstrating the CNBC news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed
from finnews.news_enum import CNBCTopNews
from finnews.news_enum import CNBCTVProgramsAsia

# Create a new instance of the News Client.
news_client = News()

# Grab the CNBC News Client.
cnbc_news_client = news_client.cnbc

# ---------------------------------------------------------------------------
# Section: List available topics.
# ---------------------------------------------------------------------------

# Print the available topic categories.
print("Available topics:", cnbc_news_client.topics)

# ---------------------------------------------------------------------------
# Section: Fetch news by string topic and by enum.
# ---------------------------------------------------------------------------

# Grab the top news by string key.
top_news = cnbc_news_client.news_feed(topic='top_news')
pprint(top_news)

# Grab real estate news using the enum.
real_estate_news = cnbc_news_client.news_feed(
    topic=CNBCTopNews.REAL_ESTATE
)

# Wrap the results in structured NewsArticle models.
feed = NewsFeed.from_dicts(real_estate_news, source='cnbc')
print(f"\nReal estate articles: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# ---------------------------------------------------------------------------
# Section: Fetch from other feed categories.
# ---------------------------------------------------------------------------

# Grab the investing news, from the Investment Feed.
investing_news = cnbc_news_client.investing_feeds(topic='investing')

# Grab the blog news, from the Blog Feed.
blog_news = cnbc_news_client.blogs(topic='charting_asia')

# Grab the video and tv news, from the Video & TV Feed.
tv_and_video_news = cnbc_news_client.videos_and_tv(topic='top_video')

# Grab the TV news from the Europe News Feed.
tv_europe_news = cnbc_news_client.tv_programs_europe(
    topic='capital_connection'
)

# Grab the TV news from the Asia Feed, using an enum.
tv_asia_news = cnbc_news_client.tv_programs_asia(
    topic=CNBCTVProgramsAsia.SQUAWK_BOX_ASIA
)

# ---------------------------------------------------------------------------
# Section: Structured article model.
# ---------------------------------------------------------------------------

# Convert a single raw dictionary into a NewsArticle.
if top_news:
    article = NewsArticle.from_dict(top_news[0], source='cnbc')
    print(f"\nFirst article: {article.title}")
    print(f"  Link: {article.link}")
    print(f"  Published: {article.published}")

# ---------------------------------------------------------------------------
# Section: Save results.
# ---------------------------------------------------------------------------

# Grab all the news feeds.
all_feeds = cnbc_news_client.all_feeds()

# Save the data.
news_client.save_to_file(
    content=all_feeds,
    file_name='cnbc_all_news_feeds'
)
