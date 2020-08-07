from enum import Enum
from typing import List
from typing import Dict
from typing import Union

import finnews.news_enum as enums_news
from finnews.parser import NewsParser


class YahooFinance():

    def __init__(self):
        """Initializes the `YahooFinance` client."""

        # Define the URLs used to query feeds.
        self.urls = {
            'news': 'https://finance.yahoo.com/news/rssindex',
            'headlines': 'https://feeds.finance.yahoo.com/rss/2.0/headline'
        }

        # Define the parser client.
        self.news_parser = NewsParser(client='yahoo')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<YahooFinance Connected: True'>"

    def news(self) -> List[Dict]:
        """Used to query topics from the News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Yahoo Finance News Client.
            >>> yahoo_finance_client = news_client.yahoo_finance

            >>> # Grab the News Feed.
            >>> yahoo_finance_news = yahoo_finance_client.news()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['news']
        )

        return data

    def headlines(self, symbols: List[str]) -> List[Dict]:
        """Used to query news headlines for a list of Stocks from the RSS feed.

        Arguments:
        ----
        symbols (List[str]): A list of ticker symbols to query.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Yahoo Finance News Client.
            >>> yahoo_finance_client = news_client.yahoo_finance

            >>> # Grab the Headlines for Google & Microsoft.
            >>> yahoo_finance_headlines = yahoo_finance_client.headlines(symbol=['GOOG', 'MSFT'])
        """

        # Define the parameters.
        params = {
            's': ','.join(symbols),
            'region': 'US',
            'lang': 'en-US'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['headlines'],
            params=params
        )

        return data
