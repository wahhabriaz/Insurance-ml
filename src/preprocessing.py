from __future__ import annotations

import json
from typing import Tuple, List

import pandas as pd


CATEGORICAL_COLS = ["sex", "smoker", "region"]
TARGET_COL = "charges"


def preprocess(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series, List[str]]:
    """
    One-hot encode categorical variables and split into X/y.
    Returns X, y, and the feature column order.
    """
    df_encoded = pd.get_dummies(df, columns=CATEGORICAL_COLS, drop_first=True)

    X = df_encoded.drop(columns=[TARGET_COL])
    y = df_encoded[TARGET_COL]

    feature_columns = list(X.columns)
    return X, y, feature_columns


def save_feature_columns(feature_columns: List[str], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(feature_columns, f, indent=2)


def load_feature_columns(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
