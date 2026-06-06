"""
Feature Engineering Module
"""

import numpy as np
import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    

    df["AGE_GROUP"] = pd.cut(
        df["AGE"],
        bins=[0, 30, 40, 50, 60, 100],
        labels=[1, 2, 3, 4, 5]
    ).astype(int)

    bill_cols = [
        "BILL_AMT1",
        "BILL_AMT2",
        "BILL_AMT3",
        "BILL_AMT4",
        "BILL_AMT5",
        "BILL_AMT6"
    ]

    df["TOTAL_BILL"] = df[bill_cols].sum(axis=1)

    df["AVG_BILL"] = df[bill_cols].mean(axis=1)

    payment_cols = [
        "PAY_AMT1",
        "PAY_AMT2",
        "PAY_AMT3",
        "PAY_AMT4",
        "PAY_AMT5",
        "PAY_AMT6"
    ]

    df["TOTAL_PAYMENT"] = df[payment_cols].sum(axis=1)

    df["AVG_PAYMENT"] = df[payment_cols].mean(axis=1)

    df["CREDIT_UTILIZATION"] = (
        df["TOTAL_BILL"]
        /
        (df["LIMIT_BAL"] + 1)
    )

    df["PAYMENT_RATIO"] = (
        df["TOTAL_PAYMENT"]
        /
        (df["TOTAL_BILL"].abs() + 1)
    )

    delay_cols = [
        "PAY_0",
        "PAY_2",
        "PAY_3",
        "PAY_4",
        "PAY_5",
        "PAY_6"
    ]

    df["AVG_DELAY"] = (
        df[delay_cols]
        .mean(axis=1)
    )

    df["MAX_DELAY"] = (
        df[delay_cols]
        .max(axis=1)
    )

    df["NUM_DELAY_MONTHS"] = (
        (df[delay_cols] > 0)
        .sum(axis=1)
    )

    df["RECENT_DELAY_FLAG"] = (
        df["PAY_0"] > 0
    ).astype(int)

    df["BILL_GROWTH"] = (
        df["BILL_AMT1"]
        -
        df["BILL_AMT6"]
    )

    df["PAYMENT_STD"] = (
        df[payment_cols]
        .std(axis=1)
        .fillna(0)
    )

    return df