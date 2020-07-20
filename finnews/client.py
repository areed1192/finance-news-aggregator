import json

from typing import List
from typing import Dict
from typing import Union

from finnews.cnbc import CNBC


class News():

    """
    Represents the main News Client that is used to access 
    the different news providers.
    """

    def __init__(self):
        """
        Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc  
        """

        self._cnbc_client = None

    def __repr__(self):
        pass

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

    def cnn_finance(self):
        pass

    def yahoo_finance(self):
        pass

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
        file_name = r'samples\responses\{name}.jsonc'.format(name=file_name)

        # Dump the content.
        with open(file_name, 'w+') as news_data:
            json.dump(obj=content, fp=news_data, indent=4)
