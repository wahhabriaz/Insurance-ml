from __future__ import annotations

import joblib
import pandas as pd

from src.preprocessing import load_feature_columns

MODEL_PATH = "models/linear_regression.joblib"
COLUMNS_PATH = "models/feature_columns.json"


def predict_one(payload: dict) -> float:
    """
    payload example:
    {
      "age": 31,
      "sex": "female",
      "bmi": 27.9,
      "children": 0,
      "smoker": "yes",
      "region": "southwest"
    }
    """
    model = joblib.load(MODEL_PATH)
    feature_columns = load_feature_columns(COLUMNS_PATH)

    # Convert to dataframe
    df = pd.DataFrame([payload])

    # Apply same encoding as training (get_dummies with drop_first=True)
    df_enc = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True)

    # Align columns to training schema
    for col in feature_columns:
        if col not in df_enc.columns:
            df_enc[col] = 0

    df_enc = df_enc[feature_columns]

    pred = model.predict(df_enc)[0]
    return float(pred)


if __name__ == "__main__":
    sample = {
        "age": 31,
        "sex": "female",
        "bmi": 27.9,
        "children": 0,
        "smoker": "yes",
        "region": "southwest",
    }
    print("Predicted charges:", predict_one(sample))
