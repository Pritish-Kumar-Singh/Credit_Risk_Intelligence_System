"""
Metadata Repository

Used by:
- Streamlit UI
- FastAPI Documentation
- Validation Layer
"""

SEX_MAPPING = {
    1: "Male",
    2: "Female"
}

EDUCATION_MAPPING = {
    1: "Graduate School",
    2: "University",
    3: "High School",
    4: "Other"
}

MARRIAGE_MAPPING = {
    1: "Married",
    2: "Single",
    3: "Other"
}

PAYMENT_STATUS_MAPPING = {
    -2: "No Consumption",
    -1: "Paid Duly",
     0: "Revolving Credit",
     1: "1 Month Delay",
     2: "2 Months Delay",
     3: "3 Months Delay",
     4: "4 Months Delay",
     5: "5 Months Delay",
     6: "6 Months Delay",
     7: "7 Months Delay",
     8: "8+ Months Delay"
}
FIELD_DESCRIPTIONS = {
    "LIMIT_BAL":
        "Total credit limit assigned to the customer",

    "SEX":
        "Customer gender (1=Male, 2=Female)",

    "EDUCATION":
        "Education level",

    "MARRIAGE":
        "Marital status",

    "AGE":
        "Customer age in years",

    "PAY_0":
        "Repayment status in September 2005",

    "PAY_2":
        "Repayment status in August 2005",

    "PAY_3":
        "Repayment status in July 2005",

    "PAY_4":
        "Repayment status in June 2005",

    "PAY_5":
        "Repayment status in May 2005",

    "PAY_6":
        "Repayment status in April 2005"
}