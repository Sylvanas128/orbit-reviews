# 🍬 Orbit Reviews — Анализ тональности отзывов

Проект для автоматического определения тональности текстовых отзывов на любые товары и услуги с помощью машинного обучения. 

Система классифицирует входящий текст на положительный или отрицательный, помогая автоматизировать модерацию и анализировать обратную связь от клиентов.

## 🚀 Демонстрация работы проекта
* **🌍 Веб-интерфейс приложения:** [orbit-reviews.streamlit.app](https://streamlit.app)
* **📊 Блокнот обучения модели:** [![Open In Colab](https://colab.research.google.com/github/Sylvanas128/orbit-reviews/blob/main/orbit_model.ipynb#scrollTo=vAE7LgixctSO)]([https://google.com](https://colab.research.google.com/github/Sylvanas128/orbit-reviews/blob/main/orbit_model.ipynb#scrollTo=vAE7LgixctSO))

## 🛠 Стек технологий

* **ML / Data:** Python, Scikit-learn, TF-IDF, Logistic Regression, Joblib
* **Backend:** FastAPI, Pydantic, TestClient
* **Frontend:** Streamlit
* **Тестирование:** Pytest

## 🚀 Архитектурная особенность
Проект спроектирован по классической схеме разделения обязанностей (Separation of Concerns):
1. **Бэкенд (`main.py`)**: Реализован на FastAPI, отвечает за валидацию входных данных через Pydantic-схемы и запуск инференса модели машинного обучения.
2. **Фронтенд (`streamlit_app.py`)**: Реализован на Streamlit, предоставляет пользователю удобный интерфейс для ввода отзывов. 
3. **Интеграция в Production**: Для деплоя в облачную среду Streamlit Cloud бэкенд FastAPI интегрирован в процесс веб-интерфейса с помощью `fastapi.testclient.TestClient`. Это обеспечивает полную изоляцию и автономность бэкенд-логики без необходимости использования внешних открытых сетевых портов.

## 🛠 Локальный запуск проекта (для проверки)

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите веб-приложение:
```bash
streamlit run streamlit_app.py
```

3. Запуск автоматических тестов бэкенда:
```bash
pytest test_main.py -v
```
