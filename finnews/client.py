"""Facade client providing unified access to all news provider clients."""

from __future__ import annotations

import json
import pathlib

from typing import List
from typing import Dict

from finnews.cnbc import CNBC
from finnews.nasdaq import NASDAQ
from finnews.market_watch import MarketWatch
from finnews.sp_global import SPGlobal
from finnews.seeking_alpha import SeekingAlpha
from finnews.cnn_finance import CNNFinance
from finnews.wsj import WallStreetJournal
from finnews.yahoo_finance import YahooFinance


class News:  # pylint: disable=too-many-instance-attributes
    """
    ### Overview:
    ----
    Represents the main News Client that is used to access
    the different news providers.
    """

    def __init__(self, cache_ttl: int = 0) -> None:
        """Initalizes the main `News` client.

        ### Arguments:
        ----
        cache_ttl (int): Time-to-live in seconds for cached feed
            responses.  Set to 0 (default) to disable caching.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Or enable 5-minute caching.
            >>> news_client = News(cache_ttl=300)
        """

        self._cache_ttl = cache_ttl
        self._cnbc_client = None
        self._nasdaq_client = None
        self._market_watch_client = None
        self._sp_global_client = None
        self._seeking_alpha_client = None
        self._cnn_finance_client = None
        self._wsj_client = None
        self._yahoo_finance_client = None

    def __repr__(self) -> str:
        """Represents the string representation of the client object.

        ### Returns:
        ----
        (str): The string representation.
        """
        return "<NewsClient Connected: True'>"

    @property
    def cnbc(self) -> CNBC:
        """Returns a new instance of the `CNBC` news client.

        ### Returns:
        ----
        CNBC: The `CNBC` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNBC News Client.
            >>> cnbc_news_client = news_client.cnbc
        """

        if self._cnbc_client is None:
            self._cnbc_client = CNBC(cache_ttl=self._cache_ttl)

        return self._cnbc_client

    @property
    def nasdaq(self) -> NASDAQ:
        """Returns a new instance of the `NASDAQ` news client.

        ### Returns:
        ----
        NASDAQ: The `NASDAQ` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the NASDAQ News Client.
            >>> nasdaq_news_client = news_client.nasdaq
        """

        if self._nasdaq_client is None:
            self._nasdaq_client = NASDAQ(cache_ttl=self._cache_ttl)

        return self._nasdaq_client

    @property
    def market_watch(self) -> MarketWatch:
        """Returns a new instance of the `MarketWatch` news client.

        ### Returns:
        ----
        MarketWatch: The `MarketWatch` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the MarketWatch News Client.
            >>> market_watch_client = news_client.market_watch
        """

        if self._market_watch_client is None:
            self._market_watch_client = MarketWatch(cache_ttl=self._cache_ttl)

        return self._market_watch_client

    @property
    def sp_global(self) -> SPGlobal:
        """Returns a new instance of the `SPGlobal` news client.

        ### Returns:
        ----
        SPGlobal: The `SPGlobal` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SPGlobal News Client.
            >>> sp_global_client = news_client.sp_global
        """

        if self._sp_global_client is None:
            self._sp_global_client = SPGlobal(cache_ttl=self._cache_ttl)

        return self._sp_global_client

    @property
    def seeking_alpha(self) -> SeekingAlpha:
        """Returns a new instance of the `SeekingAlpha` news client.

        ### Returns:
        ----
        SeekingAlpha: The `SeekingAlpha` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the SeekingAlpha News Client.
            >>> seeking_alpha_client = news_client.seeking_alpha
        """

        if self._seeking_alpha_client is None:
            self._seeking_alpha_client = SeekingAlpha(cache_ttl=self._cache_ttl)

        return self._seeking_alpha_client

    @property
    def cnn_finance(self) -> CNNFinance:
        """Returns a new instance of the `CNNFinance` news client.

        ### Returns:
        ----
        CNNFinance: The `CNNFinance` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the CNN Finance News Client.
            >>> cnn_finance_client = news_client.cnn_finance
        """

        if self._cnn_finance_client is None:
            self._cnn_finance_client = CNNFinance(cache_ttl=self._cache_ttl)

        return self._cnn_finance_client

    @property
    def wsj(self) -> WallStreetJournal:
        """Returns a new instance of the `WallStreetJournal` news client.

        ### Returns:
        ----
        WallStreetJournal: The `WallStreetJournal` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Wall Street Journal News Client.
            >>> wsj_client = news_client.wsj
        """

        if self._wsj_client is None:
            self._wsj_client = WallStreetJournal(cache_ttl=self._cache_ttl)

        return self._wsj_client

    @property
    def yahoo_finance(self) -> YahooFinance:
        """Returns a new instance of the `YahooFinance` news client.

        ### Returns:
        ----
        YahooFinance: The `YahooFinance` news client that can be used to
            query different RSS feeds by topics.

        ### Usage:
        ----
            >>> from finnews.client import News

            >>> # Create a new instance of the News Client.
            >>> news_client = News()

            >>> # Grab the Yahoo Finance News Client.
            >>> yahoo_finance_client = news_client.yahoo_finance
        """

        if self._yahoo_finance_client is None:
            self._yahoo_finance_client = YahooFinance(cache_ttl=self._cache_ttl)

        return self._yahoo_finance_client

    def save_to_file(self, content: List[Dict], file_name: str) -> None:
        """Saves the news content to a JSONC file.

        ### Arguments:
        ----
        content (List[Dict]): A news collection list.

        file_name (str): The name of the file, with no file extension
            included.

        ### Usage:
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

        # Sanitize the file name to prevent path traversal.
        base_dir = pathlib.Path("samples/responses").resolve()
        target = (base_dir / f"{file_name}.jsonc").resolve()
        if not str(target).startswith(str(base_dir)):
            raise ValueError(
                f"Invalid file_name: '{file_name}' would write outside the responses directory."
            )

        # Ensure the directory exists.
        target.parent.mkdir(parents=True, exist_ok=True)

        # Dump the content.
        with open(file=str(target), mode="w+", encoding="utf-8") as news_data:
            json.dump(obj=content, fp=news_data, indent=2)
