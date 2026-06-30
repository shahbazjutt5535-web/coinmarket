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
