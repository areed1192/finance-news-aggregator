"""Async news client for concurrent feed fetching via httpx.

Requires the ``async`` extra: ``pip install fin-news[async]``
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any

import defusedxml.ElementTree as ET

from finnews.exceptions import FeedParseError, FeedRequestError
from finnews.parser import (
    NewsParser,
    _cache_key,
    _check_cache,
    _store_cache,
)

logger = logging.getLogger(__name__)


def _require_httpx():
    """Import *httpx* at runtime or raise a helpful error."""

    try:
        import httpx  # pylint: disable=import-outside-toplevel
        return httpx
    except ImportError as exc:
        raise ImportError(
            "httpx is required for async support. "
            "Install it with: pip install fin-news[async]"
        ) from exc


class AsyncNews:
    """Async client for concurrent RSS feed fetching.

    Uses ``httpx.AsyncClient`` for non-blocking HTTP and delegates
    XML parsing to the existing synchronous ``NewsParser``.

    ### Usage:
    ----
        >>> import asyncio
        >>> from finnews.async_client import AsyncNews
        >>>
        >>> async def main():
        ...     async with AsyncNews() as client:
        ...         articles = await client.fetch(
        ...             'https://feeds.content.dowjones.io/public/rss/mw_topstories',
        ...             parser_client='market_watch',
        ...         )
        ...         print(len(articles))
        ...
        >>> asyncio.run(main())
    """

    def __init__(self, cache_ttl: int = 0) -> None:
        """Initialize the async news client.

        ### Arguments:
        ----
        cache_ttl (int): Time-to-live in seconds for cached responses.
            Set to 0 (default) to disable caching.
        """

        self._cache_ttl = cache_ttl
        self._client: Any = None

    async def __aenter__(self) -> AsyncNews:
        httpx_mod = _require_httpx()
        from fake_useragent import UserAgent  # pylint: disable=import-outside-toplevel

        self._client = httpx_mod.AsyncClient(
            headers={"user-agent": UserAgent().edge},
            timeout=10.0,
        )
        return self

    async def __aexit__(self, *args: Any) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def fetch(
        self,
        url: str,
        parser_client: str = "cnbc",
        params: dict | None = None,
    ) -> list[dict]:
        """Fetch and parse a single RSS feed URL.

        ### Arguments:
        ----
        url (str): The RSS feed URL.
        parser_client (str): Parser client ID for XML namespace
            handling (e.g. ``'cnbc'``, ``'market_watch'``).
        params (dict | None): Optional query parameters.

        ### Returns:
        ----
        list[dict]: Parsed article dictionaries.
        """

        if self._client is None:
            raise RuntimeError(
                "Use 'async with AsyncNews() as client:' context manager."
            )

        # Check the shared cache.
        key = None
        if self._cache_ttl > 0:
            key = _cache_key(url, params)
            cached = _check_cache(key, self._cache_ttl)
            if cached is not None:
                logger.debug("Async cache hit for %s", url)
                return cached

        try:
            response = await self._client.get(url, params=params)
            response.raise_for_status()
        except Exception as exc:
            raise FeedRequestError(f"Failed to fetch {url}: {exc}") from exc

        parser = NewsParser(client=parser_client)
        try:
            data = parser.parse_response(response_content=response.content)
        except ET.ParseError as exc:
            raise FeedParseError(
                f"Failed to parse response from {url}: {exc}"
            ) from exc

        if key is not None:
            _store_cache(key, data)

        return data

    async def fetch_multiple(
        self,
        urls: dict[str, str],
        parser_client: str = "cnbc",
    ) -> dict[str, list[dict]]:
        """Fetch multiple RSS feed URLs concurrently.

        ### Arguments:
        ----
        urls (dict[str, str]): Mapping of label to RSS feed URL.
        parser_client (str): Parser client ID for XML namespace handling.

        ### Returns:
        ----
        dict[str, list[dict]]: Mapping of label to parsed articles.
            Failed feeds are omitted from the result.
        """

        async def _fetch_one(
            label: str, url: str,
        ) -> tuple[str, list[dict] | None]:
            try:
                data = await self.fetch(
                    url, parser_client=parser_client,
                )
                return (label, data)
            except (FeedRequestError, FeedParseError):
                logger.warning("Failed to fetch %s: %s", label, url)
                return (label, None)

        tasks = [_fetch_one(label, url) for label, url in urls.items()]
        results = await asyncio.gather(*tasks)

        return {
            label: data for label, data in results if data is not None
        }
