"""
Explainability Engine
"""


def generate_feature_explanations(features: dict):

    explanations = []

    if features.get("MAX_DELAY", 0) >= 3:
        explanations.append(
            "Customer has experienced severe payment delays."
        )

    if features.get("NUM_DELAY_MONTHS", 0) >= 3:
        explanations.append(
            "Customer delayed payments in multiple months."
        )

    if features.get("CREDIT_UTILIZATION", 0) > 1:
        explanations.append(
            "Credit utilization exceeds available credit limit."
        )

    if features.get("PAYMENT_RATIO", 1) < 0.20:
        explanations.append(
            "Customer pays only a small fraction of outstanding bills."
        )

    if features.get("LIMIT_BAL", 0) < 50000:
        explanations.append(
            "Customer has relatively low available credit."
        )

    if not explanations:
        explanations.append(
            "No major risk indicators detected."
        )

    return explanations