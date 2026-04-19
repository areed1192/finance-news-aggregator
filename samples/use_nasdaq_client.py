"""Sample script demonstrating the NASDAQ news client."""

from pprint import pprint

from finnews.client import News
from finnews.article import NewsArticle, NewsFeed

# Create a new instance of the News Client.
news_client = News()

# Grab the NASDAQ News Client.
nasdaq_news_client = news_client.nasdaq

# ---------------------------------------------------------------------------
# Section: List available feeds.
# ---------------------------------------------------------------------------

# Print the available feed methods.
print("Available feeds:", nasdaq_news_client.feeds)

# ---------------------------------------------------------------------------
# Section: Fetch a feed and wrap in structured models.
# ---------------------------------------------------------------------------

# Grab the Original Content news.
original_content = nasdaq_news_client.original_content()

# Wrap the results in a NewsFeed.
feed = NewsFeed.from_dicts(original_content, source='nasdaq')
print(f"\nOriginal content articles: {len(feed)}")
for article in feed:
    print(f"  - {article.title} ({article.published})")

# Convert a single result to a NewsArticle.
if original_content:
    article = NewsArticle.from_dict(original_content[0], source='nasdaq')
    print(f"\nFirst article: {article.title}")
    print(f"  Link: {article.link}")

# ---------------------------------------------------------------------------
# Section: Fetch additional feeds.
# ---------------------------------------------------------------------------

# Grab the Commodity news.
commodities = nasdaq_news_client.commodities_feed()
pprint(commodities)

# Grab the IPO news.
ipos = nasdaq_news_client.ipos_feed()
pprint(ipos)

# Grab the Cryptocurrency news.
crypto = nasdaq_news_client.cryptocurrency_feed()
pprint(crypto)

# Grab the Dividends news.
dividends = nasdaq_news_client.dividends_feed()
pprint(dividends)

# Grab the Earnings news.
earnings = nasdaq_news_client.earnings_feed()
pprint(earnings)

# Grab the ETFs news.
etfs = nasdaq_news_client.etfs_feed()
pprint(etfs)

# Grab the Markets news.
markets = nasdaq_news_client.markets_feed()
pprint(markets)

# Grab the Options news.
options = nasdaq_news_client.options_feed()
pprint(options)

# Grab the Stocks news.
stocks = nasdaq_news_client.stocks_feed()
pprint(stocks)

# Grab the Artificial Intelligence news.
ai_news = nasdaq_news_client.artificial_intelligence_feed()
pprint(ai_news)

# Grab the Blockchain news.
blockchain = nasdaq_news_client.blockchain_feed()
pprint(blockchain)

# Grab the Corporate Governance news.
corp_gov = nasdaq_news_client.corporate_governance_feed()
pprint(corp_gov)

# Grab the Financial Advisors news.
fin_advisors = nasdaq_news_client.financial_advisors_feed()
pprint(fin_advisors)

# Grab the Fin Tech news.
fin_tech = nasdaq_news_client.fin_tech_feed()
pprint(fin_tech)

# Grab the Innovation news.
innovation = nasdaq_news_client.innovation_feed()
pprint(innovation)

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
