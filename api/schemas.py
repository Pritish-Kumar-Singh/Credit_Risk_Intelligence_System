from pydantic import BaseModel, Field, field_validator


class CustomerInput(BaseModel):

    LIMIT_BAL: float = Field(..., gt=0, le=10000000)

    SEX: int

    EDUCATION: int

    MARRIAGE: int

    AGE: int = Field(..., gt=0, le=120)

    PAY_0: int
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int

    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float

    PAY_AMT1: float = Field(..., ge=0)
    PAY_AMT2: float = Field(..., ge=0)
    PAY_AMT3: float = Field(..., ge=0)
    PAY_AMT4: float = Field(..., ge=0)
    PAY_AMT5: float = Field(..., ge=0)
    PAY_AMT6: float = Field(..., ge=0)

    @field_validator("SEX")
    @classmethod
    def validate_sex(cls, value):
        if value not in (1, 2):
            raise ValueError(
                "SEX must be 1 (Male) or 2 (Female)"
            )
        return value

    @field_validator("EDUCATION")
    @classmethod
    def validate_education(cls, value):
        if value not in (1, 2, 3, 4):
            raise ValueError(
                "EDUCATION must be 1,2,3 or 4"
            )
        return value

    @field_validator("MARRIAGE")
    @classmethod
    def validate_marriage(cls, value):
        if value not in (1, 2, 3):
            raise ValueError(
                "MARRIAGE must be 1,2 or 3"
            )
        return value

    @field_validator(
        "PAY_0",
        "PAY_2",
        "PAY_3",
        "PAY_4",
        "PAY_5",
        "PAY_6"
    )
    @classmethod
    def validate_payment_status(cls, value):
        if value < -2 or value > 8:
            raise ValueError(
                "Payment status must be between -2 and 8"
            )
        return value


class PredictionResponse(BaseModel):

    risk_level: str

    default_probability: float

    risk_drivers: list[str]

    recommendations: list[str]

    feature_explanations: list[str]