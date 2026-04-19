"""Tests for the custom exception hierarchy."""

import pytest

from finnews.exceptions import (
    FinnewsError,
    InvalidTopicError,
    FeedRequestError,
    FeedParseError,
)


# ---------------------------------------------------------------------------
# Exception hierarchy tests
# ---------------------------------------------------------------------------


class TestExceptionHierarchy:
    """Tests for the custom exception classes."""

    def test_finnews_error_is_base(self):
        """Verify all custom exceptions inherit from FinnewsError."""
        assert issubclass(InvalidTopicError, FinnewsError)
        assert issubclass(FeedRequestError, FinnewsError)
        assert issubclass(FeedParseError, FinnewsError)

    def test_invalid_topic_error_is_key_error(self):
        """Verify InvalidTopicError is also a KeyError for backward compat."""
        assert issubclass(InvalidTopicError, KeyError)

    def test_invalid_topic_caught_by_key_error(self):
        """Verify existing except-KeyError handlers still catch InvalidTopicError."""
        with pytest.raises(KeyError):
            raise InvalidTopicError("bad topic")

    def test_invalid_topic_caught_by_finnews_error(self):
        """Verify InvalidTopicError is caught by FinnewsError."""
        with pytest.raises(FinnewsError):
            raise InvalidTopicError("bad topic")
