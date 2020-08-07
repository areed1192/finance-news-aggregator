from enum import Enum
from typing import List
from typing import Dict
from typing import Union

import finnews.news_enum as enums_news
from finnews.parser import NewsParser


class WallStreetJournal():

    def __init__(self):
        """Initializes the `WallStreetJournal` client."""

        # Define the URL used to query feeds.
        self.url = 'https://feeds.a.dj.com/rss/{topic}.xml'

        # Define the parser client.
        self.news_parser = NewsParser(client='wsj')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<WallStreetJournal Connected: True'>"

    def all_feeds(self) -> Dict:
        """Used to query all the topics from the CNBC RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the top news.
            >>> cbnc_top_news = cnbc_news_client.all_feeds()
        """
        pass

        # all_news = {}

        # # Loop through all the topics.
        # for topic_key in self.topic_categories:

        #     print('PULLING TOPIC: {topic_id}'.format(topic_id=topic_key))

        #     # Grab the data.
        #     try:
        #         data = self.news_parser._make_request(
        #             url=self._check_key(topic_id=topic_key)
        #         )

        #         all_news[topic_key] = data
        #     except:
        #         continue

        #     time.sleep(1)

        # return all_news

    def opinions(self) -> List[Dict]:
        """Used to query topics from the Opinions RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='RSSOpinion')
        )

        return data

    def world_news(self) -> List[Dict]:
        """Used to query topics from the World News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='RSSWorldNews')
        )

        return data

    def us_business_news(self) -> List[Dict]:
        """Used to query topics from the United States Business News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='WSJcomUSBusiness')
        )

        return data

    def market_news(self) -> List[Dict]:
        """Used to query topics from the Market News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='RSSMarketsMain')
        )

        return data

    def technology_news(self) -> List[Dict]:
        """Used to query topics from the Technology News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='RSSWSJD')
        )

        return data

    def lifestyle(self) -> List[Dict]:
        """Used to query topics from the Lifestyle RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='RSSLifestyle')
        )

        return data
