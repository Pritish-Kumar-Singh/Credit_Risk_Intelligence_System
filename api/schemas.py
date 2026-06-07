from pydantic import BaseModel, Field


class CustomerInput(BaseModel):

    LIMIT_BAL: float = Field(..., gt=0)

    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int = Field(..., gt=0)

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

    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float


class PredictionResponse(BaseModel):

    risk_level: str

    default_probability: float

    risk_drivers: list[str]

    recommendations: list[str]
    feature_explanations: list[str]