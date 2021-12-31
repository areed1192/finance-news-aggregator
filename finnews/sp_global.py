from typing import List
from typing import Dict
from finnews.parser import NewsParser


class SPGlobal():

    """
    ### Overview:
    ----
    Used to access news articles from SP Global.
    """

    def __init__(self):
        """Initializes the `SPGlobal` client."""

        # Define the URL used to query feeds.
        self.url = 'https://www.spglobal.com/spdji/en/rss/rss-details/'

        # Define the parser client.
        self.news_parser = NewsParser(client='sp_global')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<SPGlobalClient Connected: True'>"

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
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def all_indicies(self) -> List[Dict]:
        """Used to query topics from the All Indicies RSS feed.

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

            >>> # Grab the All Indicies Feed.
            >>> sp_global_all_indicies = sp_global_client.all_indicies()
        """

        params = {
            'rssFeedName': 'all-indicies'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

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
        data = self.news_parser._make_request(
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
        data = self.news_parser._make_request(
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
        data = self.news_parser._make_request(
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
        data = self.news_parser._make_request(
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
        data = self.news_parser._make_request(
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
        data = self.news_parser._make_request(
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
        data = self.news_parser._make_request(
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
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def index_announcments(self) -> List[Dict]:
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

            >>> # Grab the Index Announcments Feed.
            >>> sp_global_index_announcements = sp_global_client.index_announcments()
        """

        params = {
            'rssFeedName': 'index-announcments'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data

    def new_counsultations(self) -> List[Dict]:
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
            >>> sp_global_new_counsultations = sp_global_client.new_counsultations()
        """

        params = {
            'rssFeedName': 'new-counsultations'
        }

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.url,
            params=params
        )

        return data
