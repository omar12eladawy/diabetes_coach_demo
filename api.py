from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.decisionTree import DecisionTree


app = FastAPI()
dt = DecisionTree()

class RecommendationRequest(BaseModel):
    glucose_value: float
    exercise_level: str
    glucose_trend: str
    is_Aerobic: bool


@app.post("/getRecommendation")
async def root(request: RecommendationRequest):
    dt.set_exercise_level(request.exercise_level)
    res = dt.eval_glucose(request.glucose_value, request.glucose_trend)
    return res

@app.get("/health")
async def root():
    return {"message": "App sate is healthy"}