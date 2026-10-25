# 🍬 Orbit Reviews — Анализ тональности отзывов

Проект для автоматического определения тональности текстовых отзывов на любые товары и услуги с помощью машинного обучения. 

Система классифицирует входящий текст на положительный или отрицательный, помогая автоматизировать модерацию и анализировать обратную связь от клиентов.

[![Open In Colab](https://google.com)](https://google.com)

👉 **[Открыть блокнот модели в Google Colab](https://google.com)**

## 🛠 Стек технологий

* **ML / Data:** Python, Scikit-learn, TF-IDF, Logistic Regression, Joblib
* **Backend:** FastAPI, Uvicorn, Pydantic
* **Frontend:** Streamlit
* **Тестирование:** Pytest

## 🚀 Локальный запуск проекта

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите бэкенд (FastAPI сервер):
```bash
uvicorn main:app --reload --port 8000
```

3. В другом терминале запустите фронтенд (Streamlit интерфейс):
```bash
streamlit run streamlit_app.py
```

4. Запуск автоматических тестов:
```bash
pytest test_main.py -v
```
