from fastapi import FastAPI
import requests
import joblib
import uvicorn
from data import get_data 
import pandas as pd
import numpy as np

model = joblib.load('best_model.pkl')
encoder = joblib.load('label_encoder.pkl')


app = FastAPI()


@app.get('/')
def home():
    return {'massage': 'Welcome'}

@app.post('/predict')
def predict(data : get_data):
    df = pd.DataFrame(data.dict(), index=[0])
    df.rename(columns={
        "Temperature": "Temperature (C)",
        "Wind_Speed": "Wind Speed (km/h)"
        },inplace=True)
    prediction = model.predict(df)[0]
    return {"predicted_prognosis": encoder.inverse_transform([prediction])[0]}


