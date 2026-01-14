from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = {"age", "sex", "bmi", "children", "smoker", "region", "charges"}


def load_insurance_csv(path: str) -> pd.DataFrame:
    """
    Load the insurance dataset and validate required columns.
    Fails fast if schema is unexpected.
    """
    df = pd.read_csv(path)

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    # Basic sanity checks
    if df.empty:
        raise ValueError("Loaded dataset is empty.")

    return df
