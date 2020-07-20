from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the CNBC News Client.
cnbc_news_client = news_client.cnbc

# Grab the top news.
cbnc_top_news = cnbc_news_client.news_feed(topic='top_news')

# Save the data.
news_client.save_to_file(content=cbnc_top_news, file_name='cnbc_top_news')

# print it.
pprint(cbnc_top_news)