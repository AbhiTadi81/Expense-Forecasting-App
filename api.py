from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/predict")
def predict():
    return {"prediction": 1000}