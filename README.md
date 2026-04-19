# Finance News Aggregator

[![PyPI version](https://img.shields.io/pypi/v/fin-news)](https://pypi.org/project/fin-news/)
[![Python versions](https://img.shields.io/pypi/pyversions/fin-news)](https://pypi.org/project/fin-news/)
[![Build Status](https://github.com/areed1192/finance-news-aggregator/actions/workflows/python-package.yml/badge.svg)](https://github.com/areed1192/finance-news-aggregator/actions/workflows/python-package.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Providers](#providers)
  - [CNBC](#cnbc)
  - [MarketWatch](#marketwatch)
  - [NASDAQ](#nasdaq)
  - [S\&P Global](#sp-global)
  - [CNN Finance](#cnn-finance)
  - [Seeking Alpha](#seeking-alpha)
  - [Wall Street Journal](#wall-street-journal)
  - [Yahoo Finance](#yahoo-finance)
- [Structured Models](#structured-models)
- [Enums](#enums)
- [API Reference](#api-reference)
- [Comparison with Alternatives](#comparison-with-alternatives)
- [Contributing](#contributing)
- [Support](#support)

---

## Overview

Current Version: **0.1.3**

The `finnews` library collects news articles from 8 financial news providers via their RSS feeds. It provides a clean facade pattern — create one `News()` client and access any provider through properties.

**Features:**

- 8 providers with ~84 feed methods
- Enum-based topic selection for CNBC and MarketWatch
- Automatic retry with exponential backoff
- User-Agent rotation to avoid bot detection
- Structured `NewsArticle` / `NewsFeed` dataclasses with Jupyter HTML rendering
- Secure XML parsing via `defusedxml`

---

## Installation

```bash
pip install fin-news
```

Upgrade to the latest version:

```bash
pip install --upgrade fin-news
```

---

## Quick Start

```python
from finnews import News

# Create the main client.
news_client = News()

# Fetch top CNBC news.
cnbc = news_client.cnbc
top_news = cnbc.news_feed(topic='top_news')

# Each item is a dictionary with title, link, description, etc.
for article in top_news:
    print(article['title'])
```

---

## Providers

### CNBC

```python
cnbc = news_client.cnbc

# List all available topic keys.
print(cnbc.topics)

# Fetch by topic string.
articles = cnbc.news_feed(topic='top_news')
investing = cnbc.investing_feeds(topic='investing')
blogs = cnbc.blogs(topic='charting_asia')
tv = cnbc.videos_and_tv(topic='top_video')

# Fetch all feeds at once.
all_feeds = cnbc.all_feeds()
```

### MarketWatch

```python
market_watch = news_client.market_watch

# List all available topic keys.
print(market_watch.topics)

# Fetch by topic string.
top = market_watch.top_stories()
headlines = market_watch.real_time_headlines()
commentary = market_watch.commentary()

# Or use a specific topic method.
pulse = market_watch.market_pulse()
```

### NASDAQ

```python
nasdaq = news_client.nasdaq

# List all available feed methods.
print(nasdaq.feeds)

# Fetch feeds.
commodities = nasdaq.commodities_feed()
crypto = nasdaq.cryptocurrency_feed()
ai_news = nasdaq.artificial_intelligence_feed()
earnings = nasdaq.earnings_feed()

# Fetch by ticker symbol.
ticker_news = nasdaq.ticker_feed(ticker_symbol='AAPL')
```

### S&P Global

```python
sp_global = news_client.sp_global

# List all available feed methods.
print(sp_global.feeds)

# Fetch feeds.
research = sp_global.research()
indices = sp_global.all_indices()
commentary = sp_global.market_commentary()
```

### CNN Finance

```python
cnn = news_client.cnn_finance

# List all available feed methods.
print(cnn.feeds)

# Fetch feeds.
top_stories = cnn.top_stories()
markets = cnn.markets()
technology = cnn.technology()
economy = cnn.economy()
```

### Seeking Alpha

```python
seeking_alpha = news_client.seeking_alpha

# List all available feed methods.
print(seeking_alpha.feeds)

# Fetch feeds.
latest = seeking_alpha.latest_articles()
popular = seeking_alpha.most_popular_articles()

# Fetch by ticker or sector.
aapl = seeking_alpha.stocks(ticker='AAPL')
tech = seeking_alpha.sectors(sector='technology')
```

### Wall Street Journal

```python
wsj = news_client.wsj

# List all available feed methods.
print(wsj.feeds)

# Fetch feeds.
market_news = wsj.market_news()
world = wsj.world_news()
opinions = wsj.opinions()
```

### Yahoo Finance

```python
yahoo = news_client.yahoo_finance

# List all available feed methods.
print(yahoo.feeds)

# Fetch general news.
news = yahoo.news()

# Fetch headlines for specific symbols.
headlines = yahoo.headlines(symbols=['AAPL', 'MSFT'])
```

---

## Structured Models

Raw dictionaries can be converted to `NewsArticle` and `NewsFeed` dataclasses for IDE autocomplete and Jupyter rendering:

```python
from finnews import News, NewsArticle, NewsFeed

news_client = News()
raw = news_client.cnbc.news_feed(topic='top_news')

# Single article
article = NewsArticle.from_dict(raw[0], source='cnbc')
print(article.title, article.link)

# Full feed collection
feed = NewsFeed.from_dicts(raw, source='cnbc')
print(len(feed), "articles")

# In Jupyter notebooks, articles and feeds render as HTML automatically.
feed  # displays an HTML table
```

---

## Enums

CNBC and MarketWatch support enum-based topic selection:

```python
from finnews import News
from finnews.news_enum import CNBCTopNews, MarketWatch as MWEnum

news_client = News()

# CNBC with enum.
articles = news_client.cnbc.news_feed(topic=CNBCTopNews.REAL_ESTATE)

# MarketWatch with enum.
articles = news_client.market_watch.top_stories()
```

Available CNBC enums: `CNBCTopNews`, `CNBCInvesting`, `CNBCBlogs`, `CNBCTVVideoAndTV`, `CNBCTVProgramsEurope`, `CNBCTVProgramsAsia`

---

## API Reference

### Entry Point

| Class | Description |
|-------|-------------|
| `News()` | Main facade — access all providers via properties |

### Provider Properties

| Property | Class | Topics/Feeds |
|----------|-------|-------------|
| `news.cnbc` | `CNBC` | `.topics` — 54 topic keys |
| `news.market_watch` | `MarketWatch` | `.topics` — 13 topic keys |
| `news.nasdaq` | `NASDAQ` | `.feeds` — 22 feed methods |
| `news.sp_global` | `SPGlobal` | `.feeds` — 12 feed methods |
| `news.cnn_finance` | `CNNFinance` | `.feeds` — 22 feed methods |
| `news.seeking_alpha` | `SeekingAlpha` | `.feeds` — 13 feed methods |
| `news.wsj` | `WallStreetJournal` | `.feeds` — 6 feed methods |
| `news.yahoo_finance` | `YahooFinance` | `.feeds` — 2 feed methods |

### Data Models

| Class | Description |
|-------|-------------|
| `NewsArticle` | Dataclass: `title`, `link`, `description`, `published`, `source`, `extra` |
| `NewsFeed` | Collection of `NewsArticle` — iterable, indexable, `len()` support |

### Exceptions

| Exception | Description |
|-----------|-------------|
| `FinnewsError` | Base exception for all finnews errors |
| `InvalidTopicError` | Raised for unknown topic keys (also a `KeyError`) |
| `FeedRequestError` | HTTP request failures |
| `FeedParseError` | XML parsing failures |

### Utility

| Method | Description |
|--------|-------------|
| `news.save_to_file(content, file_name)` | Save results to `samples/responses/<file_name>.jsonc` |

---

## Comparison with Alternatives

| Feature | `fin-news` | `feedparser` | `gnews` | `newscatcher` |
|---------|-----------|-------------|---------|--------------|
| Finance-focused providers | **8 providers** | Any RSS | Google News | News API |
| Topic-based feeds | Yes | N/A | Yes | Yes |
| Keyword search | No | N/A | Yes | Yes |
| Structured models | **Yes** (`NewsArticle`) | Yes | Yes | Yes |
| Enum topic selection | **Yes** | No | No | No |
| Retry with backoff | **Yes** | N/A | Yes | No |
| Jupyter rendering | **Yes** | No | No | No |
| Async support | No | No | No | No |
| No API key required | **Yes** | Yes | Yes | No |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup, testing, and PR guidelines.

---

## Support

**Patreon:** Help support this project by donating to the [Patreon Page](https://www.patreon.com/sigmacoding).

**YouTube:** Watch more content on [Sigma Coding](https://www.youtube.com/c/SigmaCoding).
