from __future__ import annotations

import joblib
import pandas as pd

PIPELINE_PATH = "models/insurance_lr_pipeline.joblib"


def predict_one(payload: dict) -> float:
    pipeline = joblib.load(PIPELINE_PATH)
    df = pd.DataFrame([payload])
    pred = pipeline.predict(df)[0]
    return float(pred)


if __name__ == "__main__":
    base = {
        "age": 40,
        "sex": "male",
        "bmi": 28,
        "children": 2,
        "region": "northwest",
    }

    print("NON-SMOKER:", predict_one({**base, "smoker": "no"}))
    print("SMOKER    :", predict_one({**base, "smoker": "yes"}))
