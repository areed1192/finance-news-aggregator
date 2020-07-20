import requests
import xml.etree.ElementTree as ET

from typing import List
from typing import Dict
from typing import Union

from finnews.parser import NewsParser


class CNBC():

    def __init__(self):
        """Initializes the `CNBC` client."""

        # Define the URL used to query feeds.
        self.url = 'https://www.cnbc.com/id/{topic_id}/device/rss/rss.html'

        # Define the topic categories.
        self.topic_categories = {
            'top_news': '100003114',
        }

        # Define the parser client.
        self.news_parser = NewsParser(client='cnbc')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<CnbcClient Connected: True'>"

    def _check_key(self, topic_id: str) -> str:
        """Checks the topic ID to see if it's valid.

        Arguments:
        ----
        topic_id (str): The topic ID to query and check.

        Raises:
        ----
        KeyError: If topic doesn't exist will raise a
            `KeyError` asking you to provide a valid topic.

        Returns:
        ----
        str: The full URL to be used in the request.
        """

        if topic_id in self.topic_categories:

            full_url = self.url.format(
                topic_id=self.topic_categories[topic_id]
            )
            return full_url
        else:
            raise KeyError("The value you're searching for does not exist.")

    def news_feed(self, topic: str) -> List[Dict]:
        """Used to query topics from the News Feed RSS feed.

        Arguments:
        ----
        topic (str): The topic ID you wish to return articles for.
            For example, `top_news` will return the top news articles.

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
            >>> cbnc_top_news = cnbc_news_client.news_feed(topic='top_news')
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self._check_key(topic_id=topic)
        )

        return data

    def investing_feeds(self, topic: str) -> List[Dict]:
        pass

    def blogs(self, topic: str) -> List[Dict]:
        pass

    def investing_feeds(self, topic: str) -> List[Dict]:
        pass

    def videos_and_tv(self, topic: str) -> List[Dict]:
        pass

    def tv_programs_europe(self, topic: str) -> List[Dict]:
        pass

    def tv_programs_asia(self, topic: str) -> List[Dict]:
        pass

    def _parse_results(self, raw_content: str) -> List[Dict]:
        pass
