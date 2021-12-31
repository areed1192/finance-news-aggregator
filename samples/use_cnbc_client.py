
from finnews.client import News
from finnews.news_enum import cnbc_top_news
from finnews.news_enum import cnbc_tv_programs_asia

# Create a new instance of the News Client.
news_client = News()

# Grab the CNBC News Client.
cnbc_news_client = news_client.cnbc

# Grab the top news.
cbnc_top_news = cnbc_news_client.news_feed(
    topic='top_news'
)

# Grab the top news, using enums.
cnbc_real_estate_news = cnbc_news_client.news_feed(
    topic=cnbc_top_news.REAL_ESTATE
)

# Grab the investing news, from the Investment Feed.
cnbc_investing_news = cnbc_news_client.investing_feeds(
    topic='investing'
)

# Grab the blog news, from the Blog Feed.
cnbc_blog_news = cnbc_news_client.blogs(
    topic='charting_asia'
)

# Grab the video and tv news, from the Video & TV Feed.
cnbc_tv_and_video_news = cnbc_news_client.videos_and_tv(
    topic='top_video'
)

# Grab the video and tv news, from the Europe News Feed.
cnbc_tv_europe_news = cnbc_news_client.tv_programs_europe(
    topic='capital_connection'
)

# Grab the video and tv news, from the Asia News Feed.
cnbc_tv_asia_news = cnbc_news_client.tv_programs_asia(
    topic=cnbc_tv_programs_asia.SQUAWK_BOX_ASIA
)

# Grab all the news feeds.
cnbc_all_news_feeds = cnbc_news_client.all_feeds()

# Save the data.
news_client.save_to_file(
    content=cnbc_all_news_feeds,
    file_name='cnbc_all_news_feeds'
)
