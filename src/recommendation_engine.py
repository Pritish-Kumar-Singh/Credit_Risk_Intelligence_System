

def get_risk_level(probability: float) -> str:
    """
    Convert probability into risk category.
    """

    if probability >= 0.75:
        return "HIGH"

    elif probability >= 0.45:
        return "MEDIUM"

    return "LOW"


def identify_risk_drivers(customer: dict) -> list:
    """
    Identify major factors contributing to risk.
    """

    drivers = []

    if customer["MAX_DELAY"] >= 3:
        drivers.append(
            "Multiple severe payment delays detected"
        )

    if customer["NUM_DELAY_MONTHS"] >= 3:
        drivers.append(
            "Frequent late payment behavior"
        )

    if customer["CREDIT_UTILIZATION"] > 0.80:
        drivers.append(
            "High credit utilization"
        )

    if customer["PAYMENT_RATIO"] < 0.20:
        drivers.append(
            "Low repayment ratio"
        )

    if customer["LIMIT_BAL"] < 50000:
        drivers.append(
            "Low available credit limit"
        )

    return drivers


def generate_recommendations(customer: dict) -> list:
    """
    Generate business recommendations.
    """

    recommendations = []

    if customer["MAX_DELAY"] >= 3:
        recommendations.append(
            "Increase account monitoring frequency"
        )

    if customer["NUM_DELAY_MONTHS"] >= 3:
        recommendations.append(
            "Review repayment behavior before extending credit"
        )

    if customer["CREDIT_UTILIZATION"] > 0.80:
        recommendations.append(
            "Avoid increasing current credit exposure"
        )

    if customer["PAYMENT_RATIO"] < 0.20:
        recommendations.append(
            "Encourage higher repayment amounts"
        )

    if not recommendations:
        recommendations.append(
            "Maintain current credit strategy"
        )

    return recommendations


def generate_risk_report(
    customer: dict,
    probability: float
) -> dict:
    """
    Main recommendation engine output.
    """

    return {
        "risk_level":
            get_risk_level(probability),

        "default_probability":
            round(float(probability), 4),

        "risk_drivers":
            identify_risk_drivers(customer),

        "recommendations":
            generate_recommendations(customer)
    }