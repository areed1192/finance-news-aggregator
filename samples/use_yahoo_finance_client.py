from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the Yahoo Finance News Client.
yahoo_finance_client = news_client.yahoo_finance

# Grab the News Feed.
content = yahoo_finance_client.news()
pprint(content)

# Grab the headlines for Microsoft (MSFT) and Google (GOOG)
content = yahoo_finance_client.headlines(symbols=['MSFT', 'GOOG'])
pprint(content)
