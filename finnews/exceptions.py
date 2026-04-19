"""Custom exception hierarchy for the finnews package."""

from __future__ import annotations


class FinnewsError(Exception):
    """Base exception for all finnews errors."""


class InvalidTopicError(FinnewsError, KeyError):
    """Raised when an unrecognised topic key is passed to a provider.

    Inherits from ``KeyError`` so existing ``except KeyError`` handlers
    continue to work.
    """


class FeedRequestError(FinnewsError):
    """Raised when an HTTP request for an RSS feed fails."""


class FeedParseError(FinnewsError):
    """Raised when RSS/XML content cannot be parsed."""
