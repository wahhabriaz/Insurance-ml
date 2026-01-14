from __future__ import annotations

import joblib
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

from src.data_loader import load_insurance_csv
from src.preprocessing import preprocess

DATA_PATH = "data/insurance.csv"
MODEL_PATH = "models/linear_regression.joblib"


def main() -> None:
    df = load_insurance_csv(DATA_PATH)
    X, y, _ = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = joblib.load(MODEL_PATH)
    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    print(f"R²   : {r2:.4f}")
    print(f"RMSE : {rmse:.2f}")


if __name__ == "__main__":
    main()
