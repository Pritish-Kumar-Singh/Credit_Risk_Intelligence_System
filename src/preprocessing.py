"""
Data Preprocessing Module
Credit Risk Intelligence System
"""

import pandas as pd


REQUIRED_COLUMNS = [
    "LIMIT_BAL",
    "SEX",
    "EDUCATION",
    "MARRIAGE",
    "AGE",
    "PAY_0",
    "PAY_2",
    "PAY_3",
    "PAY_4",
    "PAY_5",
    "PAY_6",
    "BILL_AMT1",
    "BILL_AMT2",
    "BILL_AMT3",
    "BILL_AMT4",
    "BILL_AMT5",
    "BILL_AMT6",
    "PAY_AMT1",
    "PAY_AMT2",
    "PAY_AMT3",
    "PAY_AMT4",
    "PAY_AMT5",
    "PAY_AMT6"
]


def validate_input(customer_data: dict) -> None:
    """
    Validate incoming customer payload.
    """
    
    # Required Fields
 
    missing_columns = [
        col
        for col in REQUIRED_COLUMNS
        if col not in customer_data
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required fields: {missing_columns}"
        )

    # Basic Validation

    if customer_data["AGE"] <= 0:
        raise ValueError(
            "AGE must be greater than 0"
        )

    if customer_data["LIMIT_BAL"] <= 0:
        raise ValueError(
            "LIMIT_BAL must be greater than 0"
        )

    # Categorical Validation

    if customer_data["SEX"] not in [1, 2]:
        raise ValueError(
            "SEX must be 1 (Male) or 2 (Female)"
        )

    if customer_data["EDUCATION"] not in [1, 2, 3, 4]:
        raise ValueError(
            "EDUCATION must be 1, 2, 3 or 4"
        )

    if customer_data["MARRIAGE"] not in [1, 2, 3]:
        raise ValueError(
            "MARRIAGE must be 1, 2 or 3"
        )

    # Payment Status Validation

    pay_cols = [
        "PAY_0",
        "PAY_2",
        "PAY_3",
        "PAY_4",
        "PAY_5",
        "PAY_6"
    ]

    for col in pay_cols:

        if customer_data[col] < -2:
            raise ValueError(
                f"{col} cannot be less than -2"
            )

        if customer_data[col] > 8:
            raise ValueError(
                f"{col} cannot be greater than 8"
            )

    # Payment Amount Validation
 
    payment_cols = [
        "PAY_AMT1",
        "PAY_AMT2",
        "PAY_AMT3",
        "PAY_AMT4",
        "PAY_AMT5",
        "PAY_AMT6"
    ]

    for col in payment_cols:

        if customer_data[col] < 0:
            raise ValueError(
                f"{col} cannot be negative"
            )

    # Age Range Validation
  
    if customer_data["AGE"] > 120:
        raise ValueError(
            "AGE appears unrealistic"
        )

    # Credit Limit Validation

    if customer_data["LIMIT_BAL"] > 10000000:
        raise ValueError(
            "LIMIT_BAL appears unrealistic"
        )


def preprocess_customer(customer_data: dict) -> pd.DataFrame:
    """
    Convert raw customer input into DataFrame.
    """

    validate_input(customer_data)

    df = pd.DataFrame([customer_data])

    return df