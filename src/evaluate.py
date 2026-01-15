from __future__ import annotations

import joblib
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

from src.data_loader import load_insurance_csv
from src.pipeline import TARGET_COL

DATA_PATH = "data/insurance.csv"
PIPELINE_PATH = "models/insurance_lr_pipeline.joblib"


def main() -> None:
    df = load_insurance_csv(DATA_PATH)

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = joblib.load(PIPELINE_PATH)
    preds = pipeline.predict(X_test)

    r2 = r2_score(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    print(f"R²   : {r2:.4f}")
    print(f"RMSE : {rmse:.2f}")


if __name__ == "__main__":
    main()
