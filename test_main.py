from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    """Проверка доступности сервера"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict_positive():
    """Проверка позитивного отзыва"""
    response = client.post("/predict", json={"text": "Отличная жвачка, очень свежая!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()

def test_predict_empty():
    """Проверка пустого ввода (сервер должен вернуть ошибку 400)"""
    response = client.post("/predict", json={"text": "   "})
    assert response.status_code == 400
