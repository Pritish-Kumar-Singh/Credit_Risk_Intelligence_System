"""
Model Training Pipeline
"""

from pathlib import Path
import json
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

from xgboost import XGBClassifier

# Paths

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "credit_risk_feature_engineered.csv"
)

MODEL_DIR = (
    BASE_DIR
    / "models"
    / "trained_models"
)

MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)

MODEL_PATH = (
    MODEL_DIR
    / "credit_risk_xgb.pkl"
)

FEATURE_PATH = (
    MODEL_DIR
    / "feature_columns.pkl"
)

METADATA_PATH = (
    MODEL_DIR
    / "model_metadata.json"
)

# Load Dataset

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset Shape:", df.shape)

# Feature Selection

target = "default payment next month"

feature_columns = [
    col
    for col in df.columns
    if col not in [
        target,
        "ID"
    ]
]

X = df[feature_columns]

y = df[target]

print("Features:", len(feature_columns))

# Train/Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Class Imbalance Handling

negative_class = (y_train == 0).sum()

positive_class = (y_train == 1).sum()

scale_pos_weight = (
    negative_class /
    positive_class
)

print(
    "scale_pos_weight:",
    round(scale_pos_weight, 4)
)

# Final Production Model

model = XGBClassifier(
    n_estimators=300,
    max_depth=3,
    learning_rate=0.03,
    subsample=0.8,
    colsample_bytree=0.9,
    min_child_weight=3,
    gamma=0,
    scale_pos_weight=scale_pos_weight,
    random_state=42,
    eval_metric="logloss"
)

print("Training model...")

model.fit(
    X_train,
    y_train
)

# Evaluation

y_prob = model.predict_proba(
    X_test
)[:, 1]

roc_auc = roc_auc_score(
    y_test,
    y_prob
)

print(
    "ROC-AUC:",
    round(roc_auc, 4)
)

# Save Artifacts

joblib.dump(
    model,
    MODEL_PATH
)

joblib.dump(
    feature_columns,
    FEATURE_PATH
)

metadata = {
    "model_name": "XGBoost",
    "roc_auc": round(float(roc_auc), 4),
    "threshold": 0.55,
    "num_features": len(feature_columns),
    "train_rows": int(len(X_train)),
    "test_rows": int(len(X_test))
}

with open(
    METADATA_PATH,
    "w"
) as f:
    json.dump(
        metadata,
        f,
        indent=4
    )

print("\nArtifacts Saved")

print(MODEL_PATH)
print(FEATURE_PATH)
print(METADATA_PATH)