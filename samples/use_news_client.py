from pprint import pprint
from finnews.client import News
from finnews.news_enum import cnbc_investing

# Create a new instance of the News Client.
news_client = News()

# Grab the CNBC News Client.
cnbc_client = news_client.cnbc

# Grab all the investing articles.
investing_articles = cnbc_client.investing_feeds(topic='investing')

# Grab all the personal finance articles.
personal_finance_articles = cnbc_client.investing_feeds(topic=cnbc_investing.PERSONAL_FINANCE)

# Grab the S&P Global News Client.
sp_global_client = news_client.sp_global

# Grab the research articles.
research_articles = sp_global_client.research()

pprint(research_articles)