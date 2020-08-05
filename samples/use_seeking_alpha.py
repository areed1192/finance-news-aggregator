from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the Seeking Alpha News Client.
seeking_alpha_client = news_client.seeking_alpha

# Grab the news for TSLA (Tesla).
content = seeking_alpha_client.stocks(ticker='TSLA')
pprint(content)

# Grab the Latest Articles Feed.
content = seeking_alpha_client.latest_articles()
pprint(content)

# Grab the IPO Analysis Feed.
content = seeking_alpha_client.ipo_analysis()
pprint(content)

# Grab the Long Ideas Feed.
content = seeking_alpha_client.long_ideas()
pprint(content)

# Grab the Transcripts Feed.
content = seeking_alpha_client.transcripts()
pprint(content)

# Grab the All News Feed.
content = seeking_alpha_client.all_news()
pprint(content)

# Grab the Wall Street Breakfast Feed.
content = seeking_alpha_client.wall_street_breakfast()
pprint(content)

# Grab the Most Popular Articles Feed.
content = seeking_alpha_client.most_popular_articles()
pprint(content)

# Grab the Forex Articles Feed.
content = seeking_alpha_client.forex()
pprint(content)

# Grab the Editor Picks Articles Feed.
content = seeking_alpha_client.editors_picks()
pprint(content)

# Grab the ETFs Feed.
content = seeking_alpha_client.etfs()
pprint(content)

# Grab the France Global Market Feed.
content = seeking_alpha_client.global_markets(country='france')
pprint(content)

# Grab the France Global Market Feed.
content = seeking_alpha_client.sectors(sector='financial')
pprint(content)
