"""
==========================================================
CONFIGURATION
Institutional Trading Bot v2.0
==========================================================
"""

# ==========================================================
# TELEGRAM
# ==========================================================

BOT_TOKEN = "8593585531:AAFdwMBzzEgUX5mjI0ZM0h0i9EtAKcgHiF0"

# ==========================================================
# DATA SOURCE
# ==========================================================

DEFAULT_EXCHANGE = "PSX"

TIMEFRAMES = {
    "5m": "5m",
    "15m": "15m",
    "30m": "30m",
    "1h": "1h",
    "4h": "4h",
    "1d": "1d",
    "1w": "1w",
    "1m": "1M",      # Monthly
}

DEFAULT_TIMEFRAME = "1d"
DEFAULT_BARS = 500

# ==========================================================
# ANALYSIS SETTINGS
# ==========================================================

MIN_REQUIRED_BARS = 300

SWING_LOOKBACK = 3

VOLUME_PROFILE_BINS = 24

VALUE_AREA_PERCENT = 0.70

ATR_PERIOD = 14

EMA_PERIODS = [9, 20, 50, 100, 200]

SMA_PERIODS = [20, 50, 100, 200]

HMA_PERIOD = 55

RSI_PERIOD = 14

ADX_PERIOD = 14

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

BB_PERIOD = 20
BB_STD = 2

DONCHIAN_PERIOD = 20

VWAP_PRICE = "hlc3"

# ==========================================================
# VOLUME PROFILE
# ==========================================================

VP_LOOKBACK = 300

SESSION_VP_LOOKBACK = 100

# ==========================================================
# VWAP SETTINGS
# ==========================================================

ENABLE_SESSION_VWAP = True
ENABLE_15M_VWAP = True
ENABLE_1H_VWAP = True
ENABLE_4H_VWAP = True
ENABLE_DAILY_VWAP = True
ENABLE_WEEKLY_VWAP = True
ENABLE_MONTHLY_VWAP = True

ENABLE_ANCHORED_SWING_HIGH = True
ENABLE_ANCHORED_SWING_LOW = True
ENABLE_ANCHORED_BOS = True
ENABLE_ANCHORED_CHOCH = True
ENABLE_ANCHORED_BREAKOUT = True

# ==========================================================
# SCORING WEIGHTS
# ==========================================================

WEIGHTS = {
    "trend": 10,
    "structure": 10,
    "liquidity": 10,
    "volume": 10,
    "momentum": 10,
    "orderflow": 10,
    "risk": 10,
    "higher_timeframe": 20,
    "institutional": 20,
}

MAX_SCORE = 100

# ==========================================================
# RISK SETTINGS
# ==========================================================

MIN_RISK_REWARD = 2.0

DEFAULT_RISK_PER_TRADE = 0.02

MAX_STOP_ATR = 3.0

# ==========================================================
# CONFIDENCE THRESHOLDS
# ==========================================================

EXCEPTIONAL_SCORE = 95
HIGH_PROBABILITY_SCORE = 90
WAIT_SCORE = 85

# ==========================================================
# OUTPUT
# ==========================================================

ROUND_DIGITS = 2

SHOW_DEBUG = False

LOG_LEVEL = "INFO"

# ==========================================================
# VERSION
# ==========================================================

BOT_NAME = "Institutional Trading Bot"

BOT_VERSION = "2.0"

AUTHOR = "Muhammad Shahbaz"
