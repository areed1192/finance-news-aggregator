from typing import List
from typing import Dict

from finnews.parser import NewsParser


class SeekingAlpha():

    """
    ### Overview:
    ----
    Used to access news articles from SeekingAlpha.
    """

    def __init__(self):
        """Initializes the `SeekingAlpha` client."""

        # Define the URL used to query feeds.
        self.urls = {
            'feed': 'https://seekingalpha.com/feed.xml',
            'sector': 'https://seekingalpha.com/sector/{topic}.xml',
            'tag': 'https://seekingalpha.com/tag/{topic}.xml',
            'listing': 'https://seekingalpha.com/listing/{topic}.xml',
            'api': 'https://seekingalpha.com/api/sa/combined/{topic}.xml',
            'markets': 'https://seekingalpha.com/market_currents.xml'
        }

        # Define the parser client.
        self.news_parser = NewsParser(client='seeking_alpha')

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<SeekingAlpha Connected: True'>"

    def stocks(self, ticker: str) -> List[Dict]:
        """Used to query topics for a particular Stock's RSS feed.

        ### Arguments:
        ----
        ticker (str): The ticker symbol you wish to query.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Stocks Feed.
            >>> seeking_alpha_tsla = seeking_alpha_client.stocks(ticker='TSLA')
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['api'].format(topic=ticker)
        )

        return data

    def latest_articles(self) -> List[Dict]:
        """Used to query topics from the Latest Articles RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Latest Articles Feed.
            >>> seeking_alpha_latest_articles = seeking_alpha_client.latest_articles()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['feed']
        )

        return data

    def ipo_analysis(self) -> List[Dict]:
        """Used to query topics from the IPO Analysis RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the IPO Analysis Feed.
            >>> seeking_alpha_ipo_analysis = seeking_alpha_client.ipo_analysis()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic='ipo-analysis')
        )

        return data

    def long_ideas(self) -> List[Dict]:
        """Used to query topics from the Long Ideas RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Long ideas Feed.
            >>> seeking_alpha_long_ideas = seeking_alpha_client.long_ideas()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic='long-ideas')
        )

        return data

    def transcripts(self) -> List[Dict]:
        """Used to query topics from the Transcripts RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Transcripts Feed.
            >>> seeking_alpha_transcripts = seeking_alpha_client.transcripts()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['sector'].format(topic='transcripts')
        )

        return data

    def all_news(self) -> List[Dict]:
        """Used to query topics from the All News RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the All News Feed.
            >>> seeking_alpha_all_news = seeking_alpha_client.all_news()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['markets']
        )

        return data

    def wall_street_breakfast(self) -> List[Dict]:
        """Used to query topics from the Wall Street Breakfast RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Wall Street Breakfast Feed.
            >>> seeking_alpha_wall_street_breakfast = seeking_alpha_client.wall_street_breakfast()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic='wall-st-breakfast')
        )

        return data

    def most_popular_articles(self) -> List[Dict]:
        """Used to query topics from the Most Populart Articles RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Most Popular Articles Feed.
            >>> seeking_alpha_most_popular_articles = seeking_alpha_client.most_popular_articles()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['listing'].format(topic='most-popular-articles')
        )

        return data

    def forex(self) -> List[Dict]:
        """Used to query topics from the Forex RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Forex Feed.
            >>> seeking_alpha_forex = seeking_alpha_client.forex()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic='forex')
        )

        return data

    def editors_picks(self) -> List[Dict]:
        """Used to query topics from the Editor Picks RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Editor Picks Feed.
            >>> seeking_alpha_editor_picks = seeking_alpha_client.editors_picks()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic='editors-picks')
        )

        return data

    def etfs(self) -> List[Dict]:
        """Used to query topics from the ETFs RSS feed.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the ETFs Feed.
            >>> seeking_alpha_etfs = seeking_alpha_client.etfs()
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic='etf-portfolio-strategy')
        )

        return data

    def global_markets(self, country: str) -> List[Dict]:
        """Used to query topics for a particular Country's Global Market RSS feed.

        ### Arguments:
        ----
        country (str): The country you wish to query.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the France Global Markets Feed.
            >>> seeking_alpha_france = seeking_alpha_client.global_markets(country='france')
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic=country)
        )

        return data

    def sectors(self, sector: str) -> List[Dict]:
        """Used to query topics for a particular Sector's News RSS feed.

        ### Arguments:
        ----
        sector (str): The sector you wish to query.

        ### Returns:
        ----
        List[Dict]: A list of news articles organzied in dictionaries.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Seeking Alpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha

            >>> # Grab the Financial Sector Feed.
            >>> seeking_alpha_finance = seeking_alpha_client.sectors(sector='financial')
        """

        # Grab the data.
        data = self.news_parser._make_request(
            url=self.urls['tag'].format(topic=sector)
        )

        return data
