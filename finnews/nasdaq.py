from enum import Enum
from typing import List
from typing import Dict
from typing import Union

import finnews.news_enum as enums_news
from finnews.parser import NewsParser


class NASDAQ():

    def __init__(self):
        """Initializes the `NASDAQ` client."""

        # Define the URL used to query feeds.
        self.url = 'https://www.nasdaq.com/feed/rssoutbound'
        self.url_original_content = 'https://www.nasdaq.com/feed/nasdaq-original/rss.xml'

        # Define the parser client.
        self.news_parser = NewsParser(client='nasdaq')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<NasdaqClient Connected: True'>"

    def original_content(self) -> Dict:
        """Used to query all the topics from the NASDAQ Original Content RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the original content news.
            >>> nasdaq_original_content = nasdaq_news_client.original_content()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url_original_content
        )

        return data

    def commodities_feed(self) -> List[Dict]:
        """Used to query topics from the Commodities News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Commodity news.
            >>> nasdaq_commodity_content = nasdaq_news_client.commodities_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Commodities'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def ipos_feed(self) -> List[Dict]:
        """Used to query topics from the IPOs News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the IPO news.
            >>> nasdaq_ipo_content = nasdaq_news_client.ipos_feed()
        """

        # Define the paramters.
        params = {
            'category': 'IPOs'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def cryptocurrency_feed(self) -> List[Dict]:
        """Used to query topics from the Cryptocurrency News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Cryptocurrency news.
            >>> nasdaq_cryptocurrency_content = nasdaq_news_client.cryptocurrency_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Cryptocurrencies'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def dividends_feed(self) -> List[Dict]:
        """Used to query topics from the Dividends News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Dividends news.
            >>> nasdaq_dividends_content = nasdaq_news_client.dividends_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Dividends'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def earnings_feed(self) -> List[Dict]:
        """Used to query topics from the Earnings News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Earnings news.
            >>> nasdaq_earnings_content = nasdaq_news_client.earnings_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Earnings'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def etfs_feed(self) -> List[Dict]:
        """Used to query topics from the ETFs News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the ETFs news.
            >>> nasdaq_etfs_content = nasdaq_news_client.etfs_feed()
        """

        # Define the paramters.
        params = {
            'category': 'ETFs'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def markets_feed(self) -> List[Dict]:
        """Used to query topics from the Markets News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Markets news.
            >>> nasdaq_markets_content = nasdaq_news_client.markets_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Markets'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def options_feed(self) -> List[Dict]:
        """Used to query topics from the Options News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Options news.
            >>> nasdaq_options_content = nasdaq_news_client.options_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Options'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def stocks_feed(self) -> List[Dict]:
        """Used to query topics from the Stocks News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Stocks news.
            >>> nasdaq_stocks_content = nasdaq_news_client.stocks_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Stocks'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def artifical_intelligence_feed(self) -> List[Dict]:
        """Used to query topics from the Artifical Intelligence News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Artifical Intelligence news.
            >>> nasdaq_artificial_intelligence_content = nasdaq_news_client.artifical_intelligence_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Artificial Intelligence'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def blockchain_feed(self) -> List[Dict]:
        """Used to query topics from the Blockchain News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Blockchain news.
            >>> nasdaq_blockchain_content = nasdaq_news_client.blockchain_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Blockchain'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def corporate_governance_feed(self) -> List[Dict]:
        """Used to query topics from the Corporate Governance News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Corporate Governance news.
            >>> nasdaq_corporate_governance_content = nasdaq_news_client.corporate_governance_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Corporate Governance'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def financial_advisors_feed(self) -> List[Dict]:
        """Used to query topics from the Financial Advisors News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Financial Advisors news.
            >>> nasdaq_financial_advisors_content = nasdaq_news_client.financial_advisors_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Financial Advisors'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def fin_tech_feed(self) -> List[Dict]:
        """Used to query topics from the Fin Tech News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Fin Tech news.
            >>> nasdaq_fin_tech_content = nasdaq_news_client.fin_tech_feed()
        """

        # Define the paramters.
        params = {
            'category': 'FinTech'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def innovation_feed(self) -> List[Dict]:
        """Used to query topics from the Innovation News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Innovation news.
            >>> nasdaq_innovation_content = nasdaq_news_client.innovatin_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Innovation'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def nasdaq_news_feed(self) -> List[Dict]:
        """Used to query topics from the Nasdaq News Inc. RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Innovation news.
            >>> nasdaq_nasdaq_content = nasdaq_news_client.nasdaq_news_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Nasdaq'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def technology_feed(self) -> List[Dict]:
        """Used to query topics from the Nasdaq Technology RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Technology news.
            >>> nasdaq_technology_content = nasdaq_news_client.technology_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Technology'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def investing_feed(self) -> List[Dict]:
        """Used to query topics from the Nasdaq Investing RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Investing news.
            >>> nasdaq_investing_content = nasdaq_news_client.investing_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Investing'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def retirement_feed(self) -> List[Dict]:
        """Used to query topics from the Nasdaq Retirement RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Retirement news.
            >>> nasdaq_retirement_content = nasdaq_news_client.retirement_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Retirement'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def saving_money_feed(self) -> List[Dict]:
        """Used to query topics from the Nasdaq Saving Money RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the Saving Money news.
            >>> nasdaq_saving_money_content = nasdaq_news_client.saving_money_feed()
        """

        # Define the paramters.
        params = {
            'category': 'Saving Money'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def ticker_feed(self, ticker_symbol: str) -> List[Dict]:
        """Used to query topics for a specific Ticker Symbol.

        Arguments:
        ----
        ticker_symbol (str): A ticker symbol that you want to
            query.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq

            >>> # Grab the news for AAPL.
            >>> aapl_articles = nasdaq_news_client.ticker_feed(ticker_symbol='AAPL')
        """

        # Define the paramters.
        params = {
            'symbol': ticker_symbol.lower()
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data
