from pathlib import Path
import sys
import json

BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

import streamlit as st
import requests

from src.metadata import (
    SEX_MAPPING,
    EDUCATION_MAPPING,
    MARRIAGE_MAPPING,
    PAYMENT_STATUS_MAPPING
)

st.set_page_config(
    page_title="Credit Risk Intelligence System",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Risk Intelligence System")

st.markdown(
    """
    Predict customer default risk and generate
    actionable credit risk recommendations.
    """
)

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:

    limit_bal = st.number_input(
        "Credit Limit",
        min_value=1,
        value=50000,
        help="Total credit limit assigned to the customer"
    )

    education = st.selectbox(
        "Education",
        options=list(EDUCATION_MAPPING.keys()),
        format_func=lambda x: EDUCATION_MAPPING[x]
    )

with col2:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30,
        help="Customer age in years"
    )

    sex = st.selectbox(
        "Gender",
        options=list(SEX_MAPPING.keys()),
        format_func=lambda x: SEX_MAPPING[x]
    )

    marriage = st.selectbox(
        "Marital Status",
        options=list(MARRIAGE_MAPPING.keys()),
        format_func=lambda x: MARRIAGE_MAPPING[x]
    )

st.header("Payment History")

st.info(
    """
Repayment Status Guide

- No Consumption
- Paid Duly
- Revolving Credit
- 1–8+ Month Payment Delay

Higher delays indicate higher credit risk.
"""
)

pay_0 = st.selectbox(
    "September 2005 Repayment Status",
    options=list(PAYMENT_STATUS_MAPPING.keys()),
    format_func=lambda x: PAYMENT_STATUS_MAPPING[x]
)

pay_2 = st.selectbox(
    "August 2005 Repayment Status",
    options=list(PAYMENT_STATUS_MAPPING.keys()),
    format_func=lambda x: PAYMENT_STATUS_MAPPING[x]
)

pay_3 = st.selectbox(
    "July 2005 Repayment Status",
    options=list(PAYMENT_STATUS_MAPPING.keys()),
    format_func=lambda x: PAYMENT_STATUS_MAPPING[x]
)

pay_4 = st.selectbox(
    "June 2005 Repayment Status",
    options=list(PAYMENT_STATUS_MAPPING.keys()),
    format_func=lambda x: PAYMENT_STATUS_MAPPING[x]
)

pay_5 = st.selectbox(
    "May 2005 Repayment Status",
    options=list(PAYMENT_STATUS_MAPPING.keys()),
    format_func=lambda x: PAYMENT_STATUS_MAPPING[x]
)

pay_6 = st.selectbox(
    "April 2005 Repayment Status",
    options=list(PAYMENT_STATUS_MAPPING.keys()),
    format_func=lambda x: PAYMENT_STATUS_MAPPING[x]
)

st.header("Bill Statement Amounts")

col1, col2, col3 = st.columns(3)

with col1:
    bill_amt1 = st.number_input(
        "September Bill Amount",
        value=10000
    )

    bill_amt4 = st.number_input(
        "June Bill Amount",
        value=10000
    )

with col2:
    bill_amt2 = st.number_input(
        "August Bill Amount",
        value=10000
    )

    bill_amt5 = st.number_input(
        "May Bill Amount",
        value=10000
    )

with col3:
    bill_amt3 = st.number_input(
        "July Bill Amount",
        value=10000
    )

    bill_amt6 = st.number_input(
        "April Bill Amount",
        value=10000
    )

st.caption(
    """
Bill amount represents the monthly credit card statement balance.
Negative values are allowed because some customers may have credit balances.
"""
)
    
st.header("Previous Payment Amounts")

col1, col2, col3 = st.columns(3)

with col1:
    pay_amt1 = st.number_input(
        "September Payment Amount",
        min_value=0,
        value=1000
    )

    pay_amt4 = st.number_input(
        "June Payment Amount",
        min_value=0,
        value=1000
    )

with col2:
    pay_amt2 = st.number_input(
        "August Payment Amount",
        min_value=0,
        value=1000
    )

    pay_amt5 = st.number_input(
        "May Payment Amount",
        min_value=0,
        value=1000
    )

with col3:
    pay_amt3 = st.number_input(
        "July Payment Amount",
        min_value=0,
        value=1000
    )

    pay_amt6 = st.number_input(
        "April Payment Amount",
        min_value=0,
        value=1000
    )

st.caption(
    """
Payment amount represents the actual amount paid by the customer during the month.

Higher payments generally reduce default risk.
"""
)

customer_data = {
    "LIMIT_BAL": limit_bal,
    "SEX": sex,
    "EDUCATION": education,
    "MARRIAGE": marriage,
    "AGE": age,

    "PAY_0": pay_0,
    "PAY_2": pay_2,
    "PAY_3": pay_3,
    "PAY_4": pay_4,
    "PAY_5": pay_5,
    "PAY_6": pay_6,

    "BILL_AMT1": bill_amt1,
    "BILL_AMT2": bill_amt2,
    "BILL_AMT3": bill_amt3,
    "BILL_AMT4": bill_amt4,
    "BILL_AMT5": bill_amt5,
    "BILL_AMT6": bill_amt6,

    "PAY_AMT1": pay_amt1,
    "PAY_AMT2": pay_amt2,
    "PAY_AMT3": pay_amt3,
    "PAY_AMT4": pay_amt4,
    "PAY_AMT5": pay_amt5,
    "PAY_AMT6": pay_amt6
}

if st.button(
    "Predict Credit Risk",
    use_container_width=True
):

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=customer_data,
            timeout=30
        )

        if response.status_code == 200:

            result = response.json()

            st.success(
                "Prediction generated successfully"
            )

            st.header("Risk Assessment")

            risk_level = result["risk_level"]

            probability = result[
                "default_probability"
            ]

            if risk_level == "HIGH":

                st.error(
                    f"Risk Level: {risk_level}"
                )

            elif risk_level == "MEDIUM":

                st.warning(
                    f"Risk Level: {risk_level}"
                )

            else:

                st.success(
                    f"Risk Level: {risk_level}"
                )

            st.metric(
                "Default Probability",
                f"{probability * 100:.2f}%"
            )

            st.progress(
                float(probability)
            )

            st.subheader(
                "Risk Drivers"
            )

            for driver in result[
                "risk_drivers"
            ]:

                st.warning(driver)

            st.subheader(
                "Recommendations"
            )

            for rec in result[
                "recommendations"
            ]:

                st.info(rec)

            if "feature_explanations" in result:

                st.subheader(
                    "Why did the model make this prediction?"
                )

                for item in result[
                    "feature_explanations"
                ]:

                    st.success(item)

            st.download_button(
                label="Download Risk Report",
                data=json.dumps(
                    result,
                    indent=4
                ),
                file_name="credit_risk_report.json",
                mime="application/json"
            )

        else:

            st.error(
                f"API Error: {response.text}"
            )

    except Exception as e:

        st.error(
            f"Connection Error: {str(e)}"
        )