from fastapi import FastAPI
from fastapi import HTTPException

from api.schemas import (
    CustomerInput,
    PredictionResponse
)

from src.predict import predict_customer


app = FastAPI(
    title="Credit Risk Intelligence System",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message":
        "Credit Risk Intelligence System API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
    payload: CustomerInput
):

    try:

        result = predict_customer(
            payload.model_dump()
        )

        return result

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction Error: {str(e)}"
        )