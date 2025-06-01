from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the trained model
model = joblib.load("ml/model.pkl")  # Use relative path if needed

# Define the request body schema
class InputData(BaseModel):
    age: int
    gender: int
    family_history: int
    work_interfere: int
    benefits: int
    care_options: int
    seek_help: int
    mental_health_consequence: int

# Define the prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    input_data = [[
        data.age,
        data.gender,
        data.family_history,
        data.work_interfere,
        data.benefits,
        data.care_options,
        data.seek_help,
        data.mental_health_consequence
    ]]
    prediction = model.predict(input_data)
    return {"treatment_needed": bool(prediction[0])}
