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

# ==========================================================
# SESSION VWAP
# ==========================================================

def session_vwap(df):

    typical = (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3

    pv = typical * df["volume"]

    cumulative_pv = pv.cumsum()
    cumulative_volume = df["volume"].cumsum()

    return cumulative_pv / cumulative_volume


# ==========================================================
# GENERIC VWAP
# ==========================================================

def rolling_vwap(df, length):

    typical = (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3

    pv = typical * df["volume"]

    rolling_pv = (
        pv
        .rolling(length)
        .sum()
    )

    rolling_volume = (
        df["volume"]
        .rolling(length)
        .sum()
    )

    return rolling_pv / rolling_volume


# ==========================================================
# DAILY VWAP
# ==========================================================

def daily_vwap(df):

    return rolling_vwap(df, 390)


# ==========================================================
# WEEKLY VWAP
# ==========================================================

def weekly_vwap(df):

    return rolling_vwap(df, 1950)


# ==========================================================
# MONTHLY VWAP
# ==========================================================

def monthly_vwap(df):

    return rolling_vwap(df, 7800)


# ==========================================================
# 15 MIN VWAP
# ==========================================================

def vwap_15m(df):

    return rolling_vwap(df, 15)


# ==========================================================
# 1 HOUR VWAP
# ==========================================================

def vwap_1h(df):

    return rolling_vwap(df, 60)


# ==========================================================
# 4 HOUR VWAP
# ==========================================================

def vwap_4h(df):

    return rolling_vwap(df, 240)


# ==========================================================
# PRICE DISTANCE FROM VWAP
# ==========================================================

def vwap_distance(price, vwap):

    if vwap is None:
        return 0.0

    return float(price - vwap)


# ==========================================================
# PRICE POSITION
# ==========================================================

def vwap_position(price, vwap):

    if price > vwap:
        return "ABOVE"

    elif price < vwap:
        return "BELOW"

    return "ON"


# ==========================================================
# VWAP TREND
# ==========================================================

def vwap_trend(series):

    current = safe_last(series)
    previous = safe_prev(series)

    if current > previous:
        return "RISING"

    elif current < previous:
        return "FALLING"

    return "FLAT"


# ==========================================================
# VWAP CROSS
# ==========================================================

def vwap_cross(df, series):

    price = df["close"]

    if crossover(price, series):
        return "BULLISH"

    if crossunder(price, series):
        return "BEARISH"

    return "NONE"


# ==========================================================
# VWAP SLOPE
# ==========================================================

def vwap_slope(series):

    return slope(series)


# ==========================================================
# VWAP SUMMARY
# ==========================================================

def build_vwap_summary(df, series):

    price = safe_last(df["close"])
    value = safe_last(series)

    return {

        "value": round(value, 2),

        "distance": round(
            vwap_distance(price, value),
            2
        ),

        "position": vwap_position(
            price,
            value
        ),

        "trend": vwap_trend(series),

        "slope": vwap_slope(series),

        "cross": vwap_cross(
            df,
            series
        )

    }

# ==========================================================
# END OF PART 1B
# ==========================================================

# ==========================================================
# ANCHORED VWAP ENGINE
# ==========================================================

def anchored_vwap(df, anchor_index):

    if anchor_index is None:
        anchor_index = 0

    anchor_index = max(0, min(anchor_index, len(df) - 1))

    data = df.iloc[anchor_index:].copy()

    typical = (
        data["high"] +
        data["low"] +
        data["close"]
    ) / 3.0

    pv = typical * data["volume"]

    cumulative_pv = pv.cumsum()
    cumulative_volume = data["volume"].cumsum()

    result = cumulative_pv / cumulative_volume

    return result


# ==========================================================
# LAST SWING HIGH INDEX
# ==========================================================

def last_swing_high_index(df, lookback=3):

    highs = df["high"].values

    for i in range(len(df)-lookback-1, lookback, -1):

        left = highs[i-lookback:i]
        right = highs[i+1:i+lookback+1]

        if highs[i] >= max(left) and highs[i] >= max(right):
            return i

    return 0


# ==========================================================
# LAST SWING LOW INDEX
# ==========================================================

def last_swing_low_index(df, lookback=3):

    lows = df["low"].values

    for i in range(len(df)-lookback-1, lookback, -1):

        left = lows[i-lookback:i]
        right = lows[i+1:i+lookback+1]

        if lows[i] <= min(left) and lows[i] <= min(right):
            return i

    return 0


# ==========================================================
# SWING HIGH VWAP
# ==========================================================

def anchored_vwap_swing_high(df):

    idx = last_swing_high_index(df)

    return anchored_vwap(df, idx)


# ==========================================================
# SWING LOW VWAP
# ==========================================================

def anchored_vwap_swing_low(df):

    idx = last_swing_low_index(df)

    return anchored_vwap(df, idx)


# ==========================================================
# BREAKOUT VWAP
# ==========================================================

def breakout_vwap(df):

    breakout = len(df) - 20

    if breakout < 0:
        breakout = 0

    return anchored_vwap(df, breakout)


# ==========================================================
# BOS VWAP
# ==========================================================

def bos_vwap(df):

    idx = max(0, len(df)-30)

    return anchored_vwap(df, idx)


# ==========================================================
# CHOCH VWAP
# ==========================================================

def choch_vwap(df):

    idx = max(0, len(df)-15)

    return anchored_vwap(df, idx)


# ==========================================================
# COUNT VWAPS ABOVE PRICE
# ==========================================================

def count_above(price, values):

    total = 0

    for value in values:

        if price > value:
            total += 1

    return total


# ==========================================================
# COUNT VWAPS BELOW PRICE
# ==========================================================

def count_below(price, values):

    total = 0

    for value in values:

        if price < value:
            total += 1

    return total


# ==========================================================
# VWAP CONFLUENCE ENGINE
# ==========================================================

def vwap_confluence(df):

    price = safe_last(df["close"])

    levels = [

        safe_last(session_vwap(df)),
        safe_last(daily_vwap(df)),
        safe_last(weekly_vwap(df)),
        safe_last(monthly_vwap(df)),
        safe_last(vwap_15m(df)),
        safe_last(vwap_1h(df)),
        safe_last(vwap_4h(df)),
        safe_last(anchored_vwap_swing_high(df)),
        safe_last(anchored_vwap_swing_low(df)),
        safe_last(breakout_vwap(df)),
        safe_last(bos_vwap(df)),
        safe_last(choch_vwap(df))

    ]

    above = count_above(price, levels)
    below = count_below(price, levels)

    alignment = max(above, below)

    score = round((alignment / len(levels)) * 100, 2)

    return {

        "price": round(price,2),

        "aligned": alignment,

        "total": len(levels),

        "score": score,

        "above": above,

        "below": below

    }


# ==========================================================
# STRONGEST VWAP SUPPORT
# ==========================================================

def strongest_vwap_support(df):

    price = safe_last(df["close"])

    values = [

        safe_last(session_vwap(df)),
        safe_last(daily_vwap(df)),
        safe_last(weekly_vwap(df)),
        safe_last(monthly_vwap(df)),
        safe_last(vwap_15m(df)),
        safe_last(vwap_1h(df)),
        safe_last(vwap_4h(df))

    ]

    supports = [v for v in values if v <= price]

    if len(supports) == 0:
        return 0.0

    return max(supports)


# ==========================================================
# STRONGEST VWAP RESISTANCE
# ==========================================================

def strongest_vwap_resistance(df):

    price = safe_last(df["close"])

    values = [

        safe_last(session_vwap(df)),
        safe_last(daily_vwap(df)),
        safe_last(weekly_vwap(df)),
        safe_last(monthly_vwap(df)),
        safe_last(vwap_15m(df)),
        safe_last(vwap_1h(df)),
        safe_last(vwap_4h(df))

    ]

    resistance = [v for v in values if v >= price]

    if len(resistance) == 0:
        return 0.0

    return min(resistance)

# ==========================================================
# END OF PART 1C
# ==========================================================

