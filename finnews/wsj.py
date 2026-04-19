"""Wall Street Journal RSS feed client for fetching news and opinion articles."""

from __future__ import annotations

from typing import List
from typing import Dict

from finnews.parser import NewsParser


class WallStreetJournal():

    """
    ### Overview:
    ----
    Used to access news articles from WallStreetJournal.
    """

    def __init__(self, cache_ttl: int = 0):
        """Initializes the `WallStreetJournal` client.

        ### Arguments:
        ----
        cache_ttl (int): TTL in seconds for cached responses (0 = off).
        """

        # Define the URL used to query feeds.
        self.url = 'https://feeds.a.dj.com/rss/{topic}.xml'

        # Define the parser client.
        self.news_parser = NewsParser(client='wsj', cache_ttl=cache_ttl)

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<WallStreetJournal Connected: True'>"

    @property
    def feeds(self) -> list[str]:
        """Returns a sorted list of available feed method names.

        ### Returns:
        ----
        list[str]: Feed method names that can be called on this client.
        """

        return sorted([
            'lifestyle', 'market_news', 'opinions',
            'technology_news', 'us_business_news', 'world_news',
        ])

    def opinions(self) -> List[Dict]:
        """Used to query topics from the Opinions RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Wall Street Journal News Client.
            >>> wsj_client = news_client.wsj

            >>> # Grab the Opinions Feed.
            >>> wsj_opinions = wsj_client.opinions()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url.format(topic='RSSOpinion')
        )

        return data

    def world_news(self) -> List[Dict]:
        """Used to query topics from the World News RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Wall Street Journal News Client.
            >>> wsj_client = news_client.wsj

            >>> # Grab the World News Feed.
            >>> wsj_world_news = wsj_client.world_news()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url.format(topic='RSSWorldNews')
        )

        return data

    def us_business_news(self) -> List[Dict]:
        """Used to query topics from the United States Business News RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Wall Street Journal News Client.
            >>> wsj_client = news_client.wsj

            >>> # Grab the US Business News Feed.
            >>> wsj_us_business_news = wsj_client.us_business_news()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url.format(topic='WSJcomUSBusiness')
        )

        return data

    def market_news(self) -> List[Dict]:
        """Used to query topics from the Market News RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Wall Street Journal News Client.
            >>> wsj_client = news_client.wsj

            >>> # Grab the Market News Feed.
            >>> wsj_market_news = wsj_client.market_news()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url.format(topic='RSSMarketsMain')
        )

        return data

    def technology_news(self) -> List[Dict]:
        """Used to query topics from the Technology News RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Wall Street Journal News Client.
            >>> wsj_client = news_client.wsj

            >>> # Grab the Technology News Feed.
            >>> wsj_technology_news = wsj_client.technology_news()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url.format(topic='RSSWSJD')
        )

        return data

    def lifestyle(self) -> List[Dict]:
        """Used to query topics from the Lifestyle RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Wall Street Journal News Client.
            >>> wsj_client = news_client.wsj

            >>> # Grab the Lifestyle Feed.
            >>> wsj_lifestyle = wsj_client.lifestyle()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url.format(topic='RSSLifestyle')
        )

        return data
