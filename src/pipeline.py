from __future__ import annotations

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

NUM_COLS = ["age", "bmi", "children"]
CAT_COLS = ["sex", "smoker", "region"]
TARGET_COL = "charges"


def build_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", NUM_COLS),
            (
                "cat",
                OneHotEncoder(drop="first", handle_unknown="ignore"),
                CAT_COLS,
            ),
        ]
    )

    model = LinearRegression()

    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )
