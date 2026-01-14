from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

from src.predict import predict_one


app = FastAPI(
    title="Insurance Charges Prediction API",
    version="1.0.0",
    description="Predict insurance charges using a trained multiple linear regression model.",
)

# CORS: keep permissive for local dev; tighten later for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PredictRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")  # reject unknown fields

    age: int = Field(..., ge=18, le=64, description="Age of the insured")
    sex: Literal["male", "female"]
    bmi: float = Field(..., ge=10, le=70, description="Body mass index")
    children: int = Field(..., ge=0, le=10)
    smoker: Literal["yes", "no"]
    region: Literal["northeast", "northwest", "southeast", "southwest"]


class PredictResponse(BaseModel):
    predicted_charges: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        pred = predict_one(req.model_dump())
        return PredictResponse(predicted_charges=pred)
    except FileNotFoundError as e:
        # model artifacts not found
        raise HTTPException(status_code=500, detail=f"Model files missing: {str(e)}")
    except Exception as e:
        # avoid leaking internals; keep message useful
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")
