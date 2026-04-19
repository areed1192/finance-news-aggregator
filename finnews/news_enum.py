"""Enum definitions for various news categories from different providers."""

from enum import Enum


# ---------------------------------------------------------------------------
# CNBC enums
# ---------------------------------------------------------------------------


class CNBCTopNews(Enum):
    """Enum for the top news topics on CNBC."""

    TOP_NEWS = 100003114
    WORLD_NEWS = 100727362
    US_NEWS = 15837362
    ASIA_NEWS = 19832390
    EUROPE_NEWS = 19794221
    BUSINESS = 10001147
    EARNINGS = 15839135
    COMMENTARY = 100370673
    ECONOMY = 20910258
    FINANCE = 10000664
    TECHNOLOGY = 19854910
    POLITICS = 10000113
    HEALTH_CARE = 10000108
    REAL_ESTATE = 10000115
    WEALTH = 10001054
    AUTOS = 10000101
    ENERGY = 19836768
    MEDIA = 10000110
    RETAIL = 10000116
    TRAVEL = 10000739
    SMALL_BUSINESS = 44877279


class CNBCInvesting(Enum):
    """Enum for the investing topics on CNBC."""

    INVESTING = 15839069
    FINANCIAL_ADVISORS = 100646281
    PERSONAL_FINANCE = 21324812


class CNBCBlogs(Enum):
    """Enum for the blogs topics on CNBC."""

    CHARTING_ASIA = 23103686
    FUNNY_BUSINESS = 17646093
    MARKET_INSIDER = 20409666
    NETNET = 38818154
    TRADER_TALK = 20398120
    BUFFETT_WATCH = 19206666


class CNBCTVVideoAndTV(Enum):
    """Enum for the videos and TV topics on CNBC."""

    TOP_VIDEO = 15839263
    DIGITAL_WORKSHOP = 100616801
    LATEST_VIDEO = 100004038
    CEO_INTERVIEWS = 100004032
    ANALYST_INTERVIEWS = 100004033
    MUST_WATCH = 101014894
    SQUAWK_BOX = 15838368
    SQUAWK_ON_THE_STREET = 15838381
    POWER_LUNCH = 15838342
    STREET_SIGNS = 15838408
    OPTIONS_ACTION = 28282083
    CLOSING_BELL = 15838421
    FAST_MONEY = 15838499
    MAD_MONEY = 15838459
    KUDLOW_REPORT = 15838446
    FUTURES_NOW = 48227449
    SUZE_ORMAN = 15838523


class CNBCTVProgramsEurope(Enum):
    """Enum for the TV programs in Europe topics on CNBC."""

    CAPITAL_CONNECTION = 17501773
    SQUAWK_BOX_EUROPE = 15838652
    WORLDWIDE_EXCHANGE = 15838355


class CNBCTVProgramsAsia(Enum):
    """Enum for the TV programs in Asia topics on CNBC."""

    SQUAWK_BOX_ASIA = 15838831
    THE_CALL = 37447855


# ---------------------------------------------------------------------------
# MarketWatch enums
# ---------------------------------------------------------------------------


class MarketWatch(Enum):
    """Enum for the MarketWatch news topics."""

    TOP_STORIES = "mw_topstories"
    REAL_TIME_HEADLINES = "mw_realtimeheadlines"
    BULLETINS = "bulletins"
    MARKET_PULSE = "mw_marketpulse"
