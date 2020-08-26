from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the NASDAQ News Client.
nasdaq_news_client = news_client.nasdaq

# Grab the original content news.
content = nasdaq_news_client.original_content()
pprint(content)

# Grab the Commodity news.
content = nasdaq_news_client.commodities_feed()
pprint(content)

# Grab the IPO news.
content = nasdaq_news_client.ipos_feed()
pprint(content)

# Grab the Cryptocurrency news.
content = nasdaq_news_client.cryptocurrency_feed()
pprint(content)

# Grab the Dividends news.
content = nasdaq_news_client.dividends_feed()
pprint(content)

# Grab the Earnings news.
content = nasdaq_news_client.earnings_feed()
pprint(content)

# Grab the ETFs news.
content = nasdaq_news_client.etfs_feed()
pprint(content)

# Grab the Markets news.
content = nasdaq_news_client.markets_feed()
pprint(content)

# Grab the Options news.
content = nasdaq_news_client.options_feed()
pprint(content)

# Grab the Stocks news.
content = nasdaq_news_client.stocks_feed()
pprint(content)

# Grab the Artifical Intelligence news.
content = nasdaq_news_client.artifical_intelligence_feed()
pprint(content)

# Grab the Blockchain news.
content = nasdaq_news_client.blockchain_feed()
pprint(content)

# Grab the Corporate Governance news.
content = nasdaq_news_client.corporate_governance_feed()
pprint(content)

# Grab the Financial Advisors news.
content = nasdaq_news_client.financial_advisors_feed()
pprint(content)

# Grab the Fin Tech news.
content = nasdaq_news_client.fin_tech_feed()
pprint(content)

# Grab the Innovation news.
content = nasdaq_news_client.innovation_feed()
pprint(content)

# Grab the Nasdaq News Inc. news. -- NOT WORKING!!!!
content = nasdaq_news_client.nasdaq_news_feed()
pprint(content)

# Grab the Technology news.
content = nasdaq_news_client.technology_feed()
pprint(content)

# Grab the Investing news.
content = nasdaq_news_client.investing_feed()
pprint(content)

# Grab the Retirement news.
content = nasdaq_news_client.retirement_feed()
pprint(content)

# Grab the Saving Money news.
content = nasdaq_news_client.saving_money_feed()
pprint(content)

# Grab news articles for AAPL.
content = nasdaq_news_client.ticker_feed(ticker_symbol='AAPL')
pprint(content)
