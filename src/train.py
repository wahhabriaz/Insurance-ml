from __future__ import annotations

import os
import joblib

from sklearn.model_selection import train_test_split

from src.data_loader import load_insurance_csv
from src.pipeline import build_pipeline, TARGET_COL

DATA_PATH = "data/insurance.csv"
MODEL_DIR = "models"
PIPELINE_PATH = os.path.join(MODEL_DIR, "insurance_lr_pipeline.joblib")


def main() -> None:
    os.makedirs(MODEL_DIR, exist_ok=True)

    df = load_insurance_csv(DATA_PATH)

    X = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, PIPELINE_PATH)

    print(f"Saved pipeline -> {PIPELINE_PATH}")
    print(f"Train rows: {len(X_train)}, Test rows: {len(X_test)}")


if __name__ == "__main__":
    main()
