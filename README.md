# 🍬 Orbit Reviews — Анализ отзывов

Проект для автоматического определения тональности отзывов на жевательную резинку Orbit с помощью машинного обучения.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Sylvanas128/orbit-reviews/blob/main/orbit_model.ipynb)

👉 **[Открыть блокнот модели в Google Colab](https://colab.research.google.com/github/Sylvanas128/orbit-reviews/blob/main/orbit_model.ipynb)**

---

## 🛠 Стек технологий
- **ML / Data:** Python, Scikit-learn, TF-IDF, Logistic Regression, Joblib
- **Backend:** FastAPI, Uvicorn, Pydantic
- **Frontend:** Streamlit
- **Тестирование:** Pytest

---

## 🚀 Запуск проекта

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
streamlit run streamlit_app.py
pytest test_main.py -v

