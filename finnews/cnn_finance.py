from enum import Enum
from typing import List
from typing import Dict
from typing import Union

import finnews.news_enum as enums_news
from finnews.parser import NewsParser


class CNNFinance():

    def __init__(self):
        """Initializes the `CNNFinance` client."""

        # Define the URL used to query feeds.
        self.url = 'http://rss.cnn.com/rss/{topic}.rss'
        self.url_buzz = 'http://rss.cnn.com/cnnmoneymorningbuzz'

        # Define the parser client.
        self.news_parser = NewsParser(client='cnn_finance')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<CNNFinance Connected: True'>"

    def all_stories(self) -> List[Dict]:
        """Used to query topics from the All Stories RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the All Stories Feed.
            >>> cnn_finance_all_stories = cnn_finance.all_stories()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_latest')
        )

        return data

    def top_stories(self) -> List[Dict]:
        """Used to query topics from the Top Stories RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Top Stories Feed.
            >>> cnn_finance_top_stories = cnn_finance.top_stories()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_topstories')
        )

        return data

    def most_popular(self) -> List[Dict]:
        """Used to query topics from the Most Popular RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Most Popular Feed.
            >>> cnn_finance_most_popular = cnn_finance.most_popular()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_mostpopular')
        )

        return data

    def companies(self) -> List[Dict]:
        """Used to query topics from the Companies RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Companies Feed.
            >>> cnn_finance_companies = cnn_finance.companies()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_news_companies')
        )

        return data

    def international(self) -> List[Dict]:
        """Used to query topics from the Internationals RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Internationals Feed.
            >>> cnn_finance_international = cnn_finance.international()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_news_international')
        )

        return data

    def economy(self) -> List[Dict]:
        """Used to query topics from the Economy RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Economoy Feed.
            >>> cnn_finance_economy = cnn_finance.economy()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_news_economy')
        )

        return data

    def video_news(self) -> List[Dict]:
        """Used to query topics from the Video News RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Video News Feed.
            >>> cnn_finance_video_news = cnn_finance.video_news()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_video_business')
        )

        return data

    def media(self) -> List[Dict]:
        """Used to query topics from the Media RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Media Feed.
            >>> cnn_finance_media = cnn_finance.media()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_media')
        )

        return data

    def markets(self) -> List[Dict]:
        """Used to query topics from the Markets RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Markets Feed.
            >>> cnn_finance_markets = cnn_finance.markets()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_markets')
        )

        return data

    def morning_buzz(self) -> List[Dict]:
        """Used to query topics from the Morning Buzz RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Morning Buzz Feed.
            >>> cnn_finance_morning_buzz = cnn_finance.morning_buzz()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url_buzz
        )

        return data

    def techonology(self) -> List[Dict]:
        """Used to query topics from the Technology RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Technology Feed.
            >>> cnn_finance_technology = cnn_finance.technology()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_technology')
        )

        return data

    def personal_finance(self) -> List[Dict]:
        """Used to query topics from the Personal Finance RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Personal Finance Feed.
            >>> cnn_finance_personal_finance = cnn_finance.personal_finance()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_pf')
        )

        return data

    def autos(self) -> List[Dict]:
        """Used to query topics from the Autos RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Autos Feed.
            >>> cnn_finance_autos = cnn_finance.autos()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_autos')
        )

        return data

    def funds(self) -> List[Dict]:
        """Used to query topics from the Funds RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Funds Feed.
            >>> cnn_finance_funds = cnn_finance.funds()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_funds')
        )

        return data

    def colleges(self) -> List[Dict]:
        """Used to query topics from the College RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the College Feed.
            >>> cnn_finance_colleges = cnn_finance.colleges()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_pf_college')
        )

        return data

    def insurance(self) -> List[Dict]:
        """Used to query topics from the Insurance RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Insurance Feed.
            >>> cnn_finance_insurance = cnn_finance.insurance()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_pf_insurance')
        )

        return data

    def taxes(self) -> List[Dict]:
        """Used to query topics from the Taxes RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Taxes Feed.
            >>> cnn_finance_taxes = cnn_finance.taxes()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_pf_taxes')
        )

        return data

    def retirement(self) -> List[Dict]:
        """Used to query topics from the Retirement RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Retirment Feed.
            >>> cnn_finance_retirement = cnn_finance.retirement()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_retirement')
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

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Lifestyle Feed.
            >>> cnn_finance_lifestyle = cnn_finance.lifestyle()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_lifestyle')
        )

        return data

    def real_estate(self) -> List[Dict]:
        """Used to query topics from the Real Estate RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Real Estate Feed.
            >>> cnn_finance_real_estate = cnn_finance.real_estate()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_realestate')
        )

        return data

    def luxury(self) -> List[Dict]:
        """Used to query topics from the Luxury RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Luxury Feed.
            >>> cnn_finance_luxury = cnn_finance.luxury()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_luxury')
        )

        return data

    def small_business(self) -> List[Dict]:
        """Used to query topics from the Small Business RSS feed.

        Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance = news_client.cnn_finance

            >>> # Grab the Small Business Feed.
            >>> cnn_finance_small_business = cnn_finance.small_business()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url.format(topic='money_smbusiness')
        )

        return data