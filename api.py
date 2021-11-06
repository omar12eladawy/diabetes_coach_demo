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

    return {
                # 'case_increase': 'No Ex, consider insulin correction ',
                'case_increase': None,
                'case_decrease': {
                    'text_AE': 'Not ready for Exercise.',
                    'text_other': 'Not ready for Exercise.',
                    'insulin_rec_AE': 'Insulin Correction needed!',
                    'insulin_rec_other': 'Insulin Correction needed!',
                    'food_rec': None,
                },
                'color': 'red'
            }


@app.get("/health")
async def root():
    return {"message": "App sate is healthy"}