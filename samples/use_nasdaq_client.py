from pprint import pprint

from finnews.client import News

# Create a new instance of the News Client.
news_client = News()

# Grab the NASDAQ News Client.
nasdaq_news_client = news_client.nasdaq

# Grab the original content news.
nasdaq_original_content = nasdaq_news_client.original_content()
pprint(nasdaq_original_content)

# Grab the Commodity news.
nasdaq_commodity_content = nasdaq_news_client.commodities_feed()
pprint(nasdaq_commodity_content)

# Grab the IPO news.
nasdaq_ipo_content = nasdaq_news_client.ipos_feed()
pprint(nasdaq_ipo_content)

# Grab the Cryptocurrency news.
nasdaq_cryptocurrency_content = nasdaq_news_client.cryptocurrency_feed()
pprint(nasdaq_cryptocurrency_content)

# Grab the Dividends news.
nasdaq_dividends_content = nasdaq_news_client.dividends_feed()
pprint(nasdaq_dividends_content)

# Grab the Earnings news.
nasdaq_earnings_content = nasdaq_news_client.earnings_feed()
pprint(nasdaq_earnings_content)

# Grab the ETFs news.
nasdaq_etfs_content = nasdaq_news_client.etfs_feed()
pprint(nasdaq_etfs_content)

# Grab the Markets news.
nasdaq_markets_content = nasdaq_news_client.markets_feed()
pprint(nasdaq_markets_content)

# Grab the Options news.
nasdaq_options_content = nasdaq_news_client.options_feed()
pprint(nasdaq_options_content)

# Grab the Stocks news.
nasdaq_stocks_content = nasdaq_news_client.stocks_feed()
pprint(nasdaq_stocks_content)

# Grab the Artifical Intelligence news.
nasdaq_artifical_intelligence_content = nasdaq_news_client.artifical_intelligence_feed()
pprint(nasdaq_artifical_intelligence_content)

# Grab the Blockchain news.
nasdaq_blockchain_content = nasdaq_news_client.blockchain_feed()
pprint(nasdaq_blockchain_content)

# Grab the Corporate Governance news.
nasdaq_corporate_governance_content = nasdaq_news_client.corporate_governance_feed()
pprint(nasdaq_corporate_governance_content)

# Grab the Financial Advisors news.
nasdaq_financial_advisors_content = nasdaq_news_client.financial_advisors_feed()
pprint(nasdaq_financial_advisors_content)

# Grab the Fin Tech news.
nasdaq_fin_tech_content = nasdaq_news_client.fin_tech_feed()
pprint(nasdaq_fin_tech_content)

# Grab the Innovation news.
nasdaq_innovation_content = nasdaq_news_client.innovation_feed()
pprint(nasdaq_innovation_content)

# Grab the Nasdaq News Inc. news. -- NOT WORKING!!!!
nasdaq_news_content = nasdaq_news_client.nasdaq_news_feed()
pprint(nasdaq_news_content)

# Grab the Technology news.
nasdaq_technology_content = nasdaq_news_client.technology_feed()
pprint(nasdaq_technology_content)

# Grab the Investing news.
nasdaq_investing_content = nasdaq_news_client.investing_feed()
pprint(nasdaq_investing_content)

# Grab the Retirement news.
nasdaq_retirement_content = nasdaq_news_client.retirement_feed()
pprint(nasdaq_retirement_content)

# Grab the Saving Money news.
nasdaq_saving_money_content = nasdaq_news_client.saving_money_feed()
pprint(nasdaq_saving_money_content)

# Grab news articles for AAPL.
aapl_articles = nasdaq_news_client.ticker_feed(ticker_symbol='AAPL')
pprint(aapl_articles)
