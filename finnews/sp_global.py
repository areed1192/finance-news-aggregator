"""S&P Global RSS feed client for fetching ratings, indices, and research news."""

from __future__ import annotations

import warnings

from typing import List
from typing import Dict
from finnews.parser import NewsParser


class SPGlobal():

    """
    ### Overview:
    ----
    Used to access news articles from SP Global.
    """

    def __init__(self, cache_ttl: int = 0):
        """Initializes the `SPGlobal` client.

        ### Arguments:
        ----
        cache_ttl (int): TTL in seconds for cached responses (0 = off).
        """

        # Define the URL used to query feeds.
        self.url = 'https://www.spglobal.com/spdji/en/rss/rss-details/'

        # Define the parser client.
        self.news_parser = NewsParser(client='sp_global', cache_ttl=cache_ttl)

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<SPGlobalClient Connected: True'>"

    @property
    def feeds(self) -> list[str]:
        """Returns a sorted list of available feed method names.

        ### Returns:
        ----
        list[str]: Feed method names that can be called on this client.
        """

        return sorted([
            'all_indices', 'case_shiller_home_price_indices',
            'corporate_news', 'daily_index_insights', 'education',
            'index_announcements', 'index_launches', 'index_tv',
            'market_commentary', 'methodologies', 'new_consultations',
            'performance_reports', 'research', 'spiva',
        ])

    def methodologies(self) -> List[Dict]:
        """Used to query topics from the Methodologies RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Methdologies Feed.
            >>> sp_global_methodologies = sp_global_client.methodologies()
        """

        params = {
            'rssFeedName': 'methodologies'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def all_indices(self) -> List[Dict]:
        """Used to query topics from the All Indices RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the All Indices Feed.
            >>> sp_global_all_indices = sp_global_client.all_indices()
        """

        params = {
            'rssFeedName': 'all-indices'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def all_indicies(self) -> List[Dict]:
        """Deprecated: use ``all_indices()`` instead."""
        warnings.warn(
            "all_indicies() is deprecated, use all_indices() instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.all_indices()

    def research(self) -> List[Dict]:
        """Used to query topics from the Research RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Research Feed.
            >>> sp_global_research = sp_global_client.research()
        """

        params = {
            'rssFeedName': 'research'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def market_commentary(self) -> List[Dict]:
        """Used to query topics from the Market Commentary RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Market Commentary Feed.
            >>> sp_global_market_commentary = sp_global_client.market_commentary()
        """

        params = {
            'rssFeedName': 'market-commentary'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def education(self) -> List[Dict]:
        """Used to query topics from the Education RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Education Feed.
            >>> sp_global_education = sp_global_client.education()
        """

        params = {
            'rssFeedName': 'education'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def performance_reports(self) -> List[Dict]:
        """Used to query topics from the Performance Reports RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Performance Reports Feed.
            >>> sp_global_performance_reports = sp_global_client.performance_reports()
        """

        params = {
            'rssFeedName': 'performance-reports'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def spiva(self) -> List[Dict]:
        """Used to query topics from the SPIVA RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the SPIVA Feed.
            >>> sp_global_spive = sp_global_client.spiva()
        """

        params = {
            'rssFeedName': 'spiva'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def index_tv(self) -> List[Dict]:
        """Used to query topics from the Index TV RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Index TV Feed.
            >>> sp_global_index_tv = sp_global_client.index_tv()
        """

        params = {
            'rssFeedName': 'index-tv'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def corporate_news(self) -> List[Dict]:
        """Used to query topics from the Corporate News RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Corporate News Feed.
            >>> sp_global_corporate_news = sp_global_client.corporate_news()
        """

        params = {
            'rssFeedName': 'corporate-news'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def index_launches(self) -> List[Dict]:
        """Used to query topics from the Index Launches RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Index Launches Feed.
            >>> sp_global_index_launches = sp_global_client.index_launches()
        """

        params = {
            'rssFeedName': 'index-launches'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def index_announcements(self) -> List[Dict]:
        """Used to query topics from the Index Announcements RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Index Announcements Feed.
            >>> sp_global_index_announcements = sp_global_client.index_announcements()
        """

        params = {
            'rssFeedName': 'index-news-announcements'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def index_announcments(self) -> List[Dict]:
        """Deprecated: use ``index_announcements()`` instead."""
        warnings.warn(
            "index_announcments() is deprecated, use index_announcements() instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.index_announcements()

    def new_consultations(self) -> List[Dict]:
        """Used to query topics from the New Consultations RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the New Consultations Feed.
            >>> sp_global_new_consultations = sp_global_client.new_consultations()
        """

        params = {
            'rssFeedName': 'consultations'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def new_counsultations(self) -> List[Dict]:
        """Deprecated: use ``new_consultations()`` instead."""
        warnings.warn(
            "new_counsultations() is deprecated, use new_consultations() instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.new_consultations()

    def daily_index_insights(self) -> List[Dict]:
        """Used to query topics from the Daily Index Insights RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Daily Index Insights Feed.
            >>> sp_global_daily_index_insights = sp_global_client.daily_index_insights()
        """

        params = {
            'rssFeedName': 'daily-index-insights'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data

    def case_shiller_home_price_indices(self) -> List[Dict]:
        """Used to query topics from the S&P CoreLogic Case-Shiller Home Price Indices RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global

            >>> # Grab the Case-Shiller Home Price Indices Feed.
            >>> case_shiller = sp_global_client.case_shiller_home_price_indices()
        """

        params = {
            'rssFeedName': 'sp-cotality-case-shiller-home-price-indices'
        }

        # Grab the data.
        data = self.news_parser.make_request(
            url=self.url,
            params=params
        )

        return data
