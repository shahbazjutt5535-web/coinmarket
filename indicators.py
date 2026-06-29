"""
==========================================================
INDICATORS.PY
Part 1A
Core Indicators Engine
==========================================================
"""

import numpy as np
import pandas as pd

# ==========================================================
# SAFE HELPERS
# ==========================================================

def safe_last(series, default=0.0):
    try:
        value = float(series.iloc[-1])
        if np.isnan(value):
            return default
        return value
    except:
        return default


def safe_prev(series, default=0.0):
    try:
        value = float(series.iloc[-2])
        if np.isnan(value):
            return default
        return value
    except:
        return default


def safe_series(series):
    return pd.Series(series).fillna(method="ffill").fillna(method="bfill")


# ==========================================================
# SMA
# ==========================================================

def sma(df, length=20):
    return (
        df["close"]
        .rolling(length)
        .mean()
    )


# ==========================================================
# EMA
# ==========================================================

def ema(df, length=20):
    return (
        df["close"]
        .ewm(
            span=length,
            adjust=False
        )
        .mean()
    )


# ==========================================================
# WMA
# ==========================================================

def wma(df, length=20):

    weights = np.arange(1, length + 1)

    return (
        df["close"]
        .rolling(length)
        .apply(
            lambda x:
            np.dot(x, weights) / weights.sum(),
            raw=True
        )
    )


# ==========================================================
# HMA
# ==========================================================

def hma(df, length=20):

    half = int(length / 2)
    root = int(np.sqrt(length))

    wma_half = wma(df, half)
    wma_full = wma(df, length)

    raw = (2 * wma_half) - wma_full

    temp = pd.DataFrame({
        "close": raw
    })

    return wma(temp, root)


# ==========================================================
# VWMA
# ==========================================================

def vwma(df, length=20):

    pv = df["close"] * df["volume"]

    return (
        pv.rolling(length).sum()
        /
        df["volume"].rolling(length).sum()
    )


# ==========================================================
# TRUE RANGE
# ==========================================================

def true_range(df):

    high = df["high"]
    low = df["low"]
    close = df["close"]

    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()

    tr = pd.concat(
        [tr1, tr2, tr3],
        axis=1
    ).max(axis=1)

    return tr


# ==========================================================
# ATR
# ==========================================================

def atr(df, length=14):

    tr = true_range(df)

    return (
        tr
        .rolling(length)
        .mean()
    )


# ==========================================================
# STANDARD DEVIATION
# ==========================================================

def std(df, length=20):

    return (
        df["close"]
        .rolling(length)
        .std()
    )


# ==========================================================
# BOLLINGER BANDS
# ==========================================================

def bollinger_bands(
    df,
    length=20,
    mult=2
):

    mid = sma(df, length)

    deviation = std(df, length)

    upper = mid + deviation * mult
    lower = mid - deviation * mult

    width = upper - lower

    return {
        "upper": upper,
        "middle": mid,
        "lower": lower,
        "width": width
    }


# ==========================================================
# DONCHIAN CHANNEL
# ==========================================================

def donchian(
    df,
    length=20
):

    upper = (
        df["high"]
        .rolling(length)
        .max()
    )

    lower = (
        df["low"]
        .rolling(length)
        .min()
    )

    middle = (upper + lower) / 2

    return {
        "upper": upper,
        "middle": middle,
        "lower": lower
    }


# ==========================================================
# PRICE DISTANCE
# ==========================================================

def distance_from_price(
    price,
    level
):

    if level is None:
        return 0.0

    return float(price - level)


# ==========================================================
# PERCENT DISTANCE
# ==========================================================

def percent_distance(
    price,
    level
):

    if level == 0:
        return 0.0

    return (
        (price - level)
        /
        level
    ) * 100


# ==========================================================
# TREND SLOPE
# ==========================================================

def slope(series):

    if len(series) < 5:
        return 0

    last_value = safe_last(series)
    prev_value = safe_prev(series)

    if last_value > prev_value:
        return "RISING"

    elif last_value < prev_value:
        return "FALLING"

    return "FLAT"


# ==========================================================
# CROSS DETECTION
# ==========================================================

def crossover(a, b):

    return (
        safe_prev(a) < safe_prev(b)
        and
        safe_last(a) > safe_last(b)
    )


def crossunder(a, b):

    return (
        safe_prev(a) > safe_prev(b)
        and
        safe_last(a) < safe_last(b)
    )

# =========================
# END OF PART 1A
# =========================
