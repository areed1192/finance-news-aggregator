"""Yahoo Finance RSS feed client for fetching top stories and market news."""

from __future__ import annotations

from typing import List
from typing import Dict

from finnews.parser import NewsParser


class YahooFinance():

    """
    ### Overview:
    ----
    Used to access news articles from Yahoo Finance.
    """

    def __init__(self, cache_ttl: int = 0):
        """Initializes the `YahooFinance` client.

        ### Arguments:
        ----
        cache_ttl (int): TTL in seconds for cached responses (0 = off).
        """

        # Define the URLs used to query feeds.
        self.urls = {
            'news': 'https://finance.yahoo.com/news/rssindex',
            'headlines': 'https://feeds.finance.yahoo.com/rss/2.0/headline'
        }

        # Define the parser client.
        self.news_parser = NewsParser(client='yahoo', cache_ttl=cache_ttl)

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<YahooFinance Connected: True'>"

    @property
    def feeds(self) -> list[str]:
        """Returns a sorted list of available feed method names.

        ### Returns:
        ----
        list[str]: Feed method names that can be called on this client.
        """

        return sorted(['headlines', 'news'])

    def news(self) -> List[Dict]:
        """Used to query topics from the News RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
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
        data = self.news_parser.make_request(
            url=self.urls['news']
        )

        return data

    def headlines(self, symbols: List[str]) -> List[Dict]:
        """Used to query news headlines for a list of Stocks from the RSS feed.

        ### Arguments:
        ----
        symbols (List[str]): A list of ticker symbols to query.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
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
        data = self.news_parser.make_request(
            url=self.urls['headlines'],
            params=params
        )

        return data
