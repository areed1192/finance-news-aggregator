"""MarketWatch RSS feed client for fetching financial news and commentary."""

from __future__ import annotations

import logging
import time
import warnings
from enum import Enum
from typing import List
from typing import Dict

from finnews.parser import NewsParser
from finnews.fields import market_watch_rss_feeds_id
from finnews.exceptions import InvalidTopicError

logger = logging.getLogger(__name__)


class MarketWatch():

    """
    ### Overview:
    ----
    Used to access news articles from MarketWatch.
    """

    def __init__(self, cache_ttl: int = 0):
        """Initializes the `MarketWatch` client.

        ### Arguments:
        ----
        cache_ttl (int): TTL in seconds for cached responses (0 = off).
        """

        # Define the URLs for available feeds.
        self.feed_urls = {
            'top_stories': 'https://feeds.content.dowjones.io/public/rss/mw_topstories',
            'real_time_headlines': (
                'https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines'
            ),
            'bulletins': 'http://feeds.marketwatch.com/marketwatch/bulletins',
            'market_pulse': 'https://feeds.content.dowjones.io/public/rss/mw_marketpulse',
        }

        # Legacy template URL kept for backward compatibility with _check_key.
        self.url = 'https://feeds.marketwatch.com/marketwatch/{topic}/'

        # Define the parser client.
        self.news_parser = NewsParser(client='market_watch', cache_ttl=cache_ttl)

        # Define the Topic Categories.
        self.topic_categories = market_watch_rss_feeds_id

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<MarketWatchClient Connected: True'>"

    @property
    def topics(self) -> list[str]:
        """Returns a sorted list of available feed names.

        ### Returns:
        ----
        list[str]: Sorted feed names that can be called as methods.
        """

        return sorted(self.feed_urls)

    def _check_key(self, topic_id: str | Enum) -> str:
        """Checks the topic ID to see if it's valid.

        ### Arguments:
        ----
        topic_id (str): The topic ID to query and check.

        ### Raises:
        ----
        KeyError: If topic doesn't exist will raise a
            `KeyError` asking you to provide a valid topic.

        ### Returns:
        ----
        str: The full URL to be used in the request.
        """

        if isinstance(topic_id, Enum):
            topic_id = topic_id.name.lower()

        if topic_id in self.topic_categories:
            full_url = self.url.format(
                topic=self.topic_categories[topic_id]
            )
            return full_url

        valid = ', '.join(sorted(self.topic_categories))
        raise InvalidTopicError(
            f"Unknown topic {topic_id!r}. Valid topics: {valid}"
        )

    def all_feeds(self) -> Dict:
        """Used to query all the topics from the Market Watch RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Market Watch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the top news.
            >>> all_feeds = market_watch_client.all_feeds()
        """

        all_news = {}

        # Loop through all the feeds.
        for feed_key, feed_url in self.feed_urls.items():

            logger.debug('PULLING TOPIC: %s', feed_key)

            # Grab the data.
            try:
                data = self.news_parser.make_request(url=feed_url)
                all_news[feed_key] = data
            except Exception:  # noqa: BLE001  # pylint: disable=broad-exception-caught
                continue

            time.sleep(1)

        return all_news

    def top_stories(self) -> List[Dict]:
        """Used to query topics from the Top Stories Feed RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the top news.
            >>> market_watch_top_stories = market_watch_client.top_stories()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.feed_urls['top_stories']
        )

        return data

    def real_time_headlines(self) -> List[Dict]:
        """Used to query topics from the Real Time Headlines Feed RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Real Time Headlines news.
            >>> market_watch_real_time_headlines = market_watch_client.real_time_headlines()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.feed_urls['real_time_headlines']
        )

        return data

    def market_pulse(self) -> List[Dict]:
        """Used to query topics from the Market Pulse Feed RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Market Pulse news.
            >>> market_watch_market_pulse = market_watch_client.market_pulse()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.feed_urls['market_pulse']
        )

        return data

    def bulletins(self) -> List[Dict]:
        """Used to query topics from the Bulletins Feed RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Bulletins news.
            >>> market_watch_bulletins = market_watch_client.bulletins()
        """

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.feed_urls['bulletins']
        )

        return data

    # -------------------------------------------------------------------
    # Deprecated feeds — these RSS endpoints no longer exist.
    # -------------------------------------------------------------------

    def personal_finance(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "personal_finance() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def stocks_to_watch(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "stocks_to_watch() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def internet_stories(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "internet_stories() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def mutual_funds(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "mutual_funds() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def software_stories(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "software_stories() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def banking_and_finance(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "banking_and_finance() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def commentary(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "commentary() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def newsletter_and_research(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "newsletter_and_research() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []

    def auto_reviews(self) -> List[Dict]:
        """Deprecated: this RSS feed is no longer available."""
        warnings.warn(
            "auto_reviews() is deprecated — the MarketWatch RSS feed no longer exists",
            DeprecationWarning,
            stacklevel=2,
        )
        return []
