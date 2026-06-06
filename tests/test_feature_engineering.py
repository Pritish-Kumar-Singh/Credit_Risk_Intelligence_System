from src.preprocessing import preprocess_customer
from src.feature_engineering import create_features


customer = {
    "LIMIT_BAL": 50000,
    "SEX": 2,
    "EDUCATION": 2,
    "MARRIAGE": 1,
    "AGE": 30,
    "PAY_0": 0,
    "PAY_2": 1,
    "PAY_3": 0,
    "PAY_4": 2,
    "PAY_5": 0,
    "PAY_6": 0,
    "BILL_AMT1": 10000,
    "BILL_AMT2": 12000,
    "BILL_AMT3": 11000,
    "BILL_AMT4": 13000,
    "BILL_AMT5": 12500,
    "BILL_AMT6": 10000,
    "PAY_AMT1": 1000,
    "PAY_AMT2": 1200,
    "PAY_AMT3": 1100,
    "PAY_AMT4": 900,
    "PAY_AMT5": 1000,
    "PAY_AMT6": 1000
}

df = preprocess_customer(customer)

df = create_features(df)

print(df.columns.tolist())

print("\nTotal Columns:", len(df.columns))