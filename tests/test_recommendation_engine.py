from src.recommendation_engine import generate_risk_report

customer = {
    "MAX_DELAY": 4,
    "NUM_DELAY_MONTHS": 5,
    "CREDIT_UTILIZATION": 1.2,
    "PAYMENT_RATIO": 0.12,
    "LIMIT_BAL": 30000
}

result = generate_risk_report(
    customer,
    0.81
)

print(result)