import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Orbit Sentiment API")

# Загружаем сохраненную модель
try:
    model = joblib.load("model.pkl")
except Exception:
    model = None

# Формат входящих данных
class TextRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok", "model_ready": model is not None}

@app.post("/predict")
def predict(request: TextRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Модель не загружена")
    
    clean_text = request.text.strip()
    if not clean_text:
        raise HTTPException(status_code=400, detail="Текст пустой")

    prediction = model.predict([clean_text])[0]
    return {
        "text": clean_text,
        "sentiment": str(prediction)
    }
