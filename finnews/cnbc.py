"""CNBC RSS feed client for fetching news, investing, blog, and TV articles."""

from __future__ import annotations

import logging
import time

from enum import Enum
from typing import Dict
from typing import List

from finnews.parser import NewsParser
from finnews.fields import cnbc_rss_feeds_id
from finnews.exceptions import InvalidTopicError

logger = logging.getLogger(__name__)


class CNBC:
    """
    ### Overview:
    ----
    Used to access news articles from CNBC.
    """

    def __init__(self, cache_ttl: int = 0):
        """Initializes the `CNBC` client.

        ### Arguments:
        ----
        cache_ttl (int): TTL in seconds for cached responses (0 = off).
        """

        # Define the URL used to query feeds.
        self.url = "https://www.cnbc.com/id/{topic_id}/device/rss/rss.html"

        # Define the topic categories.
        self.topic_categories: dict = cnbc_rss_feeds_id

        # Define the parser client.
        self.news_parser = NewsParser(client="cnbc", cache_ttl=cache_ttl)

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<CnbcClient Connected: True'>"

    @property
    def topics(self) -> list[str]:
        """Returns a sorted list of available topic names.

        ### Returns:
        ----
        list[str]: Sorted topic names that can be passed to feed methods.
        """

        return sorted(self.topic_categories)

    def _check_key(self, topic_id: str) -> str:
        """Checks the topic ID to see if it's valid.

        ### Arguments:
        ----
        topic_id (str): The topic ID to query and check.

        Raises:
        ----
        KeyError: If topic doesn't exist will raise a
            `KeyError` asking you to provide a valid topic.

        ### Returns:
        ----
        str: The full URL to be used in the request.
        """

        if topic_id in self.topic_categories:
            full_url = self.url.format(topic_id=self.topic_categories[topic_id])
            return full_url

        valid = ', '.join(sorted(self.topic_categories))
        raise InvalidTopicError(
            f"Unknown topic {topic_id!r}. Valid topics: {valid}"
        )

    def all_feeds(self) -> Dict:
        """Used to query all the topics from the CNBC RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the top news.
            >>> cbnc_top_news = cnbc_news_client.all_feeds()
        """

        all_news = {}

        # Loop through all the topics.
        for topic_key in self.topic_categories:

            logger.debug("PULLING TOPIC: %s", topic_key)

            # Grab the data.
            try:
                data = self.news_parser.make_request(
                    url=self._check_key(topic_id=topic_key)
                )

                all_news[topic_key] = data
            except InvalidTopicError:
                continue

            time.sleep(1)

        return all_news

    def news_feed(self, topic: str | Enum) -> List[Dict]:
        """Used to query topics from the News Feed RSS feed.

        Arguments:
        ---
        topic (str): The topic ID you wish to return articles for.
            For example, `top_news` will return the top news articles.

        Returns:
        ---
        List[Dict]: A list of news articles organized in dictionaries.

        Usage:
        ---

            >>> # Create a new instance of the News Client.
            >>> from finnews.client import News

            # Create a new instance of the News Client.
            >>> news_client = News()

            # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            # Grab the top news.
            >>> cbnc_top_news = cnbc_news_client.news_feed(topic='top_news')

        """

        # If it's an enum grab the name.
        if isinstance(topic, Enum):
            topic = topic.name.lower()

        # Grab the data.
        data = self.news_parser.make_request(url=self._check_key(topic_id=topic))

        return data

    def investing_feeds(self, topic: str | Enum) -> List[Dict]:
        """Used to query topics from the Investing News RSS feed.

        ### Arguments:
        ----
        topic (str): The topic ID you wish to return articles for.
            For example, `investing_news` will return the top news articles.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the investing news.
            >>> cbnc_top_news = cnbc_news_client.investing_feeds(topic='investing')
        """

        # If it's an enum grab the name.
        if isinstance(topic, Enum):
            topic = topic.name.lower()

        # Grab the data.
        data = self.news_parser.make_request(url=self._check_key(topic_id=topic))

        return data

    def blogs(self, topic: str | Enum) -> List[Dict]:
        """Used to query topics from the Blogs RSS feed.

        ### Arguments:
        ----
        topic (str): The topic ID you wish to return articles for.
            For example, `charting_asia` will return the top news articles.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the top blogs.
            >>> cbnc_top_news = cnbc_news_client.blogs(topic='charting_asia')
        """

        # If it's an enum grab the name.
        if isinstance(topic, Enum):
            topic = topic.name.lower()

        # Grab the data.
        data = self.news_parser.make_request(url=self._check_key(topic_id=topic))

        return data

    def videos_and_tv(self, topic: str | Enum) -> List[Dict]:
        """Used to query topics from the Videos & TV RSS feed.

        ### Arguments:
        ----
        topic (str): The topic ID you wish to return articles for.
            For example, `top_video` will return the top news articles.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the articles from videos and tv.
            >>> cbnc_top_news = cnbc_news_client.videos_and_tv(topic='top_video')
        """

        # If it's an enum grab the name.
        if isinstance(topic, Enum):
            topic = topic.name.lower()

        # Grab the data.
        data = self.news_parser.make_request(url=self._check_key(topic_id=topic))

        return data

    def tv_programs_europe(self, topic: str | Enum) -> List[Dict]:
        """Used to query topics from the TV Programs (Europe) RSS feed.

        ### Arguments:
        ----
        topic (str): The topic ID you wish to return articles for.
            For example, `capital_connection` will return the top news articles.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the articles from Europe.
            >>> cbnc_top_news = cnbc_news_client.tv_programs_europe(
                topic='capital_connection'
            )
        """

        # If it's an enum grab the name.
        if isinstance(topic, Enum):
            topic = topic.name.lower()

        # Grab the data.
        data = self.news_parser.make_request(url=self._check_key(topic_id=topic))

        return data

    def tv_programs_asia(self, topic: str | Enum) -> List[Dict]:
        """Used to query topics from the TV Programs (Asia) RSS feed.

        ### Arguments:
        ----
        topic (str): The topic ID you wish to return articles for.
            For example, `squawk_box_asia` will return the top news articles.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the articles from Asia.
            >>> cbnc_top_news = cnbc_news_client.tv_programs_asia(
                topic='squawk_box_asia'
            )
        """

        # If it's an enum grab the name.
        if isinstance(topic, Enum):
            topic = topic.name.lower()

        # Grab the data.
        data = self.news_parser.make_request(url=self._check_key(topic_id=topic))

        return data
