# ==========================================================
# CONFIG.PY
# PART 1
# GLOBAL CONFIGURATION
# ==========================================================

"""
Bot 2 Configuration

Purpose:
Central configuration for all institutional calculations.
Only constants, parameters and settings are stored here.
No calculation logic should exist in this file.
"""

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

PROJECT_NAME = "PSX Institutional Trading Bot 2"

PROJECT_VERSION = "2.0.0"

PROJECT_STATUS = "Active"

AUTHOR = "Internal"

# ==========================================================
# GENERAL SETTINGS
# ==========================================================

DEBUG_MODE = False

LOGGING_ENABLED = True

STRICT_VALIDATION = True

ALLOW_PARTIAL_DATA = False

ROUND_DECIMALS = 2

PERCENT_DECIMALS = 2

PRICE_DECIMALS = 4

DEFAULT_LOOKBACK = 200

MIN_REQUIRED_CANDLES = 250

MAX_LOOKBACK = 1000

# ==========================================================
# DATA SETTINGS
# ==========================================================

REQUIRED_COLUMNS = [

    "open",
    "high",
    "low",
    "close",
    "volume"

]

PRICE_COLUMNS = [

    "open",
    "high",
    "low",
    "close"

]

# ==========================================================
# FEATURE FLAGS
# ==========================================================

ENABLE_MULTI_TIMEFRAME = True

ENABLE_INSTITUTIONAL_ENGINE = True

ENABLE_SMART_MONEY = True

ENABLE_VWAP_ENGINE = True

ENABLE_SCORE_ENGINE = True

ENABLE_PROBABILITY_ENGINE = True

ENABLE_CONFLUENCE_ENGINE = True

ENABLE_DASHBOARD = True

ENABLE_MARKET_STRUCTURE = True

ENABLE_VOLUME_ANALYSIS = True

ENABLE_VOLATILITY_ANALYSIS = True

ENABLE_ENTRY_ENGINE = True

ENABLE_EXIT_ENGINE = True

# ==========================================================
# DEFAULT VALUES
# ==========================================================

DEFAULT_SCORE = 50.0

DEFAULT_PROBABILITY = 50.0

DEFAULT_CONFIDENCE = 50.0

DEFAULT_BIAS = "NEUTRAL"

DEFAULT_TREND = "UNKNOWN"

DEFAULT_SIGNAL = "NONE"

DEFAULT_DIRECTION = "FLAT"

# ==========================================================
# SCORE LIMITS
# ==========================================================

MIN_SCORE = 0.0

MAX_SCORE = 100.0

MIN_PROBABILITY = 0.0

MAX_PROBABILITY = 100.0

# ==========================================================
# NUMERIC CONSTANTS
# ==========================================================

EPSILON = 1e-10

PERCENT_MULTIPLIER = 100.0

# ==========================================================
# END OF CONFIG.PY PART 1
# ==========================================================

# ==========================================================
# CONFIG.PY
# PART 2
# TIMEFRAME CONFIGURATION
# ==========================================================

# ==========================================================
# PRIMARY TIMEFRAME
# ==========================================================

PRIMARY_TIMEFRAME = "15m"

# ==========================================================
# MULTI TIMEFRAME LIST
# ==========================================================

SUPPORTED_TIMEFRAMES = [

    "15m",
    "1h",
    "4h",
    "1d",
    "1w"

]

# ==========================================================
# TIMEFRAME PRIORITY
# Higher number = Higher Priority
# ==========================================================

TIMEFRAME_PRIORITY = {

    "15m": 1,

    "1h": 2,

    "4h": 3,

    "1d": 4,

    "1w": 5

}

# ==========================================================
# TIMEFRAME WEIGHTS
# Used by Institutional Engine
# ==========================================================

TIMEFRAME_WEIGHTS = {

    "15m": 0.15,

    "1h": 0.20,

    "4h": 0.25,

    "1d": 0.25,

    "1w": 0.15

}

# ==========================================================
# TIMEFRAME LOOKBACK
# ==========================================================

TIMEFRAME_LOOKBACK = {

    "15m": 300,

    "1h": 300,

    "4h": 250,

    "1d": 200,

    "1w": 150

}

# ==========================================================
# MINIMUM REQUIRED CANDLES
# ==========================================================

TIMEFRAME_MIN_CANDLES = {

    "15m": 250,

    "1h": 250,

    "4h": 200,

    "1d": 150,

    "1w": 100

}

# ==========================================================
# CONFLUENCE SETTINGS
# ==========================================================

MIN_CONFLUENCE_TIMEFRAMES = 3

IDEAL_CONFLUENCE_TIMEFRAMES = 5

REQUIRED_HIGHER_TIMEFRAME_CONFIRMATION = True

ALLOW_LOWER_TIMEFRAME_OVERRIDE = False

# ==========================================================
# TREND ALIGNMENT
# ==========================================================

TREND_ALIGNMENT_REQUIRED = True

MIN_TREND_ALIGNMENT_SCORE = 60.0

# ==========================================================
# ENTRY FILTER
# ==========================================================

ENTRY_CONFIRMATION_TIMEFRAMES = [

    "15m",

    "1h",

    "4h"

]

# ==========================================================
# EXIT FILTER
# ==========================================================

EXIT_CONFIRMATION_TIMEFRAMES = [

    "15m",

    "1h"

]

# ==========================================================
# MTF SCORE LIMITS
# ==========================================================

MTF_MIN_SCORE = 0.0

MTF_MAX_SCORE = 100.0

# ==========================================================
# END OF CONFIG.PY PART 2
# ==========================================================

# ==========================================================
# CONFIG.PY
# PART 3
# INDICATOR PARAMETERS
# ==========================================================

# ==========================================================
# EMA SETTINGS
# ==========================================================

EMA_FAST = 20

EMA_MEDIUM = 50

EMA_SLOW = 100

EMA_LONG = 200

# ==========================================================
# HMA SETTINGS
# ==========================================================

HMA_PERIOD = 55

# ==========================================================
# SMA SETTINGS
# ==========================================================

SMA_FAST = 20

SMA_MEDIUM = 50

SMA_LONG = 200

# ==========================================================
# ATR SETTINGS
# ==========================================================

ATR_PERIOD = 14

ATR_VOLATILITY_PERIOD = 20

# ==========================================================
# RSI SETTINGS
# ==========================================================

RSI_PERIOD = 14

RSI_OVERBOUGHT = 70

RSI_OVERSOLD = 30

RSI_MIDLINE = 50

# ==========================================================
# MACD SETTINGS
# ==========================================================

MACD_FAST = 12

MACD_SLOW = 26

MACD_SIGNAL = 9

# ==========================================================
# ADX SETTINGS
# ==========================================================

ADX_PERIOD = 14

ADX_WEAK = 20

ADX_STRONG = 25

ADX_VERY_STRONG = 40

# ==========================================================
# DMI SETTINGS
# ==========================================================

DMI_PERIOD = 14

# ==========================================================
# AROON SETTINGS
# ==========================================================

AROON_PERIOD = 25

# ==========================================================
# BOLLINGER BAND SETTINGS
# ==========================================================

BB_PERIOD = 20

BB_STD = 2.0

# ==========================================================
# SUPERTREND SETTINGS
# ==========================================================

SUPERTREND_PERIOD = 10

SUPERTREND_MULTIPLIER = 3.0

# ==========================================================
# ICHIMOKU SETTINGS
# ==========================================================

ICHIMOKU_CONVERSION = 9

ICHIMOKU_BASE = 26

ICHIMOKU_SPAN_B = 52

ICHIMOKU_DISPLACEMENT = 26

# ==========================================================
# MOMENTUM SETTINGS
# ==========================================================

ROC_PERIOD = 10

MOMENTUM_PERIOD = 10

# ==========================================================
# VOLUME SETTINGS
# ==========================================================

VOLUME_SMA_PERIOD = 20

RELATIVE_VOLUME_PERIOD = 20

VOLUME_SPIKE_MULTIPLIER = 2.0

# ==========================================================
# VOLATILITY SETTINGS
# ==========================================================

HISTORICAL_VOLATILITY_PERIOD = 20

STANDARD_DEVIATION_PERIOD = 20

# ==========================================================
# SUPPORT / RESISTANCE SETTINGS
# ==========================================================

SUP_RES_LOOKBACK = 50

SWING_LOOKBACK = 20

LEVEL_TOUCH_TOLERANCE = 0.002

# ==========================================================
# MARKET STRUCTURE SETTINGS
# ==========================================================

STRUCTURE_LOOKBACK = 20

BOS_LOOKBACK = 20

CHOCH_LOOKBACK = 20

# ==========================================================
# PRICE POSITION SETTINGS
# ==========================================================

PRICE_POSITION_LOOKBACK = 20

ROLLING_MIDPOINT_LOOKBACK = 20

# ==========================================================
# END OF CONFIG.PY PART 3
# ==========================================================

# ==========================================================
# CONFIG.PY
# PART 4
# VWAP CONFIGURATION
# ==========================================================

# ==========================================================
# VWAP FEATURE FLAGS
# ==========================================================

ENABLE_SESSION_VWAP = True

ENABLE_15M_VWAP = True

ENABLE_1H_VWAP = True

ENABLE_4H_VWAP = True

ENABLE_DAILY_VWAP = True

ENABLE_WEEKLY_VWAP = True

ENABLE_MONTHLY_VWAP = True

ENABLE_ANCHORED_VWAP = True

ENABLE_VWAP_CONFLUENCE = True

# ==========================================================
# VWAP TIMEFRAMES
# ==========================================================

VWAP_TIMEFRAMES = [

    "15m",

    "1h",

    "4h",

    "1d",

    "1w",

    "1M"

]

# ==========================================================
# VWAP DISTANCE SETTINGS
# ==========================================================

VWAP_NEAR_PERCENT = 0.25

VWAP_CONFLUENCE_PERCENT = 0.50

VWAP_SUPPORT_PERCENT = 0.40

VWAP_RESISTANCE_PERCENT = 0.40

# ==========================================================
# VWAP TREND SETTINGS
# ==========================================================

VWAP_SLOPE_PERIOD = 5

VWAP_RISING_THRESHOLD = 0.0

VWAP_FALLING_THRESHOLD = 0.0

# ==========================================================
# ANCHORED VWAP SETTINGS
# ==========================================================

ANCHOR_SWING_LOOKBACK = 80

ANCHOR_BOS_LOOKBACK = 20

ANCHOR_CHOCH_LOOKBACK = 20

ANCHOR_BREAKOUT_LOOKBACK = 30

# ==========================================================
# BREAKOUT SETTINGS
# ==========================================================

BREAKOUT_RANGE_PERIOD = 20

BREAKOUT_MULTIPLIER = 1.50

# ==========================================================
# VWAP CONFLUENCE SETTINGS
# ==========================================================

MIN_VWAP_CONFLUENCE = 2

GOOD_VWAP_CONFLUENCE = 4

STRONG_VWAP_CONFLUENCE = 6

MAX_VWAP_SCORE = 100.0

# ==========================================================
# VWAP OUTPUT SETTINGS
# ==========================================================

SHOW_VWAP_DISTANCE = True

SHOW_VWAP_DIRECTION = True

SHOW_VWAP_SLOPE = True

SHOW_VWAP_CROSS = True

SHOW_VWAP_CONFLUENCE = True

SHOW_STRONGEST_SUPPORT_VWAP = True

SHOW_STRONGEST_RESISTANCE_VWAP = True

# ==========================================================
# VWAP SCORE WEIGHTS
# ==========================================================

VWAP_DISTANCE_WEIGHT = 25.0

VWAP_SLOPE_WEIGHT = 20.0

VWAP_TREND_WEIGHT = 20.0

VWAP_CROSS_WEIGHT = 15.0

VWAP_CONFLUENCE_WEIGHT = 20.0

# ==========================================================
# END OF CONFIG.PY PART 4
# ==========================================================

# ==========================================================
# CONFIG.PY
# PART 5
# INSTITUTIONAL SCORING CONFIGURATION
# ==========================================================

# ==========================================================
# MASTER SCORE WEIGHTS
# Total = 100
# ==========================================================

TREND_WEIGHT = 15.0

MOMENTUM_WEIGHT = 10.0

VOLUME_WEIGHT = 10.0

SMART_MONEY_WEIGHT = 15.0

MARKET_STRUCTURE_WEIGHT = 15.0

LIQUIDITY_WEIGHT = 10.0

VWAP_WEIGHT = 10.0

VOLATILITY_WEIGHT = 5.0

CONFLUENCE_WEIGHT = 10.0

INSTITUTIONAL_WEIGHT = 10.0

# ==========================================================
# MARKET HEALTH WEIGHTS
# ==========================================================

MARKET_HEALTH_WEIGHTS = {

    "trend": 25,

    "momentum": 15,

    "volume": 15,

    "structure": 15,

    "smart_money": 15,

    "liquidity": 10,

    "volatility": 5

}

# ==========================================================
# ENTRY QUALITY WEIGHTS
# ==========================================================

ENTRY_QUALITY_WEIGHTS = {

    "trend": 15,

    "confluence": 20,

    "smart_money": 20,

    "liquidity": 15,

    "vwap": 15,

    "volume": 10,

    "volatility": 5

}

# ==========================================================
# EXIT QUALITY WEIGHTS
# ==========================================================

EXIT_QUALITY_WEIGHTS = {

    "momentum": 20,

    "volume": 15,

    "vwap": 15,

    "liquidity": 15,

    "structure": 20,

    "volatility": 15

}

# ==========================================================
# INSTITUTIONAL BIAS WEIGHTS
# ==========================================================

BIAS_WEIGHTS = {

    "trend": 30,

    "market_structure": 20,

    "smart_money": 20,

    "vwap": 15,

    "momentum": 10,

    "volume": 5

}

# ==========================================================
# SCORE LIMITS
# ==========================================================

SCORE_MIN = 0.0

SCORE_MAX = 100.0

# ==========================================================
# SCORE LABELS
# ==========================================================

VERY_STRONG_SCORE = 90

STRONG_SCORE = 75

GOOD_SCORE = 60

AVERAGE_SCORE = 40

WEAK_SCORE = 20

# ==========================================================
# CONFLUENCE SETTINGS
# ==========================================================

MIN_SIGNAL_AGREEMENT = 3

GOOD_SIGNAL_AGREEMENT = 5

STRONG_SIGNAL_AGREEMENT = 7

MAX_SIGNAL_AGREEMENT = 10

# ==========================================================
# SCORE NORMALIZATION
# ==========================================================

ENABLE_SCORE_NORMALIZATION = True

NORMALIZED_SCORE_MIN = 0.0

NORMALIZED_SCORE_MAX = 100.0

# ==========================================================
# END OF CONFIG.PY PART 5
# ==========================================================

# ==========================================================
# CONFIG.PY
# PART 6
# PROBABILITY ENGINE CONFIGURATION
# ==========================================================

# ==========================================================
# MASTER PROBABILITY SETTINGS
# ==========================================================

ENABLE_PROBABILITY_ENGINE = True

PROBABILITY_MIN = 0.0

PROBABILITY_MAX = 100.0

DEFAULT_PROBABILITY = 50.0

# ==========================================================
# TRADE CONFIDENCE
# ==========================================================

TRADE_CONFIDENCE_WEIGHTS = {

    "institutional_score": 30,

    "confluence": 20,

    "trend": 15,

    "momentum": 10,

    "volume": 10,

    "market_structure": 10,

    "volatility": 5

}

# ==========================================================
# ENTRY QUALITY
# ==========================================================

ENTRY_QUALITY_MIN = 60.0

ENTRY_QUALITY_GOOD = 75.0

ENTRY_QUALITY_STRONG = 85.0

ENTRY_QUALITY_EXCELLENT = 95.0

# ==========================================================
# EXIT QUALITY
# ==========================================================

EXIT_QUALITY_MIN = 60.0

EXIT_QUALITY_GOOD = 75.0

EXIT_QUALITY_STRONG = 85.0

EXIT_QUALITY_EXCELLENT = 95.0

# ==========================================================
# PULLBACK PROBABILITY
# ==========================================================

PULLBACK_LOW = 30.0

PULLBACK_MEDIUM = 50.0

PULLBACK_HIGH = 70.0

PULLBACK_VERY_HIGH = 85.0

# ==========================================================
# BREAKOUT PROBABILITY
# ==========================================================

BREAKOUT_LOW = 30.0

BREAKOUT_MEDIUM = 50.0

BREAKOUT_HIGH = 70.0

BREAKOUT_VERY_HIGH = 85.0

# ==========================================================
# REVERSAL PROBABILITY
# ==========================================================

REVERSAL_LOW = 30.0

REVERSAL_MEDIUM = 50.0

REVERSAL_HIGH = 70.0

REVERSAL_VERY_HIGH = 85.0

# ==========================================================
# CONTINUATION PROBABILITY
# ==========================================================

CONTINUATION_LOW = 30.0

CONTINUATION_MEDIUM = 50.0

CONTINUATION_HIGH = 70.0

CONTINUATION_VERY_HIGH = 85.0

# ==========================================================
# DYNAMIC TP ENGINE
# ==========================================================

ENABLE_DYNAMIC_TP = True

MIN_TP_PROBABILITY = 60.0

GOOD_TP_PROBABILITY = 75.0

STRONG_TP_PROBABILITY = 85.0

# ==========================================================
# FINAL TRADE FILTER
# ==========================================================

MINIMUM_TRADE_CONFIDENCE = 65.0

MINIMUM_INSTITUTIONAL_SCORE = 60.0

MINIMUM_CONFLUENCE_SCORE = 60.0

# ==========================================================
# END OF CONFIG.PY PART 6
# ==========================================================

# ==========================================================
# CONFIG.PY
# PART 7
# DASHBOARD • OUTPUT • LABEL CONFIGURATION
# ==========================================================

# ==========================================================
# DASHBOARD SETTINGS
# ==========================================================

ENABLE_DASHBOARD = True

SHOW_HEADER = True

SHOW_TIMESTAMP = True

SHOW_SYMBOL = True

SHOW_TIMEFRAME = True

SHOW_SEPARATOR = True

# ==========================================================
# INSTITUTIONAL DASHBOARD
# ==========================================================

SHOW_INSTITUTIONAL_SCORE = True

SHOW_INSTITUTIONAL_BIAS = True

SHOW_MARKET_HEALTH = True

SHOW_TRADE_CONFIDENCE = True

SHOW_ENTRY_QUALITY = True

SHOW_EXIT_QUALITY = True

# ==========================================================
# PROBABILITY OUTPUT
# ==========================================================

SHOW_PULLBACK_PROBABILITY = True

SHOW_BREAKOUT_PROBABILITY = True

SHOW_REVERSAL_PROBABILITY = True

SHOW_CONTINUATION_PROBABILITY = True

SHOW_DYNAMIC_TP = True

# ==========================================================
# VWAP OUTPUT
# ==========================================================

SHOW_SESSION_VWAP = True

SHOW_15M_VWAP = True

SHOW_1H_VWAP = True

SHOW_4H_VWAP = True

SHOW_DAILY_VWAP = True

SHOW_WEEKLY_VWAP = True

SHOW_MONTHLY_VWAP = True

SHOW_ANCHORED_VWAP = True

# ==========================================================
# SCORE LABELS
# ==========================================================

SCORE_LABELS = {

    "excellent": (90, 100),

    "very_strong": (80, 89),

    "strong": (70, 79),

    "moderate": (60, 69),

    "weak": (40, 59),

    "very_weak": (0, 39)

}

# ==========================================================
# BIAS LABELS
# ==========================================================

BIAS_LABELS = {

    "strong_bullish": 90,

    "bullish": 70,

    "neutral": 50,

    "bearish": 30,

    "strong_bearish": 10

}

# ==========================================================
# TREND LABELS
# ==========================================================

TREND_LABELS = [

    "STRONG_BULLISH",

    "BULLISH",

    "NEUTRAL",

    "BEARISH",

    "STRONG_BEARISH"

]

# ==========================================================
# SIGNAL LABELS
# ==========================================================

BUY_SIGNAL = "BUY"

SELL_SIGNAL = "SELL"

WAIT_SIGNAL = "WAIT"

NO_SIGNAL = "NONE"

# ==========================================================
# RATING LABELS
# ==========================================================

RATING_LABELS = {

    "A+": 95,

    "A": 85,

    "B": 75,

    "C": 65,

    "D": 50,

    "F": 0

}

# ==========================================================
# OUTPUT PRECISION
# ==========================================================

PRICE_PRECISION = 4

PERCENT_PRECISION = 2

SCORE_PRECISION = 2

PROBABILITY_PRECISION = 2

# ==========================================================
# END OF CONFIG.PY PART 7
# ==========================================================

# ==========================================================
# CONFIG.PY
# PART 8 (FINAL)
# VALIDATION • PERFORMANCE • SYSTEM SETTINGS
# ==========================================================

# ==========================================================
# DATA VALIDATION
# ==========================================================

STRICT_DATA_VALIDATION = True

REMOVE_NAN_VALUES = True

REMOVE_INFINITE_VALUES = True

REPLACE_INVALID_VALUES = True

INVALID_NUMERIC_VALUE = 0.0

# ==========================================================
# MINIMUM DATA REQUIREMENTS
# ==========================================================

MIN_CANDLES_15M = 250

MIN_CANDLES_1H = 250

MIN_CANDLES_4H = 200

MIN_CANDLES_1D = 150

MIN_CANDLES_1W = 100

# ==========================================================
# PERFORMANCE SETTINGS
# ==========================================================

CACHE_ENABLED = True

CACHE_INDICATORS = True

CACHE_SCORES = True

CACHE_PROBABILITIES = True

CACHE_VWAP = True

# ==========================================================
# EXECUTION SETTINGS
# ==========================================================

MAX_RETRY = 3

TIMEOUT_SECONDS = 30

SAFE_MODE = True

# ==========================================================
# LOGGING SETTINGS
# ==========================================================

SAVE_LOGS = True

LOG_LEVEL = "INFO"

LOG_ERRORS_ONLY = False

# ==========================================================
# INTERNAL ENGINE SETTINGS
# ==========================================================

ENABLE_INTERNAL_CHECKS = True

ENABLE_RESULT_VALIDATION = True

ENABLE_SCORE_VALIDATION = True

ENABLE_PROBABILITY_VALIDATION = True

ENABLE_CONSISTENCY_CHECK = True

# ==========================================================
# OUTPUT VALIDATION
# ==========================================================

ALLOW_NEGATIVE_SCORE = False

ALLOW_SCORE_ABOVE_100 = False

ALLOW_PROBABILITY_ABOVE_100 = False

ALLOW_PROBABILITY_BELOW_ZERO = False

# ==========================================================
# RESERVED FOR FUTURE FEATURES
# ==========================================================

ENABLE_AI_FILTER = False

ENABLE_MACHINE_LEARNING = False

ENABLE_BACKTEST_MODE = False

ENABLE_PAPER_MODE = False

# ==========================================================
# SYSTEM STATUS
# ==========================================================

CONFIG_FILE_COMPLETE = True

PROJECT_READY = True

# ==========================================================
# END OF CONFIG.PY
# ==========================================================
