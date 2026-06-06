from src.predict import predict_customer

customer = {
    "LIMIT_BAL": 20000,
    "SEX": 2,
    "EDUCATION": 2,
    "MARRIAGE": 1,
    "AGE": 35,

    "PAY_0": 3,
    "PAY_2": 2,
    "PAY_3": 2,
    "PAY_4": 1,
    "PAY_5": 0,
    "PAY_6": 0,

    "BILL_AMT1": 50000,
    "BILL_AMT2": 48000,
    "BILL_AMT3": 47000,
    "BILL_AMT4": 45000,
    "BILL_AMT5": 43000,
    "BILL_AMT6": 42000,

    "PAY_AMT1": 1000,
    "PAY_AMT2": 1000,
    "PAY_AMT3": 1000,
    "PAY_AMT4": 1000,
    "PAY_AMT5": 1000,
    "PAY_AMT6": 1000
}

result = predict_customer(customer)

print(result)