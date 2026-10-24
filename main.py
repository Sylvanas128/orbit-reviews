import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Создаем приложение FastAPI
app = FastAPI(title="Orbit Reviews API", description="API для определения тональности отзывов")

# Загружаем вашу модель один раз при старте сервера
try:
    model = joblib.load("model.pkl")
except Exception as e:
    model = None
    print(f"Ошибка загрузки модели model.pkl: {e}")

# Описываем, в каком виде принимаем текст (в формате JSON)
class ReviewInput(BaseModel):
    text: str

# Главная страница API (для проверки, что сервер работает)
@app.get("/")
def read_root():
    return {"status": "working", "message": "FastAPI для Orbit Reviews запущен!"}

# Метод для предсказания тональности отзыва
@app.post("/predict")
def predict_sentiment(data: ReviewInput):
    if not model:
        return {"error": "Модель не загружена на сервере"}
        
    if not data.text.strip():
        return {"sentiment": "neutral", "message": "Текст пустой"}
    
    # Делаем предсказание с помощью вашей модели
    # Передаем текст в виде списка [text], так как модель обучалась на текстах
    prediction = model.predict([data.text])[0]
    
    # Пытаемся определить, что вернула модель (0/1 или текст)
    # Если ваша модель возвращает числа, переводим их в понятные слова
    if prediction == 1 or str(prediction).lower() in ["positive", "pos", "положительный"]:
        sentiment_result = "positive"
    elif prediction == 0 or str(prediction).lower() in ["negative", "neg", "отрицательный"]:
        sentiment_result = "negative"
    else:
        sentiment_result = str(prediction) # на случай, если там другой класс
        
    return {
        "text": data.text,
        "sentiment": sentiment_result
    }
