import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

from sklearn.metrics import mean_squared_error, mean_absolute_error

import bentoml

from datetime import datetime
import os

# Replace the categories with their corresponding frequencies
# previously calculated
MODEL_REPLACE_RULES = {
    'Focus': 7.4e-05,
    ' Ranger': 7.4e-05,
    ' Transit Tourneo': 7.4e-05,
    ' Escort': 7.4e-05,
    ' Streetka': 0.000148,
    ' Fusion': 0.000891,
    ' Tourneo Connect': 0.002004,
    ' Mustang': 0.003414,
    ' Tourneo Custom': 0.003637,
    ' Grand Tourneo Connect': 0.003637,
    ' Puma': 0.004527,
    ' KA': 0.01091,
    ' Edge': 0.011578,
    ' Galaxy': 0.012097,
    ' Grand C-MAX': 0.012765,
    ' S-MAX': 0.016328,
    ' B-MAX': 0.018703,
    ' C-MAX': 0.029761,
    ' Ka+': 0.030058,
    ' Mondeo': 0.030503,
    ' EcoSport': 0.063307,
    ' Kuga': 0.124091,
    ' Focus': 0.254861,
    ' Fiesta': 0.366558,
    'Other': 0
}

DROP_FUEL_TYPE = ["Electric", "Hybrid"]

if __name__ == "__main__":
    # read test data from csv file ford_test.csv
    TRAIN_PATH = os.path.join(os.path.dirname(__file__), "data/ford_train.csv")
    TEST_PATH = os.path.join(os.path.dirname(__file__), "data/ford_test.csv")

    ford_df = pd.read_csv(TRAIN_PATH)

    # Define the transformer pipeline for the dataframe
    feature_eng_tfm = ColumnTransformer(
        [
            (
                "Mileage",
                Pipeline([
                    ("Log1P", FunctionTransformer(np.log1p)),
                    ("Scaler", StandardScaler())
                ]),
                ["mileage"]
            ),
            (
                "transmission",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse=False
                ),
                ["transmission"]
            ),
            (
                "fuelType",
                # Replace the fuelType "Electric" or "Hybrid" with "other"
                # and OneHotEncoder will ignore it.
                # This is a small trick to implement the frequency encoder
                Pipeline(
                    [
                        (
                            f"inputer_{d}",
                            SimpleImputer(
                                missing_values=d,
                                strategy="constant",
                                fill_value="other"
                            )
                        )
                        for d in DROP_FUEL_TYPE
                    ]+[
                        (
                            "OneHotEncoder",
                            OneHotEncoder(
                                handle_unknown="ignore",
                                sparse=False
                            ),
                        )
                    ]
                ),
                ["fuelType"]
            ),
            (
                "model",
                # replace model with the corresponding frequency in MODEL_REPLACE_RULES
                Pipeline(
                    [
                        (
                            f"inputer_{column_value}",
                            SimpleImputer(
                                missing_values=column_value,
                                strategy="constant",
                                fill_value=value
                            )
                        )
                        for column_value, value
                        in MODEL_REPLACE_RULES.items()
                    ]
                ),
                ["model"]
            ),
            (
                "year",
                Pipeline([
                    ("Scaler", StandardScaler())
                ]),
                ["year"]
            ),
            (
                "engineSize",
                Pipeline([
                    ("Scaler", StandardScaler())
                ]),
                ["engineSize"]
            ),
            (
                "tax",
                Pipeline([
                    ("Log1P", FunctionTransformer(np.log1p)),
                    ("Scaler", StandardScaler())
                ]),
                ["tax"]
            ),
            (
                "mpg",
                Pipeline([
                    ("Scaler", StandardScaler())
                ]),
                ["mpg"]
            )
        ],
        remainder="drop"
    )

    # Define the regressor model
    xgb_reg = XGBRegressor(
        max_depth=None,
        n_estimators=100,
        random_state=214,
    )

    ml_model = Pipeline([
        ("FeatureEngineering", feature_eng_tfm),
        ("Regressor", xgb_reg)
    ])

    # Train the model to predict the price of the car
    print(f"[{datetime.now()}] Training the model...")

    ml_model.fit(
        ford_df.drop(columns=["price"]),
        ford_df["price"]
    )

    print(f"[{datetime.now()}] Saving the model...")

    # Model on Test Data
    # MSE
    print(f"[{datetime.now()}] Calculating MSE on the test data...")
    ford_df_test = pd.read_csv(TEST_PATH)
    y_pred = ml_model.predict(ford_df_test)
    mse = mean_squared_error(ford_df_test["price"], y_pred)
    print(f"[{datetime.now()}] MSE on the test data: {mse}")
    # MAE
    mae = mean_absolute_error(ford_df_test["price"], y_pred)
    print(f"[{datetime.now()}] MAE on the test data: {mae}")

    # Save the model to a bento service
    model_id = bentoml.sklearn.save_model(
        "ford_price_predictor",
        ml_model
    )

    print(f"[{datetime.now()}] Model - {ml_model}")
