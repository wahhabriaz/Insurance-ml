from __future__ import annotations

import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from src.data_loader import load_insurance_csv
from src.preprocessing import preprocess, save_feature_columns


DATA_PATH = "data/insurance.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "linear_regression.joblib")
COLUMNS_PATH = os.path.join(MODEL_DIR, "feature_columns.json")


def main() -> None:
    os.makedirs(MODEL_DIR, exist_ok=True)

    df = load_insurance_csv(DATA_PATH)
    X, y, feature_columns = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    save_feature_columns(feature_columns, COLUMNS_PATH)

    print(f"Saved model -> {MODEL_PATH}")
    print(f"Saved feature columns -> {COLUMNS_PATH}")
    print(f"Train rows: {len(X_train)}, Test rows: {len(X_test)}")


if __name__ == "__main__":
    main()
