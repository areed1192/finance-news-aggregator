"""Tests for the AsyncNews async client."""

import asyncio

import pytest

from finnews.async_client import AsyncNews


# ---------------------------------------------------------------------------
# Async client tests
# ---------------------------------------------------------------------------


class TestAsyncClientImport:
    """Tests for the async client module availability."""

    def test_async_news_importable(self):
        """Verify AsyncNews can be imported and instantiated."""
        client = AsyncNews()

        assert client is not None

    def test_async_news_requires_context_manager(self):
        """Verify fetch raises RuntimeError outside context manager."""

        async def _run():
            client = AsyncNews()
            with pytest.raises(RuntimeError):
                await client.fetch("https://example.com")

        asyncio.run(_run())
