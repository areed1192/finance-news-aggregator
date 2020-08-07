from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the Wall Street Journal News Client.
wsj_client = news_client.wsj

# Grab the Opinions Feed.
content = wsj_client.opinions()
pprint(content)

# Grab the World News Feed.
content = wsj_client.world_news()
pprint(content)

# Grab the US Business News Feed.
content = wsj_client.us_business_news()
pprint(content)

# Grab the Market News Feed.
content = wsj_client.market_news()
pprint(content)

# Grab the Technology News Feed.
content = wsj_client.technology_news()
pprint(content)

# Grab the Technology News Feed.
content = wsj_client.lifestyle()
pprint(content)