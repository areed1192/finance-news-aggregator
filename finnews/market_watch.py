from enum import Enum
from typing import List
from typing import Dict
from typing import Union

import finnews.news_enum as enums_news
from finnews.parser import NewsParser


class MarketWatch():

    def __init__(self):
        """Initializes the `MarketWatch` client."""

        # Define the URL used to query feeds.
        self.url = 'http://feeds.marketwatch.com/marketwatch/{topic}/'

        # Define the parser client.
        self.news_parser = NewsParser(client='market_watch')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<MarketWatchClient Connected: True'>"

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
        pass

        # if topic_id in self.topic_categories:

        #     full_url = self.url.format(
        #         topic_id=self.topic_categories[topic_id]
        #     )
        #     return full_url
        # else:
        #     raise KeyError("The value you're searching for does not exist.")

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

    def top_stories(self) -> List[Dict]:
        """Used to query topics from the Top Stories Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='topstories')
        )

        return data

    def real_time_headlines(self) -> List[Dict]:
        """Used to query topics from the Real Time Headlines Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='realtimeheadlines')
        )

        return data

    def market_pulse(self) -> List[Dict]:
        """Used to query topics from the Market Pulse Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='marketpulse')
        )

        return data

    def bulletins(self) -> List[Dict]:
        """Used to query topics from the Bulletins Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
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
        data = self.news_parser._make_request(
            url=self.url.format(topic='bulletins')
        )

        return data

    def personal_finance(self) -> List[Dict]:
        """Used to query topics from the Personal Finance Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Personal Finance news.
            >>> market_watch_personal_finance = market_watch_client.personal_finance()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='pf')
        )

        return data

    def stocks_to_watch(self) -> List[Dict]:
        """Used to query topics from the Stocks To Watch Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Stocks to Watch Feed.
            >>> market_watch_stocks_to_watch = market_watch_client.stocks_to_watch()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='StockstoWatch')
        )

        return data

    def internet_stories(self) -> List[Dict]:
        """Used to query topics from the Internet Stories Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Internet Stories Feed.
            >>> market_watch_internet_stories = market_watch_client.internet_stories()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='Internet')
        )

        return data

    def mutual_funds(self) -> List[Dict]:
        """Used to query topics from the Mutual Funds Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Mutual Funds Feed.
            >>> market_watch_mutual_funds = market_watch_client.mutual_funds()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='mutualfunds')
        )

        return data

    def software_stories(self) -> List[Dict]:
        """Used to query topics from the Software Stories Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Software Stories Feed.
            >>> market_watch_software_stories = market_watch_client.software_stories()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='software')
        )

        return data

    def banking_and_finance(self) -> List[Dict]:
        """Used to query topics from the Banking & Finance Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Banking & Finance Feed.
            >>> market_watch_banking = market_watch_client.banking_and_finance()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='financial')
        )

        return data

    def commentary(self) -> List[Dict]:
        """Used to query topics from the Commentary Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Commentary Feed.
            >>> market_watch_commentary = market_watch_client.commentary()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='commentary')
        )

        return data

    def newsletter_and_research(self) -> List[Dict]:
        """Used to query topics from the Newsletter & Research Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Newsletter & Research Feed.
            >>> market_watch_newsletter_and_research = market_watch_client.newsletter_and_research()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='newslettersandresearch')
        )

        return data

    def auto_reviews(self) -> List[Dict]:
        """Used to query topics from the Auto Reviews Feed RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch

            >>> # Grab the Auto Reviews Feed.
            >>> market_watch_auto_reviews = market_watch_client.auto_reviews()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='autoreviews')
        )

        return data
