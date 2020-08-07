from pprint import pprint
from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the MarketWatch News Client.
market_watch_client = news_client.market_Watch

# Grab the original content news.
content = market_watch_client.top_stories()
pprint(content)

# Grab the original content news.
content = market_watch_client.real_time_headlines()
pprint(content)

# Grab the Market Pulse Feed.
content = market_watch_client.market_pulse()
pprint(content)

# Grab the Bulletins
content = market_watch_client.bulletins()
pprint(content)

# Grab the Personal Finance
content = market_watch_client.personal_finance()
pprint(content)

# Grab the Stocks to Watch
content = market_watch_client.stocks_to_watch()
pprint(content)

# Grab the Internet Stories
content = market_watch_client.internet_stories()
pprint(content)

# Grab the Mutual Funds Feed
content = market_watch_client.mutual_funds()
pprint(content)

# Grab the Software Stories Feed
content = market_watch_client.software_stories()
pprint(content)

# Grab the Banking & Finance Feed
content = market_watch_client.banking_and_finance()
pprint(content)

# Grab the Commentary Feed
content = market_watch_client.commentary()
pprint(content)

# Grab the Newsletter & Research Feed
content = market_watch_client.newsletter_and_research()
pprint(content)

# Grab the Newsletter & Research Feed
content = market_watch_client.auto_reviews()
pprint(content)
