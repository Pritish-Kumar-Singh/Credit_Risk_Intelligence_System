"""
Prediction Pipeline
"""

from pathlib import Path

import joblib
import pandas as pd

from src.preprocessing import preprocess_customer
from src.feature_engineering import create_features
from src.recommendation_engine import generate_risk_report
from src.explainability import generate_feature_explanations

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "trained_models"
    / "credit_risk_xgb.pkl"
)

FEATURE_PATH = (
    BASE_DIR
    / "models"
    / "trained_models"
    / "feature_columns.pkl"
)

model = joblib.load(MODEL_PATH)

feature_columns = joblib.load(FEATURE_PATH)

def predict_customer(customer_data: dict) -> dict:

    df = preprocess_customer(customer_data)

    df = create_features(df)

    model_input = df[feature_columns]

    probability = model.predict_proba(
        model_input
    )[0][1]

    customer_features = model_input.iloc[0].to_dict()

    result = generate_risk_report(
        customer_features,
        probability
    )
    result["feature_explanations"] = (
    generate_feature_explanations(
        customer_features
    )
)

    return result