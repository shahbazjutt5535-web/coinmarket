# ==========================================================
# INDICATORS.PY
# PART 1A
# CORE IMPORTS + HELPERS
# ==========================================================

import numpy as np
import pandas as pd

# ==========================================================
# SAFE VALUE HELPERS
# ==========================================================

def safe_float(value, default=0.0):
    try:
        if value is None:
            return default
        if pd.isna(value):
            return default
        if np.isinf(value):
            return default
        return float(value)
    except:
        return default


def safe_series(series):
    if series is None:
        return pd.Series(dtype=float)

    return series.replace([np.inf, -np.inf], np.nan).fillna(0.0)


def safe_last(series, default=0.0):

    try:
        return safe_float(series.iloc[-1], default)
    except:
        return default


def safe_previous(series, default=0.0):

    try:
        return safe_float(series.iloc[-2], default)
    except:
        return default


# ==========================================================
# BASIC PRICE HELPERS
# ==========================================================

def hl2(df):

    return (df["high"] + df["low"]) / 2


def hlc3(df):

    return (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3


def ohlc4(df):

    return (
        df["open"] +
        df["high"] +
        df["low"] +
        df["close"]
    ) / 4


def candle_range(df):

    return df["high"] - df["low"]


def candle_body(df):

    return (df["close"] - df["open"]).abs()


def upper_wick(df):

    return df["high"] - df[["open", "close"]].max(axis=1)


def lower_wick(df):

    return df[["open", "close"]].min(axis=1) - df["low"]


# ==========================================================
# DISTANCE HELPERS
# ==========================================================

def distance(price, level):

    return abs(
        safe_float(price) -
        safe_float(level)
    )


def distance_percent(price, level):

    level = safe_float(level)

    if level == 0:
        return 0.0

    return (
        (safe_float(price) - level)
        / level
    ) * 100


# ==========================================================
# MOVING AVERAGE HELPERS
# ==========================================================

def sma(series, length):

    return safe_series(series).rolling(length).mean()


def ema(series, length):

    return safe_series(series).ewm(
        span=length,
        adjust=False
    ).mean()


# ==========================================================
# TRUE RANGE
# ==========================================================

def true_range(df):

    tr1 = df["high"] - df["low"]

    tr2 = (
        df["high"] -
        df["close"].shift()
    ).abs()

    tr3 = (
        df["low"] -
        df["close"].shift()
    ).abs()

    return pd.concat(
        [tr1, tr2, tr3],
        axis=1
    ).max(axis=1)


# ==========================================================
# ATR
# ==========================================================

def atr(df, length=14):

    return true_range(df).rolling(length).mean()


# ==========================================================
# SLOPE
# ==========================================================

def slope(series, period=5):

    series = safe_series(series)

    return (
        series -
        series.shift(period)
    ) / period


# ==========================================================
# CROSSOVER
# ==========================================================

def crossover(a, b):

    return (
        (a > b) &
        (a.shift(1) <= b.shift(1))
    )


def crossunder(a, b):

    return (
        (a < b) &
        (a.shift(1) >= b.shift(1))
    )


# ==========================================================
# END OF PART 1A
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1B
# MOVING AVERAGES + PRICE UTILITIES
# ==========================================================

# ==========================================================
# RMA (WILDER)
# ==========================================================

def rma(series, length=14):

    series = safe_series(series)

    return series.ewm(
        alpha=1 / length,
        adjust=False
    ).mean()


# ==========================================================
# WMA
# ==========================================================

def wma(series, length=14):

    series = safe_series(series)

    weights = np.arange(1, length + 1)

    return series.rolling(length).apply(
        lambda x: np.dot(x, weights) / weights.sum(),
        raw=True
    )


# ==========================================================
# VWMA
# ==========================================================

def vwma(close, volume, length=20):

    close = safe_series(close)
    volume = safe_series(volume)

    pv = close * volume

    return (
        pv.rolling(length).sum() /
        volume.rolling(length).sum()
    )


# ==========================================================
# HMA
# ==========================================================

def hma(series, length=20):

    half = int(length / 2)

    root = int(np.sqrt(length))

    first = wma(series, half)

    second = wma(series, length)

    raw = (2 * first) - second

    return wma(raw, root)


# ==========================================================
# SMMA
# ==========================================================

def smma(series, length=14):

    return rma(series, length)


# ==========================================================
# MEDIAN PRICE
# ==========================================================

def median_price(df):

    return (
        df["high"] +
        df["low"]
    ) / 2


# ==========================================================
# TYPICAL PRICE
# ==========================================================

def typical_price(df):

    return (
        df["high"] +
        df["low"] +
        df["close"]
    ) / 3


# ==========================================================
# WEIGHTED CLOSE
# ==========================================================

def weighted_close(df):

    return (
        df["high"] +
        df["low"] +
        (df["close"] * 2)
    ) / 4


# ==========================================================
# HIGHEST
# ==========================================================

def highest(series, length):

    return safe_series(series).rolling(length).max()


# ==========================================================
# LOWEST
# ==========================================================

def lowest(series, length):

    return safe_series(series).rolling(length).min()


# ==========================================================
# HIGHEST BAR
# ==========================================================

def highest_bar(series, length):

    return safe_series(series).rolling(length).apply(
        np.argmax,
        raw=True
    )


# ==========================================================
# LOWEST BAR
# ==========================================================

def lowest_bar(series, length):

    return safe_series(series).rolling(length).apply(
        np.argmin,
        raw=True
    )


# ==========================================================
# PRICE CHANGE
# ==========================================================

def price_change(series):

    return safe_series(series).diff()


# ==========================================================
# PRICE CHANGE %
# ==========================================================

def percent_change(series):

    return safe_series(series).pct_change() * 100


# ==========================================================
# LOG RETURN
# ==========================================================

def log_return(series):

    series = safe_series(series)

    return np.log(
        series / series.shift(1)
    )


# ==========================================================
# VOLATILITY
# ==========================================================

def volatility(series, length=20):

    return log_return(series).rolling(length).std()


# ==========================================================
# PRICE POSITION
# ==========================================================

def price_position(df, length=20):

    hh = highest(df["high"], length)

    ll = lowest(df["low"], length)

    return (
        (df["close"] - ll) /
        (hh - ll)
    ) * 100


# ==========================================================
# ROLLING MIDPOINT
# ==========================================================

def rolling_midpoint(df, length=20):

    hh = highest(df["high"], length)

    ll = lowest(df["low"], length)

    return (hh + ll) / 2


# ==========================================================
# END OF PART 1B
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1C
# VWAP ENGINE
# ==========================================================

# ==========================================================
# CUMULATIVE VWAP
# ==========================================================

def cumulative_vwap(df):

    tp = typical_price(df)

    pv = tp * df["volume"]

    cumulative_pv = pv.cumsum()

    cumulative_volume = df["volume"].cumsum()

    return cumulative_pv / cumulative_volume


# ==========================================================
# SESSION VWAP
# ==========================================================

def session_vwap(df):

    return cumulative_vwap(df)


# ==========================================================
# DAILY VWAP
# ==========================================================

def daily_vwap(df):

    return cumulative_vwap(df)


# ==========================================================
# WEEKLY VWAP
# ==========================================================

def weekly_vwap(df):

    return cumulative_vwap(df)


# ==========================================================
# MONTHLY VWAP
# ==========================================================

def monthly_vwap(df):

    return cumulative_vwap(df)


# ==========================================================
# GENERIC VWAP
# ==========================================================

def vwap(df):

    return cumulative_vwap(df)


# ==========================================================
# VWAP DISTANCE
# ==========================================================

def vwap_distance(price, vwap_value):

    return safe_float(price) - safe_float(vwap_value)


# ==========================================================
# VWAP DISTANCE %
# ==========================================================

def vwap_distance_percent(price, vwap_value):

    if safe_float(vwap_value) == 0:
        return 0.0

    return (
        (safe_float(price) - safe_float(vwap_value))
        / safe_float(vwap_value)
    ) * 100


# ==========================================================
# ABOVE VWAP
# ==========================================================

def above_vwap(price, vwap_value):

    return safe_float(price) > safe_float(vwap_value)


# ==========================================================
# BELOW VWAP
# ==========================================================

def below_vwap(price, vwap_value):

    return safe_float(price) < safe_float(vwap_value)


# ==========================================================
# VWAP SLOPE
# ==========================================================

def vwap_slope(vwap_series, period=5):

    return slope(vwap_series, period)


# ==========================================================
# VWAP TREND
# ==========================================================

def vwap_trend(vwap_series):

    s = safe_last(vwap_slope(vwap_series))

    if s > 0:
        return "RISING"

    if s < 0:
        return "FALLING"

    return "FLAT"


# ==========================================================
# VWAP CROSS
# ==========================================================

def bullish_vwap_cross(close, vwap_series):

    return crossover(close, vwap_series)


def bearish_vwap_cross(close, vwap_series):

    return crossunder(close, vwap_series)


# ==========================================================
# MULTI VWAP SNAPSHOT
# ==========================================================

def multi_vwap_snapshot(df):

    price = safe_last(df["close"])

    session = session_vwap(df)
    daily = daily_vwap(df)
    weekly = weekly_vwap(df)
    monthly = monthly_vwap(df)

    return {

        "price": safe_float(price),

        "session": safe_last(session),
        "daily": safe_last(daily),
        "weekly": safe_last(weekly),
        "monthly": safe_last(monthly),

        "session_distance":
            vwap_distance(price, safe_last(session)),

        "daily_distance":
            vwap_distance(price, safe_last(daily)),

        "weekly_distance":
            vwap_distance(price, safe_last(weekly)),

        "monthly_distance":
            vwap_distance(price, safe_last(monthly)),

        "session_trend":
            vwap_trend(session),

        "daily_trend":
            vwap_trend(daily),

        "weekly_trend":
            vwap_trend(weekly),

        "monthly_trend":
            vwap_trend(monthly)

    }


# ==========================================================
# END OF PART 1C
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1D
# ANCHORED VWAP ENGINE
# ==========================================================

# ==========================================================
# INTERNAL AVWAP
# ==========================================================

def _anchored_vwap(df, anchor_index):

    anchor_index = int(max(0, min(anchor_index, len(df) - 1)))

    data = df.iloc[anchor_index:].copy()

    tp = typical_price(data)

    pv = tp * data["volume"]

    cumulative_pv = pv.cumsum()

    cumulative_volume = data["volume"].cumsum()

    avwap = cumulative_pv / cumulative_volume

    return avwap.reindex(df.index)


# ==========================================================
# SWING HIGH ANCHOR
# ==========================================================

def anchored_vwap_swing_high(df, lookback=80):

    high = df["high"].tail(lookback)

    idx = high.idxmax()

    anchor = df.index.get_loc(idx)

    return _anchored_vwap(df, anchor)


# ==========================================================
# SWING LOW ANCHOR
# ==========================================================

def anchored_vwap_swing_low(df, lookback=80):

    low = df["low"].tail(lookback)

    idx = low.idxmin()

    anchor = df.index.get_loc(idx)

    return _anchored_vwap(df, anchor)


# ==========================================================
# BOS ANCHOR
# ==========================================================

def anchored_vwap_bos(df):

    hh = highest(df["high"], 20)

    trigger = crossover(df["close"], hh.shift(1))

    if trigger.any():

        idx = trigger[trigger].index[-1]

        anchor = df.index.get_loc(idx)

    else:

        anchor = max(0, len(df) - 50)

    return _anchored_vwap(df, anchor)


# ==========================================================
# CHOCH ANCHOR
# ==========================================================

def anchored_vwap_choch(df):

    ll = lowest(df["low"], 20)

    trigger = crossunder(df["close"], ll.shift(1))

    if trigger.any():

        idx = trigger[trigger].index[-1]

        anchor = df.index.get_loc(idx)

    else:

        anchor = max(0, len(df) - 50)

    return _anchored_vwap(df, anchor)


# ==========================================================
# BREAKOUT CANDLE ANCHOR
# ==========================================================

def anchored_vwap_breakout(df):

    rng = candle_range(df)

    avg = rng.rolling(20).mean()

    breakout = rng > (avg * 1.5)

    if breakout.any():

        idx = breakout[breakout].index[-1]

        anchor = df.index.get_loc(idx)

    else:

        anchor = max(0, len(df) - 30)

    return _anchored_vwap(df, anchor)


# ==========================================================
# AVWAP SNAPSHOT
# ==========================================================

def anchored_vwap_snapshot(df):

    price = safe_last(df["close"])

    sh = anchored_vwap_swing_high(df)

    sl = anchored_vwap_swing_low(df)

    bos = anchored_vwap_bos(df)

    choch = anchored_vwap_choch(df)

    breakout = anchored_vwap_breakout(df)

    return {

        "swing_high": safe_last(sh),
        "swing_low": safe_last(sl),
        "bos": safe_last(bos),
        "choch": safe_last(choch),
        "breakout": safe_last(breakout),

        "distance_high":
            vwap_distance(price, safe_last(sh)),

        "distance_low":
            vwap_distance(price, safe_last(sl)),

        "distance_bos":
            vwap_distance(price, safe_last(bos)),

        "distance_choch":
            vwap_distance(price, safe_last(choch)),

        "distance_breakout":
            vwap_distance(price, safe_last(breakout))

    }


# ==========================================================
# VWAP CONFLUENCE SCORE
# ==========================================================

def vwap_confluence_score(df):

    price = safe_last(df["close"])

    levels = [

        safe_last(session_vwap(df)),
        safe_last(daily_vwap(df)),
        safe_last(weekly_vwap(df)),
        safe_last(monthly_vwap(df)),
        safe_last(anchored_vwap_swing_high(df)),
        safe_last(anchored_vwap_swing_low(df)),
        safe_last(anchored_vwap_bos(df)),
        safe_last(anchored_vwap_choch(df)),
        safe_last(anchored_vwap_breakout(df))

    ]

    score = 0

    aligned = 0

    for level in levels:

        if abs(price - level) <= (price * 0.005):

            aligned += 1

            score += 10

    return {

        "score": min(score, 100),

        "aligned": aligned,

        "total": len(levels)

    }


# ==========================================================
# END OF PART 1D
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1E
# TREND ENGINE
# ==========================================================

# ==========================================================
# EMA TREND
# ==========================================================

def ema_trend(df):

    ema20 = ema(df["close"], 20)
    ema50 = ema(df["close"], 50)
    ema100 = ema(df["close"], 100)
    ema200 = ema(df["close"], 200)

    price = safe_last(df["close"])

    bullish = (
        price > safe_last(ema20) >
        safe_last(ema50) >
        safe_last(ema100) >
        safe_last(ema200)
    )

    bearish = (
        price < safe_last(ema20) <
        safe_last(ema50) <
        safe_last(ema100) <
        safe_last(ema200)
    )

    if bullish:
        trend = "STRONG_BULLISH"
    elif bearish:
        trend = "STRONG_BEARISH"
    elif price > safe_last(ema200):
        trend = "BULLISH"
    elif price < safe_last(ema200):
        trend = "BEARISH"
    else:
        trend = "SIDEWAYS"

    return {

        "trend": trend,

        "ema20": safe_last(ema20),
        "ema50": safe_last(ema50),
        "ema100": safe_last(ema100),
        "ema200": safe_last(ema200)

    }


# ==========================================================
# EMA ALIGNMENT SCORE
# ==========================================================

def ema_alignment_score(df):

    data = ema_trend(df)

    score = 0

    if data["ema20"] > data["ema50"]:
        score += 25

    if data["ema50"] > data["ema100"]:
        score += 25

    if data["ema100"] > data["ema200"]:
        score += 25

    if safe_last(df["close"]) > data["ema20"]:
        score += 25

    return score


# ==========================================================
# HMA TREND
# ==========================================================

def hma_trend(df):

    hma55 = hma(df["close"], 55)

    current = safe_last(hma55)

    previous = safe_previous(hma55)

    if current > previous:
        return "BULLISH"

    if current < previous:
        return "BEARISH"

    return "FLAT"


# ==========================================================
# PRICE TREND
# ==========================================================

def price_trend(df, length=20):

    hh = highest(df["high"], length)

    ll = lowest(df["low"], length)

    close = safe_last(df["close"])

    if close >= safe_last(hh):
        return "BREAKOUT"

    if close <= safe_last(ll):
        return "BREAKDOWN"

    midpoint = (
        safe_last(hh) +
        safe_last(ll)
    ) / 2

    if close > midpoint:
        return "UPTREND"

    return "DOWNTREND"


# ==========================================================
# TREND STRENGTH SCORE
# ==========================================================

def trend_strength_score(df):

    score = 0

    ema_score = ema_alignment_score(df)

    score += ema_score

    if hma_trend(df) == "BULLISH":
        score += 20

    if price_trend(df) == "BREAKOUT":
        score += 20

    if price_trend(df) == "UPTREND":
        score += 10

    return min(score, 100)


# ==========================================================
# TREND SNAPSHOT
# ==========================================================

def trend_snapshot(df):

    return {

        "ema": ema_trend(df),

        "hma": hma_trend(df),

        "price": price_trend(df),

        "strength":
            trend_strength_score(df)

    }


# ==========================================================
# END OF PART 1E
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1F
# MOMENTUM ENGINE
# ==========================================================

# ==========================================================
# MOMENTUM
# ==========================================================

def momentum(series, length=10):

    series = safe_series(series)

    return series - series.shift(length)


# ==========================================================
# RATE OF CHANGE (ROC)
# ==========================================================

def roc(series, length=10):

    series = safe_series(series)

    return (
        (series - series.shift(length))
        / series.shift(length)
    ) * 100


# ==========================================================
# RSI
# ==========================================================

def rsi(series, length=14):

    series = safe_series(series)

    delta = series.diff()

    gain = delta.clip(lower=0)

    loss = (-delta).clip(lower=0)

    avg_gain = gain.ewm(
        alpha=1 / length,
        adjust=False
    ).mean()

    avg_loss = loss.ewm(
        alpha=1 / length,
        adjust=False
    ).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)

    return 100 - (100 / (1 + rs))


# ==========================================================
# MACD
# ==========================================================

def macd(series,
         fast=12,
         slow=26,
         signal=9):

    fast_ema = ema(series, fast)

    slow_ema = ema(series, slow)

    macd_line = fast_ema - slow_ema

    signal_line = ema(macd_line, signal)

    histogram = macd_line - signal_line

    return {

        "macd": macd_line,

        "signal": signal_line,

        "histogram": histogram

    }


# ==========================================================
# MONEY FLOW INDEX
# ==========================================================

def mfi(df, length=14):

    tp = typical_price(df)

    money = tp * df["volume"]

    direction = tp.diff()

    positive = money.where(direction > 0, 0)

    negative = money.where(direction < 0, 0)

    pos = positive.rolling(length).sum()

    neg = negative.rolling(length).sum()

    ratio = pos / neg.replace(0, np.nan)

    return 100 - (100 / (1 + ratio))


# ==========================================================
# MOMENTUM SCORE
# ==========================================================

def momentum_score(df):

    score = 0

    r = safe_last(rsi(df["close"]))

    if r > 70:
        score += 25
    elif r > 50:
        score += 15

    macd_data = macd(df["close"])

    if safe_last(macd_data["histogram"]) > 0:
        score += 25

    if safe_last(macd_data["macd"]) > safe_last(macd_data["signal"]):
        score += 25

    m = safe_last(mfi(df))

    if m > 50:
        score += 25

    return min(score, 100)


# ==========================================================
# MOMENTUM SNAPSHOT
# ==========================================================

def momentum_snapshot(df):

    macd_data = macd(df["close"])

    return {

        "rsi":
            safe_last(rsi(df["close"])),

        "mfi":
            safe_last(mfi(df)),

        "momentum":
            safe_last(momentum(df["close"])),

        "roc":
            safe_last(roc(df["close"])),

        "macd":
            safe_last(macd_data["macd"]),

        "signal":
            safe_last(macd_data["signal"]),

        "histogram":
            safe_last(macd_data["histogram"]),

        "score":
            momentum_score(df)

    }


# ==========================================================
# END OF PART 1F
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1G
# TREND STRENGTH ENGINE
# ==========================================================

# ==========================================================
# DIRECTIONAL MOVEMENT (+DM / -DM)
# ==========================================================

def directional_movement(df):

    up_move = df["high"].diff()

    down_move = -df["low"].diff()

    plus_dm = up_move.where(
        (up_move > down_move) & (up_move > 0),
        0.0
    )

    minus_dm = down_move.where(
        (down_move > up_move) & (down_move > 0),
        0.0
    )

    return plus_dm, minus_dm


# ==========================================================
# DMI
# ==========================================================

def dmi(df, length=14):

    plus_dm, minus_dm = directional_movement(df)

    atr_value = atr(df, length)

    plus_di = (
        100 *
        rma(plus_dm, length) /
        atr_value.replace(0, np.nan)
    )

    minus_di = (
        100 *
        rma(minus_dm, length) /
        atr_value.replace(0, np.nan)
    )

    return plus_di, minus_di


# ==========================================================
# ADX
# ==========================================================

def adx(df, length=14):

    plus_di, minus_di = dmi(df, length)

    dx = (
        (plus_di - minus_di).abs() /
        (plus_di + minus_di).replace(0, np.nan)
    ) * 100

    return rma(dx, length)


# ==========================================================
# AROON
# ==========================================================

def aroon(df, length=25):

    aroon_up = (
        df["high"]
        .rolling(length)
        .apply(lambda x: np.argmax(x))
    )

    aroon_down = (
        df["low"]
        .rolling(length)
        .apply(lambda x: np.argmin(x))
    )

    up = ((length - aroon_up) / length) * 100

    down = ((length - aroon_down) / length) * 100

    return up, down


# ==========================================================
# ADX TREND
# ==========================================================

def adx_trend(df):

    value = safe_last(adx(df))

    if value >= 40:
        return "VERY_STRONG"

    if value >= 25:
        return "STRONG"

    if value >= 20:
        return "MODERATE"

    return "WEAK"


# ==========================================================
# TREND QUALITY SCORE
# ==========================================================

def trend_quality_score(df):

    score = 0

    adx_value = safe_last(adx(df))

    plus_di, minus_di = dmi(df)

    if adx_value >= 25:
        score += 40

    if safe_last(plus_di) > safe_last(minus_di):
        score += 30

    aroon_up, aroon_down = aroon(df)

    if safe_last(aroon_up) > safe_last(aroon_down):
        score += 30

    return min(score, 100)


# ==========================================================
# TREND STRENGTH SNAPSHOT
# ==========================================================

def trend_strength_snapshot(df):

    plus_di, minus_di = dmi(df)

    aroon_up, aroon_down = aroon(df)

    return {

        "adx":
            safe_last(adx(df)),

        "plus_di":
            safe_last(plus_di),

        "minus_di":
            safe_last(minus_di),

        "aroon_up":
            safe_last(aroon_up),

        "aroon_down":
            safe_last(aroon_down),

        "trend":
            adx_trend(df),

        "score":
            trend_quality_score(df)

    }


# ==========================================================
# END OF PART 1G
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1H
# SUPERTREND + ICHIMOKU ENGINE
# ==========================================================

# ==========================================================
# SUPERTREND
# ==========================================================

def supertrend(df, period=10, multiplier=3.0):

    atr_value = atr(df, period)

    hl2 = (df["high"] + df["low"]) / 2

    upper = hl2 + (multiplier * atr_value)
    lower = hl2 - (multiplier * atr_value)

    final_upper = upper.copy()
    final_lower = lower.copy()

    trend = pd.Series(index=df.index, dtype=float)

    for i in range(1, len(df)):

        if (
            upper.iloc[i] < final_upper.iloc[i - 1]
            or df["close"].iloc[i - 1] > final_upper.iloc[i - 1]
        ):
            final_upper.iloc[i] = upper.iloc[i]
        else:
            final_upper.iloc[i] = final_upper.iloc[i - 1]

        if (
            lower.iloc[i] > final_lower.iloc[i - 1]
            or df["close"].iloc[i - 1] < final_lower.iloc[i - 1]
        ):
            final_lower.iloc[i] = lower.iloc[i]
        else:
            final_lower.iloc[i] = final_lower.iloc[i - 1]

        if i == 1:
            trend.iloc[i] = final_lower.iloc[i]
            continue

        if trend.iloc[i - 1] == final_upper.iloc[i - 1]:

            if df["close"].iloc[i] <= final_upper.iloc[i]:
                trend.iloc[i] = final_upper.iloc[i]
            else:
                trend.iloc[i] = final_lower.iloc[i]

        else:

            if df["close"].iloc[i] >= final_lower.iloc[i]:
                trend.iloc[i] = final_lower.iloc[i]
            else:
                trend.iloc[i] = final_upper.iloc[i]

    direction = np.where(
        df["close"] > trend,
        1,
        -1
    )

    return {
        "line": trend,
        "direction": pd.Series(direction, index=df.index)
    }


# ==========================================================
# ICHIMOKU CLOUD
# ==========================================================

def ichimoku(df):

    conversion = (
        highest(df["high"], 9) +
        lowest(df["low"], 9)
    ) / 2

    base = (
        highest(df["high"], 26) +
        lowest(df["low"], 26)
    ) / 2

    span_a = (
        conversion + base
    ) / 2

    span_b = (
        highest(df["high"], 52) +
        lowest(df["low"], 52)
    ) / 2

    lagging = df["close"].shift(-26)

    return {

        "conversion": conversion,
        "base": base,
        "span_a": span_a,
        "span_b": span_b,
        "lagging": lagging

    }


# ==========================================================
# SUPERTREND SIGNAL
# ==========================================================

def supertrend_signal(df):

    st = supertrend(df)

    if safe_last(st["direction"]) > 0:
        return "BULLISH"

    return "BEARISH"


# ==========================================================
# ICHIMOKU SIGNAL
# ==========================================================

def ichimoku_signal(df):

    ichi = ichimoku(df)

    close = safe_last(df["close"])

    span_a = safe_last(ichi["span_a"])
    span_b = safe_last(ichi["span_b"])

    cloud_top = max(span_a, span_b)
    cloud_bottom = min(span_a, span_b)

    if close > cloud_top:
        return "BULLISH"

    if close < cloud_bottom:
        return "BEARISH"

    return "NEUTRAL"


# ==========================================================
# TREND CONFIRMATION
# ==========================================================

def trend_confirmation(df):

    score = 0

    if supertrend_signal(df) == "BULLISH":
        score += 50

    if ichimoku_signal(df) == "BULLISH":
        score += 50

    return {

        "score": score,

        "confirmed": score >= 100

    }


# ==========================================================
# INSTITUTIONAL TREND SCORE
# ==========================================================

def institutional_trend_score(df):

    base = trend_strength_score(df)

    quality = trend_quality_score(df)

    confirmation = trend_confirmation(df)["score"]

    return min(

        round(
            (base + quality + confirmation) / 3
        ),

        100

    )


# ==========================================================
# TREND ENGINE SNAPSHOT
# ==========================================================

def institutional_trend_snapshot(df):

    return {

        "supertrend":
            supertrend_signal(df),

        "ichimoku":
            ichimoku_signal(df),

        "confirmation":
            trend_confirmation(df),

        "institutional_score":
            institutional_trend_score(df)

    }


# ==========================================================
# END OF PART 1H
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1I
# VOLUME ENGINE
# ==========================================================

# ==========================================================
# ON BALANCE VOLUME (OBV)
# ==========================================================

def obv(df):

    close = safe_series(df["close"])
    volume = safe_series(df["volume"])

    direction = np.sign(close.diff()).fillna(0)

    return (direction * volume).cumsum()


# ==========================================================
# ACCUMULATION / DISTRIBUTION LINE (ADI)
# ==========================================================

def adi(df):

    high = df["high"]
    low = df["low"]
    close = df["close"]
    volume = df["volume"]

    mfm = (
        ((close - low) - (high - close))
        /
        (high - low).replace(0, np.nan)
    ).fillna(0)

    mfv = mfm * volume

    return mfv.cumsum()


# ==========================================================
# VOLUME SMA
# ==========================================================

def volume_sma(df, length=20):

    return df["volume"].rolling(length).mean()


# ==========================================================
# RELATIVE VOLUME
# ==========================================================

def relative_volume(df, length=20):

    avg = volume_sma(df, length)

    return df["volume"] / avg.replace(0, np.nan)


# ==========================================================
# VOLUME RATIO
# ==========================================================

def volume_ratio(df, length=20):

    rv = relative_volume(df, length)

    return safe_last(rv)


# ==========================================================
# VOLUME SPIKE
# ==========================================================

def volume_spike(df, multiplier=2.0):

    avg = safe_last(volume_sma(df))

    current = safe_last(df["volume"])

    return current >= (avg * multiplier)


# ==========================================================
# BUY / SELL VOLUME
# ==========================================================

def buy_sell_volume(df):

    buy = np.where(
        df["close"] >= df["open"],
        df["volume"],
        0
    )

    sell = np.where(
        df["close"] < df["open"],
        df["volume"],
        0
    )

    return {

        "buy": float(np.sum(buy)),

        "sell": float(np.sum(sell))

    }


# ==========================================================
# VOLUME TREND
# ==========================================================

def volume_trend(df):

    current = safe_last(df["volume"])

    average = safe_last(volume_sma(df))

    if current > average * 1.50:
        return "STRONG"

    if current > average:
        return "RISING"

    if current < average * 0.70:
        return "WEAK"

    return "NORMAL"


# ==========================================================
# VOLUME SCORE
# ==========================================================

def volume_score(df):

    score = 0

    if volume_spike(df):
        score += 30

    if volume_trend(df) == "STRONG":
        score += 30

    if safe_last(obv(df)) > safe_previous(obv(df)):
        score += 20

    if safe_last(adi(df)) > safe_previous(adi(df)):
        score += 20

    return min(score, 100)


# ==========================================================
# VOLUME SNAPSHOT
# ==========================================================

def volume_snapshot(df):

    bs = buy_sell_volume(df)

    return {

        "obv":
            safe_last(obv(df)),

        "adi":
            safe_last(adi(df)),

        "relative_volume":
            volume_ratio(df),

        "trend":
            volume_trend(df),

        "spike":
            volume_spike(df),

        "buy_volume":
            bs["buy"],

        "sell_volume":
            bs["sell"],

        "score":
            volume_score(df)

    }


# ==========================================================
# END OF PART 1I
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1J
# VOLATILITY ENGINE
# ==========================================================

# ==========================================================
# STANDARD DEVIATION
# ==========================================================

def standard_deviation(series, length=20):

    series = safe_series(series)

    return series.rolling(length).std()


# ==========================================================
# BOLLINGER BANDS
# ==========================================================

def bollinger_bands(series,
                    length=20,
                    deviation=2.0):

    basis = sma(series, length)

    std = standard_deviation(series, length)

    upper = basis + (std * deviation)

    lower = basis - (std * deviation)

    return {

        "basis": basis,

        "upper": upper,

        "lower": lower

    }


# ==========================================================
# BOLLINGER BAND WIDTH
# ==========================================================

def bollinger_width(series,
                    length=20,
                    deviation=2):

    bb = bollinger_bands(
        series,
        length,
        deviation
    )

    width = (

        (bb["upper"] - bb["lower"])

        /

        bb["basis"].replace(0, np.nan)

    ) * 100

    return width


# ==========================================================
# ATR %
# ==========================================================

def atr_percent(df,
                length=14):

    atr_value = atr(df, length)

    return (

        atr_value

        /

        df["close"]

    ) * 100


# ==========================================================
# HISTORICAL VOLATILITY
# ==========================================================

def historical_volatility(df,
                          length=20):

    returns = np.log(

        df["close"]

        /

        df["close"].shift(1)

    )

    hv = (

        returns

        .rolling(length)

        .std()

        * np.sqrt(252)

        * 100

    )

    return hv


# ==========================================================
# VOLATILITY STATE
# ==========================================================

def volatility_state(df):

    width = safe_last(

        bollinger_width(df["close"])

    )

    atrp = safe_last(

        atr_percent(df)

    )

    if width > 10 or atrp > 5:

        return "HIGH"

    elif width < 4 and atrp < 2:

        return "LOW"

    else:

        return "NORMAL"


# ==========================================================
# COMPRESSION
# ==========================================================

def compression(df):

    width = bollinger_width(df["close"])

    avg = width.rolling(20).mean()

    return safe_last(width) < safe_last(avg)


# ==========================================================
# EXPANSION
# ==========================================================

def expansion(df):

    width = bollinger_width(df["close"])

    avg = width.rolling(20).mean()

    return safe_last(width) > safe_last(avg)


# ==========================================================
# VOLATILITY SCORE
# ==========================================================

def volatility_score(df):

    score = 50

    if expansion(df):

        score += 25

    if compression(df):

        score -= 25

    hv = safe_last(

        historical_volatility(df)

    )

    if hv > 40:

        score += 25

    return max(

        0,

        min(

            score,

            100

        )

    )


# ==========================================================
# VOLATILITY SNAPSHOT
# ==========================================================

def volatility_snapshot(df):

    return {

        "atr":

            safe_last(

                atr(df)

            ),

        "atr_percent":

            safe_last(

                atr_percent(df)

            ),

        "bb_width":

            safe_last(

                bollinger_width(

                    df["close"]

                )

            ),

        "historical":

            safe_last(

                historical_volatility(df)

            ),

        "compression":

            compression(df),

        "expansion":

            expansion(df),

        "state":

            volatility_state(df),

        "score":

            volatility_score(df)

    }


# ==========================================================
# END OF PART 1J
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1K
# SUPPORT • RESISTANCE • PIVOT ENGINE
# ==========================================================

# ==========================================================
# CLASSIC PIVOT
# ==========================================================

def classic_pivot(df):

    h = safe_last(df["high"])
    l = safe_last(df["low"])
    c = safe_last(df["close"])

    pivot = (h + l + c) / 3

    r1 = (2 * pivot) - l
    s1 = (2 * pivot) - h

    r2 = pivot + (h - l)
    s2 = pivot - (h - l)

    r3 = h + 2 * (pivot - l)
    s3 = l - 2 * (h - pivot)

    return {

        "pivot": pivot,

        "r1": r1,
        "r2": r2,
        "r3": r3,

        "s1": s1,
        "s2": s2,
        "s3": s3

    }


# ==========================================================
# SUPPORT LEVEL
# ==========================================================

def support_level(df, length=50):

    return safe_last(

        lowest(df["low"], length)

    )


# ==========================================================
# RESISTANCE LEVEL
# ==========================================================

def resistance_level(df, length=50):

    return safe_last(

        highest(df["high"], length)

    )


# ==========================================================
# SUPPORT DISTANCE
# ==========================================================

def support_distance(df):

    close = safe_last(df["close"])

    support = support_level(df)

    return close - support


# ==========================================================
# RESISTANCE DISTANCE
# ==========================================================

def resistance_distance(df):

    close = safe_last(df["close"])

    resistance = resistance_level(df)

    return resistance - close


# ==========================================================
# SUPPORT STRENGTH
# ==========================================================

def support_strength(df):

    support = support_level(df)

    tolerance = support * 0.002

    touches = (

        abs(

            df["low"] - support

        ) <= tolerance

    ).sum()

    return min(

        int(touches * 10),

        100

    )


# ==========================================================
# RESISTANCE STRENGTH
# ==========================================================

def resistance_strength(df):

    resistance = resistance_level(df)

    tolerance = resistance * 0.002

    touches = (

        abs(

            df["high"] - resistance

        ) <= tolerance

    ).sum()

    return min(

        int(touches * 10),

        100

    )


# ==========================================================
# BREAKOUT LEVEL
# ==========================================================

def breakout_level(df):

    return resistance_level(df)


# ==========================================================
# BREAKDOWN LEVEL
# ==========================================================

def breakdown_level(df):

    return support_level(df)


# ==========================================================
# S/R SNAPSHOT
# ==========================================================

def support_resistance_snapshot(df):

    pivot = classic_pivot(df)

    return {

        "support":

            support_level(df),

        "resistance":

            resistance_level(df),

        "support_distance":

            support_distance(df),

        "resistance_distance":

            resistance_distance(df),

        "support_strength":

            support_strength(df),

        "resistance_strength":

            resistance_strength(df),

        "pivot":

            pivot

    }


# ==========================================================
# END OF PART 1K
# ==========================================================

# ==========================================================
# INDICATORS.PY
# PART 1L
# MARKET STRUCTURE ENGINE
# ==========================================================

# ==========================================================
# MARKET SWINGS
# ==========================================================

def market_swings(df, length=20):

    hh = safe_last(highest(df["high"], length))
    ll = safe_last(lowest(df["low"], length))

    ph = safe_previous(highest(df["high"], length))
    pl = safe_previous(lowest(df["low"], length))

    return {

        "hh": hh,
        "hl": pl,

        "lh": ph,
        "ll": ll

    }


# ==========================================================
# STRUCTURE TYPE
# ==========================================================

def market_structure(df):

    s = market_swings(df)

    if s["hh"] > s["lh"] and s["hl"] > s["ll"]:
        return "BULLISH"

    if s["hh"] < s["lh"] and s["hl"] < s["ll"]:
        return "BEARISH"

    return "RANGE"


# ==========================================================
# BOS CONFIRMATION
# ==========================================================

def bos_confirmation(df):

    close = safe_last(df["close"])

    swing = market_swings(df)

    if close > swing["lh"]:
        return "BULLISH"

    if close < swing["hl"]:
        return "BEARISH"

    return "NONE"


# ==========================================================
# CHOCH CONFIRMATION
# ==========================================================

def choch_confirmation(df):

    trend = market_structure(df)

    bos = bos_confirmation(df)

    if trend == "BULLISH" and bos == "BEARISH":
        return "BEARISH"

    if trend == "BEARISH" and bos == "BULLISH":
        return "BULLISH"

    return "NONE"


# ==========================================================
# STRUCTURE STRENGTH SCORE
# ==========================================================

def structure_strength_score(df):

    score = 0

    if market_structure(df) == "BULLISH":
        score += 35

    elif market_structure(df) == "BEARISH":
        score += 35

    if bos_confirmation(df) != "NONE":
        score += 35

    if choch_confirmation(df) == "NONE":
        score += 30

    return min(score, 100)


# ==========================================================
# HIGHER HIGH
# ==========================================================

def is_higher_high(df):

    s = market_swings(df)

    return s["hh"] > s["lh"]


# ==========================================================
# HIGHER LOW
# ==========================================================

def is_higher_low(df):

    s = market_swings(df)

    return s["hl"] > s["ll"]


# ==========================================================
# LOWER HIGH
# ==========================================================

def is_lower_high(df):

    s = market_swings(df)

    return s["hh"] < s["lh"]


# ==========================================================
# LOWER LOW
# ==========================================================

def is_lower_low(df):

    s = market_swings(df)

    return s["hl"] < s["ll"]


# ==========================================================
# STRUCTURE SNAPSHOT
# ==========================================================

def structure_snapshot(df):

    swings = market_swings(df)

    return {

        "trend":
            market_structure(df),

        "bos":
            bos_confirmation(df),

        "choch":
            choch_confirmation(df),

        "higher_high":
            is_higher_high(df),

        "higher_low":
            is_higher_low(df),

        "lower_high":
            is_lower_high(df),

        "lower_low":
            is_lower_low(df),

        "score":
            structure_strength_score(df),

        "swings":
            swings

    }


# ==========================================================
# END OF PART 1L
# ==========================================================
