from fastapi.testclient import TestClient
from main import app

# Создаем тестового клиента для нашего FastAPI приложения
client = TestClient(app)

def test_read_root():
    """Проверка, что главная страница API отвечает успешно"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "working"

def test_predict_empty_text():
    """Проверка, как сервер обрабатывает пустой текст"""
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "neutral"

def test_predict_whitespace_text():
    """Проверка, как сервер обрабатывает текст, состоящий только из пробелов"""
    response = client.post("/predict", json={"text": "   "})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "neutral"
