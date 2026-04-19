"""RSS feed parser handling HTTP requests and XML-to-dict conversion."""

from __future__ import annotations

import logging
import time

import defusedxml.ElementTree as ET


import requests
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from finnews.exceptions import FeedRequestError, FeedParseError

logger = logging.getLogger(__name__)

# Module-level response cache: cache_key -> (timestamp, parsed_data)
_response_cache: dict[str, tuple[float, list[dict]]] = {}


def _cache_key(url: str, params: dict | None) -> str:
    """Build a deterministic cache key from URL and query params."""

    if params:
        suffix = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
        return f"{url}?{suffix}"
    return url


def _check_cache(key: str, ttl: float) -> list[dict] | None:
    """Return cached data if still valid, otherwise ``None``."""

    if key in _response_cache:
        timestamp, data = _response_cache[key]
        if time.time() - timestamp < ttl:
            return data
    return None


def _store_cache(key: str, data: list[dict]) -> None:
    """Store parsed data in the response cache."""

    _response_cache[key] = (time.time(), data)


def clear_cache() -> None:
    """Clear the entire response cache."""

    _response_cache.clear()


class NewsParser:  # pylint: disable=too-few-public-methods
    """
    ### Overview:
    ----
    Serves as the parser for each of the
    news clients.
    """

    def __init__(self, client: str, cache_ttl: int = 0) -> None:
        """Initializes the new parser client.

        ### Overview:
        ----
        To help standardize the parser process the
        `NewsParser` client is used to help make the
        request, parse the response, and organize the
        results for each of the news client.

        ### Arguments:
        ----
        client (str): The ID of the client you wish to use
            the parser for.
        cache_ttl (int): Time-to-live in seconds for cached responses.
            Set to 0 (default) to disable caching.

        ### Usage:
        ----
            >>> self.news_parser = NewsParser(client='cnbc')
        """

        self.client = client
        self.cache_ttl = cache_ttl
        self.paths = {
            "cnbc": "./channel/item",
            "nasdaq": "./channel/item",
            "market_watch": "./channel/item",
            "sp_global": ".channel/item",
            "seeking_alpha": ".channel/item",
            "cnn_finance": ".channel/item",
            "wsj": ".channel/item",
            "yahoo": ".channel/item",
        }

        self.namespaces = {
            "cnbc": ["{http://search.cnbc.com/rss/2.0/modules/siteContentMetadata}"],
            "nasdaq": [
                "{http://purl.org/dc/elements/1.1/}",
                "{http://nasdaq.com/reference/feeds/1.0}",
                "{http://purl.org/dc/elements/1.1/}",
            ],
            "market_watch": ["{http://rssnamespace.org/feedburner/ext/1.0}"],
            "sp_global": [""],
            "seeking_alpha": [
                "{http://search.yahoo.com/mrss/}",
                "{https://seekingalpha.com/api/1.0}",
            ],
            "cnn_finance": [
                "{http://rssnamespace.org/feedburner/ext/1.0}",
                "{http://search.yahoo.com/mrss/}",
            ],
            "wsj": [
                "{http://dowjones.net/rss/}",
                "{http://purl.org/rss/1.0/modules/content/}",
                "{http://search.yahoo.com/mrss/}",
            ],
            "yahoo": ["{http://search.yahoo.com/mrss/}"],
        }

    def parse_response(self, response_content: str | bytes) -> list[dict]:
        """Parses the text content from a request and ### Returns the news item collection.

        ### Arguments:
        ----
        response_content (str): The raw XML content from the RSS feed that
            needs to be parsed.

        ### Returns:
        ----
        List[Dict]: A list of news items objects.
        """

        # Parse the text.
        root = ET.fromstring(response_content)
        entries = []

        # Grab the path.
        path = self.paths[self.client]

        # Find all the news items.
        for news_item in root.findall(path):

            # Initialize a new dictionary.
            item_dict = {}

            # Loop through each element.
            for news_item_element in news_item.iter():

                # Grab the news tag.
                news_tag: str = news_item_element.tag

                # Replace the namespace.
                for path in self.namespaces[self.client]:

                    # Clean the tag.
                    news_tag = news_tag.replace(path, "")

                # Grab the text.
                if news_item_element.text:
                    news_value = news_item_element.text.strip()
                else:
                    news_value = ""

                # Store it — collect duplicate tags into lists.
                if news_tag in item_dict:
                    existing = item_dict[news_tag]
                    if isinstance(existing, list):
                        existing.append(news_value)
                    else:
                        item_dict[news_tag] = [existing, news_value]
                else:
                    item_dict[news_tag] = news_value

            entries.append(item_dict)

        return entries

    def make_request(self, url: str, params: dict | None = None) -> list[dict]:
        """Used to make a request for each of the news clients.

        Uses automatic retry with exponential backoff for transient
        HTTP errors (429, 500, 502, 503, 504).  When ``cache_ttl`` is
        set, responses are cached in memory and reused within the TTL.

        ### Arguments:
        ----
        url (str): The URL to request.

        params (dict): The paramters to pass through to the request.

        ### Returns:
        ----
        List[Dict]: A list of news items objects.
        """

        # Check the cache first.
        cache_hit_key = None
        if self.cache_ttl > 0:
            cache_hit_key = _cache_key(url, params)
            cached = _check_cache(cache_hit_key, self.cache_ttl)
            if cached is not None:
                logger.debug("Cache hit for %s", url)
                return cached

        # Fake the headers.
        headers = {"user-agent": UserAgent().edge}

        # Build a session with retry logic.
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        try:
            # Grab the response.
            response = session.get(url=url, headers=headers, params=params, timeout=10)

            # Raise an exception for HTTP errors.
            response.raise_for_status()
        except requests.RequestException as exc:
            raise FeedRequestError(f"Failed to fetch {url}: {exc}") from exc

        # Parse the response.
        try:
            data = self.parse_response(response_content=response.content)
        except ET.ParseError as exc:
            raise FeedParseError(f"Failed to parse response from {url}: {exc}") from exc

        # Store in cache.
        if cache_hit_key is not None:
            _store_cache(cache_hit_key, data)

        return data
