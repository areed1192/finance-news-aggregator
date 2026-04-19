"""finnews — A finance news aggregator for collecting articles on market topics."""

from finnews.article import NewsArticle, NewsFeed
from finnews.client import News
from finnews.exceptions import (
    FeedParseError,
    FeedRequestError,
    FinnewsError,
    InvalidTopicError,
)
from finnews.parser import clear_cache

__version__ = "0.1.3"
__all__ = [
    "News",
    "NewsArticle",
    "NewsFeed",
    "FinnewsError",
    "InvalidTopicError",
    "FeedRequestError",
    "FeedParseError",
    "clear_cache",
]
