import json

from typing import List
from typing import Dict
from typing import Union

from finnews.cnbc import CNBC
from finnews.nasdaq import NASDAQ
from finnews.market_watch import MarketWatch
from finnews.sp_global import SPGlobal


class News():

    """
    Represents the main News Client that is used to access 
    the different news providers.
    """

    def __init__(self) -> None:
        """Initalizes the main `News` client.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()
        """

        self._cnbc_client = None
        self._nasdaq_client = None
        self._market_watch_client = None
        self._sp_global_client = None

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        Returns:
        ----
        (str): The string representation.
        """
        return "<NewsClient Connected: True'>"

    @property
    def cnbc(self) -> CNBC:
        """Returns a new instance of the `CNBC` news client.

        Returns:
        ----
        CNBC: The `CNBC` news client that can be used to
            query different RSS feeds by topics.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc        
        """

        self._cnbc_client = CNBC()

        return self._cnbc_client

    @property
    def nasdaq(self) -> NASDAQ:
        """Returns a new instance of the `NASDAQ` news client.

        Returns:
        ----
        NASDAQ: The `NASDAQ` news client that can be used to
            query different RSS feeds by topics.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq       
        """

        self._nasdaq_client = NASDAQ()

        return self._nasdaq_client

    @property
    def market_Watch(self) -> MarketWatch:
        """Returns a new instance of the `MarketWatch` news client.

        Returns:
        ----
        MarketWatch: The `MarketWatch` news client that can be used to
            query different RSS feeds by topics.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_Watch_client = news_client.market_Watch       
        """

        self._market_watch_client = MarketWatch()

        return self._market_watch_client

    @property
    def sp_global(self) -> SPGlobal:
        """Returns a new instance of the `SPGlobal` news client.

        Returns:
        ----
        SPGlobal: The `SPGlobal` news client that can be used to
            query different RSS feeds by topics.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global       
        """

        self._sp_global_client = SPGlobal()

        return self._sp_global_client

    def save_to_file(self, content: List[Dict], file_name: str) -> None:
        """Saves the news content to a JSONC file.

        Arguments:
        ----
        content (List[Dict]): A news collection list.

        file_name (str): The name of the file, with no file extension
            included.

        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc

            >>> # Grab the top news.
            >>> cbnc_top_news = cnbc_news_client.news_feed(topic='top_news')   

            >>> # Save the data.
            >>> news_client.save_to_file(
                content=cbnc_top_news,
                file_name='cnbc_top_news'
            )
        """

        # Define the file name.
        file_name = 'samples/responses/{name}.jsonc'.format(name=file_name)

        # Dump the content.
        with open(file_name, 'w+') as news_data:
            json.dump(obj=content, fp=news_data, indent=2)
