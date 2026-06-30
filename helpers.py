# ==========================================================
# HELPERS.PY
# PART 1
# CORE HELPERS
# ==========================================================

from __future__ import annotations

import math
import statistics
from typing import Any, Dict, List, Optional, Iterable

import numpy as np
import pandas as pd


# ==========================================================
# CONSTANTS
# ==========================================================

EPSILON = 1e-10

MIN_SCORE = 0.0
MAX_SCORE = 100.0


# ==========================================================
# SAFE TYPE CONVERSION
# ==========================================================

def safe_float(value: Any, default: float = 0.0) -> float:

    try:

        if value is None:
            return default

        if pd.isna(value):
            return default

        value = float(value)

        if math.isnan(value):
            return default

        if math.isinf(value):
            return default

        return value

    except Exception:

        return default


def safe_int(value: Any, default: int = 0) -> int:

    try:

        if value is None:
            return default

        return int(float(value))

    except Exception:

        return default


def safe_bool(value: Any) -> bool:

    try:

        return bool(value)

    except Exception:

        return False


def safe_str(value: Any, default: str = "") -> str:

    try:

        if value is None:
            return default

        return str(value)

    except Exception:

        return default


# ==========================================================
# SAFE SERIES
# ==========================================================

def safe_series(series: pd.Series) -> pd.Series:

    if series is None:

        return pd.Series(dtype=float)

    return (

        series

        .replace([np.inf, -np.inf], np.nan)

        .fillna(0.0)

        .astype(float)

    )


# ==========================================================
# SAFE DATAFRAME
# ==========================================================

def safe_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    if df is None:

        return pd.DataFrame()

    return df.replace(

        [np.inf, -np.inf],

        np.nan

    ).fillna(0.0)


# ==========================================================
# SAFE INDEX ACCESS
# ==========================================================

def safe_last(series, default=0.0):

    try:

        return safe_float(series.iloc[-1], default)

    except Exception:

        return default


def safe_previous(series, default=0.0):

    try:

        return safe_float(series.iloc[-2], default)

    except Exception:

        return default


def safe_value(series, index, default=0.0):

    try:

        return safe_float(

            series.iloc[index],

            default

        )

    except Exception:

        return default


# ==========================================================
# SAFE DIVISION
# ==========================================================

def safe_divide(

    numerator,

    denominator,

    default=0.0

):

    numerator = safe_float(numerator)

    denominator = safe_float(denominator)

    if abs(denominator) < EPSILON:

        return default

    return numerator / denominator


# ==========================================================
# NORMALIZATION
# ==========================================================

def normalize(

    value,

    minimum,

    maximum

):

    value = safe_float(value)

    minimum = safe_float(minimum)

    maximum = safe_float(maximum)

    if maximum <= minimum:

        return 0.0

    return (

        value - minimum

    ) / (

        maximum - minimum

    )


def normalize_score(

    value,

    minimum,

    maximum

):

    return normalize(

        value,

        minimum,

        maximum

    ) * 100.0


# ==========================================================
# CLAMP
# ==========================================================

def clamp(

    value,

    minimum,

    maximum

):

    value = safe_float(value)

    return max(

        minimum,

        min(

            maximum,

            value

        )

    )


def clamp_score(value):

    return clamp(

        value,

        MIN_SCORE,

        MAX_SCORE

    )


# ==========================================================
# ROUND HELPERS
# ==========================================================

def round_price(

    value,

    digits=4

):

    return round(

        safe_float(value),

        digits

    )


def round_score(value):

    return round(

        clamp_score(value),

        2

    )


# ==========================================================
# END OF HELPERS.PY PART 1
# ==========================================================

# ==========================================================
# HELPERS.PY
# PART 2
# PRICE • DISTANCE • TREND HELPERS
# ==========================================================

# ==========================================================
# BASIC PRICE CALCULATIONS
# ==========================================================

def typical_price(df):

    return (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3.0


def hl2(df):

    return (
        df["high"] +
        df["low"]
    ) / 2.0


def hlc3(df):

    return (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3.0


def ohlc4(df):

    return (
        df["open"] +
        df["high"] +
        df["low"] +
        df["close"]
    ) / 4.0


# ==========================================================
# CANDLE HELPERS
# ==========================================================

def candle_body(df):

    return (

        df["close"] -

        df["open"]

    ).abs()


def candle_range(df):

    return (

        df["high"] -

        df["low"]

    )


def upper_wick(df):

    return (

        df["high"]

        -

        df[["open", "close"]].max(axis=1)

    )


def lower_wick(df):

    return (

        df[["open", "close"]].min(axis=1)

        -

        df["low"]

    )


# ==========================================================
# DISTANCE HELPERS
# ==========================================================

def price_distance(

    price,

    level

):

    return abs(

        safe_float(price)

        -

        safe_float(level)

    )


def signed_distance(

    price,

    level

):

    return (

        safe_float(price)

        -

        safe_float(level)

    )


def percentage_distance(

    price,

    level

):

    return (

        safe_divide(

            (

                safe_float(price)

                -

                safe_float(level)

            ),

            safe_float(level)

        )

    ) * 100.0


def distance_points(

    a,

    b

):

    return abs(

        safe_float(a)

        -

        safe_float(b)

    )


# ==========================================================
# TREND HELPERS
# ==========================================================

def slope(

    series,

    period=5

):

    series = safe_series(series)

    return (

        series

        -

        series.shift(period)

    ) / period


def trend_direction(

    current,

    previous

):

    current = safe_float(current)

    previous = safe_float(previous)

    if current > previous:

        return "UP"

    if current < previous:

        return "DOWN"

    return "FLAT"


def trend_strength(

    current,

    previous

):

    return abs(

        safe_float(current)

        -

        safe_float(previous)

    )


# ==========================================================
# RISING / FALLING
# ==========================================================

def is_rising(

    series,

    period=1

):

    series = safe_series(series)

    return (

        series >

        series.shift(period)

    )


def is_falling(

    series,

    period=1

):

    series = safe_series(series)

    return (

        series <

        series.shift(period)

    )


def is_flat(

    series,

    tolerance=1e-8

):

    series = safe_series(series)

    return (

        (

            series -

            series.shift(1)

        ).abs()

        <= tolerance

    )


# ==========================================================
# LAST TREND STATE
# ==========================================================

def last_trend_state(

    series

):

    if safe_last(

        is_rising(series)

    ):

        return "RISING"

    if safe_last(

        is_falling(series)

    ):

        return "FALLING"

    return "FLAT"


# ==========================================================
# CROSS HELPERS
# ==========================================================

def crossover(

    a,

    b

):

    return (

        (a > b)

        &

        (

            a.shift(1)

            <=

            b.shift(1)

        )

    )


def crossunder(

    a,

    b

):

    return (

        (a < b)

        &

        (

            a.shift(1)

            >=

            b.shift(1)

        )

    )


# ==========================================================
# END OF HELPERS.PY PART 2
# ==========================================================

# ==========================================================
# HELPERS.PY
# PART 3
# SIGNAL • SCORE • PROBABILITY HELPERS
# ==========================================================

# ==========================================================
# SIGNAL AGREEMENT COUNTER
# ==========================================================

def signal_agreement(signals):

    bullish = 0
    bearish = 0
    neutral = 0

    bullish_values = {
        "BUY",
        "BULLISH",
        "LONG",
        "UP",
        "STRONG_BUY",
        "TRUE",
        True,
        1
    }

    bearish_values = {
        "SELL",
        "BEARISH",
        "SHORT",
        "DOWN",
        "STRONG_SELL",
        False,
        -1
    }

    for signal in signals:

        value = signal

        if isinstance(value, str):
            value = value.strip().upper()

        if value in bullish_values:
            bullish += 1

        elif value in bearish_values:
            bearish += 1

        else:
            neutral += 1

    return {

        "bullish": bullish,

        "bearish": bearish,

        "neutral": neutral,

        "total": len(signals)

    }


# ==========================================================
# STRONGEST SIGNAL
# ==========================================================

def strongest_signal(signals):

    result = signal_agreement(signals)

    if result["bullish"] > result["bearish"]:

        return "BULLISH"

    if result["bearish"] > result["bullish"]:

        return "BEARISH"

    return "NEUTRAL"


# ==========================================================
# CONFLUENCE %
# ==========================================================

def confluence_percent(signals):

    result = signal_agreement(signals)

    total = result["total"]

    if total == 0:

        return 0.0

    strongest = max(

        result["bullish"],

        result["bearish"],

        result["neutral"]

    )

    return round(

        (strongest / total) * 100,

        2

    )


# ==========================================================
# SCORE HELPERS
# ==========================================================

def average_score(scores):

    values = [

        clamp_score(x)

        for x in scores

        if x is not None

    ]

    if not values:

        return 0.0

    return round(

        sum(values) / len(values),

        2

    )


def weighted_score(score_weight_pairs):

    total_weight = 0.0

    total_score = 0.0

    for score, weight in score_weight_pairs:

        score = clamp_score(score)

        weight = max(

            0.0,

            safe_float(weight)

        )

        total_score += score * weight

        total_weight += weight

    if total_weight == 0:

        return 0.0

    return round(

        total_score / total_weight,

        2

    )


# ==========================================================
# SCORE → RATING
# ==========================================================

def score_rating(score):

    score = clamp_score(score)

    if score >= 90:
        return "EXCELLENT"

    if score >= 75:
        return "VERY_STRONG"

    if score >= 60:
        return "STRONG"

    if score >= 45:
        return "MODERATE"

    if score >= 30:
        return "WEAK"

    return "VERY_WEAK"


# ==========================================================
# SCORE → BIAS
# ==========================================================

def score_bias(score):

    score = clamp_score(score)

    if score >= 70:
        return "BULLISH"

    if score <= 30:
        return "BEARISH"

    return "NEUTRAL"


# ==========================================================
# PROBABILITY HELPERS
# ==========================================================

def probability(score):

    return round(

        clamp_score(score),

        2

    )


def probability_label(value):

    value = clamp_score(value)

    if value >= 85:
        return "VERY_HIGH"

    if value >= 70:
        return "HIGH"

    if value >= 55:
        return "MEDIUM"

    if value >= 40:
        return "LOW"

    return "VERY_LOW"


# ==========================================================
# BOOLEAN HELPERS
# ==========================================================

def all_true(values):

    return all(bool(v) for v in values)


def any_true(values):

    return any(bool(v) for v in values)


def none_true(values):

    return not any(bool(v) for v in values)


# ==========================================================
# END OF HELPERS.PY PART 3
# ==========================================================

# ==========================================================
# HELPERS.PY
# PART 4 (FINAL)
# VALIDATION • DICTIONARY • TIMEFRAME • UTILITIES
# ==========================================================

from datetime import datetime


# ==========================================================
# VALIDATION HELPERS
# ==========================================================

def has_columns(df, columns):

    if df is None:
        return False

    return all(col in df.columns for col in columns)


def validate_ohlcv(df):

    required = [
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    return has_columns(df, required)


def dataframe_length(df):

    try:
        return len(df)
    except Exception:
        return 0


# ==========================================================
# DICTIONARY HELPERS
# ==========================================================

def safe_get(dictionary, key, default=None):

    try:

        if dictionary is None:
            return default

        return dictionary.get(key, default)

    except Exception:

        return default


def merge_dicts(*dicts):

    merged = {}

    for d in dicts:

        if isinstance(d, dict):

            merged.update(d)

    return merged


def remove_none(dictionary):

    return {

        k: v

        for k, v in dictionary.items()

        if v is not None

    }


# ==========================================================
# TIMEFRAME HELPERS
# ==========================================================

TIMEFRAME_ORDER = {

    "1m": 1,
    "3m": 3,
    "5m": 5,
    "15m": 15,
    "30m": 30,

    "1h": 60,
    "2h": 120,
    "4h": 240,
    "6h": 360,
    "8h": 480,
    "12h": 720,

    "1d": 1440,
    "1w": 10080,
    "1M": 43200

}


def timeframe_value(timeframe):

    return TIMEFRAME_ORDER.get(

        str(timeframe),

        0

    )


def higher_timeframe(tf1, tf2):

    return timeframe_value(tf1) > timeframe_value(tf2)


def lower_timeframe(tf1, tf2):

    return timeframe_value(tf1) < timeframe_value(tf2)


# ==========================================================
# LIST HELPERS
# ==========================================================

def remove_duplicates(values):

    return list(dict.fromkeys(values))


def average(values):

    values = [

        safe_float(v)

        for v in values

        if v is not None

    ]

    if len(values) == 0:

        return 0.0

    return sum(values) / len(values)


def median(values):

    values = [

        safe_float(v)

        for v in values

        if v is not None

    ]

    if len(values) == 0:

        return 0.0

    return statistics.median(values)


# ==========================================================
# PRICE HELPERS
# ==========================================================

def highest_price(df):

    return safe_float(df["high"].max())


def lowest_price(df):

    return safe_float(df["low"].min())


def last_close(df):

    return safe_last(df["close"])


# ==========================================================
# DATE / TIME
# ==========================================================

def utc_now():

    return datetime.utcnow()


def current_timestamp():

    return utc_now().strftime(

        "%Y-%m-%d %H:%M:%S"

    )


# ==========================================================
# OUTPUT HELPERS
# ==========================================================

def success(

    message,

    **kwargs

):

    data = {

        "success": True,

        "message": message

    }

    data.update(kwargs)

    return data


def failure(

    message,

    **kwargs

):

    data = {

        "success": False,

        "message": message

    }

    data.update(kwargs)

    return data


# ==========================================================
# INTERNAL DEBUG
# ==========================================================

DEBUG_MODE = False


def debug(*args):

    if DEBUG_MODE:

        print(*args)


# ==========================================================
# END OF HELPERS.PY
# ==========================================================

# ==========================================================
# HELPERS.PY
# PART 5
# ADVANCED NUMERIC & CONFLUENCE HELPERS
# ==========================================================

# ==========================================================
# SCORE UTILITIES
# ==========================================================

def score_percentage(value, maximum):

    maximum = safe_float(maximum)

    if maximum <= 0:
        return 0.0

    return clamp_score(
        (safe_float(value) / maximum) * 100.0
    )


def inverse_score(score):

    return clamp_score(100.0 - safe_float(score))


# ==========================================================
# WEIGHTED AVERAGE
# ==========================================================

def weighted_average(values, weights):

    values = list(values)
    weights = list(weights)

    if len(values) != len(weights):
        return 0.0

    total_weight = sum(
        safe_float(w) for w in weights
    )

    if total_weight <= 0:
        return 0.0

    weighted_sum = sum(
        safe_float(v) * safe_float(w)
        for v, w in zip(values, weights)
    )

    return weighted_sum / total_weight


# ==========================================================
# SCORE AGREEMENT
# ==========================================================

def agreement_score(scores, threshold=60):

    scores = [
        clamp_score(s)
        for s in scores
        if s is not None
    ]

    if not scores:
        return 0

    return sum(
        1 for s in scores
        if s >= threshold
    )


# ==========================================================
# CONFLUENCE
# ==========================================================

def confluence_counter(conditions):

    return sum(
        1 for c in conditions
        if bool(c)
    )


def confluence_percentage(conditions):

    total = len(conditions)

    if total == 0:
        return 0.0

    count = confluence_counter(conditions)

    return round(
        (count / total) * 100.0,
        2
    )


# ==========================================================
# BIAS HELPERS
# ==========================================================

def bullish_percentage(bullish, total):

    return score_percentage(
        bullish,
        total
    )


def bearish_percentage(bearish, total):

    return score_percentage(
        bearish,
        total
    )


def dominant_bias(bullish, bearish):

    bullish = safe_float(bullish)
    bearish = safe_float(bearish)

    if bullish > bearish:
        return "BULLISH"

    if bearish > bullish:
        return "BEARISH"

    return "NEUTRAL"


# ==========================================================
# STRENGTH CLASSIFICATION
# ==========================================================

def strength_label(score):

    score = clamp_score(score)

    if score >= 90:
        return "EXTREME"

    if score >= 75:
        return "VERY_STRONG"

    if score >= 60:
        return "STRONG"

    if score >= 40:
        return "MODERATE"

    if score >= 20:
        return "WEAK"

    return "VERY_WEAK"


# ==========================================================
# PROBABILITY HELPERS
# ==========================================================

def probability_from_score(score):

    return clamp_score(score)


def probability_band(score):

    score = clamp_score(score)

    if score >= 80:
        return "HIGH"

    if score >= 60:
        return "MEDIUM"

    if score >= 40:
        return "LOW"

    return "VERY_LOW"


# ==========================================================
# END OF HELPERS.PY PART 5
# ==========================================================

# ==========================================================
# HELPERS.PY
# PART 6 (FINAL)
# INSTITUTIONAL HELPERS
# ==========================================================

# ==========================================================
# BIAS HELPERS
# ==========================================================

def institutional_bias(score):

    score = clamp_score(score)

    if score >= 85:
        return "STRONG_BULLISH"

    if score >= 65:
        return "BULLISH"

    if score >= 35:
        return "NEUTRAL"

    if score >= 15:
        return "BEARISH"

    return "STRONG_BEARISH"


# ==========================================================
# MARKET HEALTH
# ==========================================================

def market_health_label(score):

    score = clamp_score(score)

    if score >= 85:
        return "EXCELLENT"

    if score >= 70:
        return "GOOD"

    if score >= 50:
        return "NORMAL"

    if score >= 30:
        return "WEAK"

    return "VERY_WEAK"


# ==========================================================
# ENTRY QUALITY
# ==========================================================

def entry_quality_label(score):

    score = clamp_score(score)

    if score >= 90:
        return "A+"

    if score >= 80:
        return "A"

    if score >= 70:
        return "B"

    if score >= 60:
        return "C"

    return "POOR"


# ==========================================================
# EXIT QUALITY
# ==========================================================

def exit_quality_label(score):

    return entry_quality_label(score)


# ==========================================================
# SUPPORT / RESISTANCE RATING
# ==========================================================

def level_strength_label(score):

    score = clamp_score(score)

    if score >= 80:
        return "VERY_STRONG"

    if score >= 60:
        return "STRONG"

    if score >= 40:
        return "MODERATE"

    if score >= 20:
        return "WEAK"

    return "VERY_WEAK"


# ==========================================================
# VOLATILITY RATING
# ==========================================================

def volatility_label(score):

    score = clamp_score(score)

    if score >= 80:
        return "EXTREME"

    if score >= 60:
        return "HIGH"

    if score >= 40:
        return "NORMAL"

    if score >= 20:
        return "LOW"

    return "VERY_LOW"


# ==========================================================
# CONFIDENCE LABEL
# ==========================================================

def confidence_label(score):

    score = clamp_score(score)

    if score >= 90:
        return "VERY_HIGH"

    if score >= 75:
        return "HIGH"

    if score >= 60:
        return "GOOD"

    if score >= 45:
        return "AVERAGE"

    return "LOW"


# ==========================================================
# SCORE SUMMARY
# ==========================================================

def score_summary(score):

    score = clamp_score(score)

    return {

        "score": round(score, 2),

        "bias": institutional_bias(score),

        "rating": score_rating(score),

        "strength": strength_label(score),

        "confidence": confidence_label(score)

    }


# ==========================================================
# DATA QUALITY
# ==========================================================

def data_quality(df):

    if df is None:

        return 0.0

    total = len(df)

    if total == 0:

        return 0.0

    missing = df.isna().sum().sum()

    cells = df.shape[0] * df.shape[1]

    quality = (

        1 -

        safe_divide(

            missing,

            cells

        )

    ) * 100

    return clamp_score(quality)


# ==========================================================
# EMPTY RESULT
# ==========================================================

def empty_result():

    return {

        "success": False,

        "score": 0.0,

        "bias": "UNKNOWN"

    }


# ==========================================================
# SUCCESS RESULT
# ==========================================================

def success_result(**kwargs):

    result = {

        "success": True

    }

    result.update(kwargs)

    return result


# ==========================================================
# FAILURE RESULT
# ==========================================================

def failure_result(message="Unknown Error"):

    return {

        "success": False,

        "message": message

    }


# ==========================================================
# END OF HELPERS.PY
# ==========================================================
