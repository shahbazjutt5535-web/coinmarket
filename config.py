# ==========================================================
# BOT CONFIGURATION
# ==========================================================

BOT_TOKEN = "8593585531:AAFdwMBzzEgUX5mjI0ZM0h0i9EtAKcgHiF0"

# ==========================================================
# TV DATA CONFIG
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
    "1m": "1m"
}

DEFAULT_TIMEFRAME = "1d"

# Number of candles fetched from TradingView
DEFAULT_BARS = 500
MIN_BARS = 500
MAX_BARS = 2000

# ==========================================================
# LOOKBACK SETTINGS
# ==========================================================

LOOKBACK_SWING = 3
LOOKBACK_ATR = 14
LOOKBACK_VOLUME = 50
LOOKBACK_PROFILE = 200
LOOKBACK_STRUCTURE = 200
LOOKBACK_WYCKOFF = 200

# ==========================================================
# RISK / STRATEGY SETTINGS
# ==========================================================

RISK_PER_TRADE = 0.02      # 2%
MAX_TRADES_PER_DAY = 5

MIN_RISK_REWARD = 2.0
TARGET_RISK_REWARD = 3.0
MAX_RISK_REWARD = 5.0

ATR_STOP_MULTIPLIER = 1.0
ATR_TARGET_MULTIPLIER = 2.0

# ==========================================================
# FEATURE FLAGS
# ==========================================================

ENABLE_MULTI_TIMEFRAME = True

ENABLE_VWAP = True
ENABLE_ANCHORED_VWAP = True

ENABLE_VOLUME_PROFILE = True
ENABLE_MARKET_PROFILE = True

ENABLE_SMART_MONEY = True
ENABLE_WYCKOFF = True

ENABLE_SCORE_ENGINE = True
ENABLE_CONFLUENCE_ENGINE = True
ENABLE_PROBABILITY_ENGINE = True
ENABLE_DYNAMIC_TP_MODEL = True
ENABLE_ADAPTIVE_WEIGHT_ENGINE = True

ENABLE_DASHBOARD = True

# ==========================================================
# VWAP SETTINGS
# ==========================================================

VWAP_SESSION = True
VWAP_15M = True
VWAP_1H = True
VWAP_4H = True
VWAP_DAILY = True
VWAP_WEEKLY = True
VWAP_MONTHLY = True

ANCHOR_SWING_HIGH = True
ANCHOR_SWING_LOW = True
ANCHOR_BOS = True
ANCHOR_CHOCH = True
ANCHOR_BREAKOUT = True

# ==========================================================
# CONFLUENCE SETTINGS
# ==========================================================

MIN_CONFLUENCE_FOR_ENTRY = 7
HIGH_CONFLUENCE = 9
MAX_CONFLUENCE = 12

# ==========================================================
# INSTITUTIONAL SCORE WEIGHTS
# ==========================================================

TREND_WEIGHT = 15
STRUCTURE_WEIGHT = 20
SMART_MONEY_WEIGHT = 20
LIQUIDITY_WEIGHT = 10
VOLUME_WEIGHT = 10
MOMENTUM_WEIGHT = 10
VOLATILITY_WEIGHT = 5
RISK_WEIGHT = 10

TOTAL_SCORE = 100

# ==========================================================
# DECISION SETTINGS
# ==========================================================

EXCEPTIONAL_SETUP = 95
HIGH_PROBABILITY_SETUP = 90
WAIT_CONFIRMATION = 85
NO_TRADE = 84

# ==========================================================
# MARKET HEALTH
# ==========================================================

ENABLE_MARKET_HEALTH = True

MARKET_HEALTH_TREND_WEIGHT = 30
MARKET_HEALTH_VOLUME_WEIGHT = 20
MARKET_HEALTH_STRUCTURE_WEIGHT = 25
MARKET_HEALTH_VOLATILITY_WEIGHT = 10
MARKET_HEALTH_MOMENTUM_WEIGHT = 15

# ==========================================================
# ENTRY QUALITY
# ==========================================================

ENABLE_ENTRY_TIMING_ENGINE = True

ENTRY_CONFIRMATIONS_REQUIRED = 5

# ==========================================================
# EXIT QUALITY
# ==========================================================

ENABLE_DYNAMIC_EXIT = True

# ==========================================================
# SCENARIO ENGINE
# ==========================================================

ENABLE_SCENARIO_ENGINE = True

MAX_SCENARIOS = 3

# ==========================================================
# PROBABILITY ENGINE
# ==========================================================

MIN_SUCCESS_PROBABILITY = 70
HIGH_SUCCESS_PROBABILITY = 85
VERY_HIGH_SUCCESS_PROBABILITY = 90

# ==========================================================
# DASHBOARD
# ==========================================================

SHOW_SCORE_BREAKDOWN = True
SHOW_PROBABILITY = True
SHOW_CONFLUENCE = True
SHOW_VWAP = True
SHOW_HEALTH_SCORE = True
SHOW_RISK_GRADE = True

# ==========================================================
# LOGGING
# ==========================================================

LOG_LEVEL = "INFO"

# ==========================================================
# DEBUG
# ==========================================================

DEBUG_MODE = False
