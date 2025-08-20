from fastapi import FastAPI
from pydantic import BaseModel
import re
import joblib
import numpy as np


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords   

stopwords = set(stopwords.words('english'))



def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = ' '.join(word for word in text.split() if word not in stopwords)
    return text


with open("vectorizer.pkl", "rb") as f:
    vectorizer = joblib.load(f)

with open("xgb_model.pkl", "rb") as f:
    model = joblib.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = joblib.load(f)    


app = FastAPI(title="Domain Classification API")

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input_data: InputText):
    cleaned_text = preprocess_text(input_data.text)
    X = vectorizer.transform([cleaned_text])
    prediction = model.predict(X)[0]
    pred_label = label_encoder.inverse_transform([prediction])[0]  # get single label
    return {"prediction": pred_label}


