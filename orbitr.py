import streamlit as st
import pandas as pd

st.set_page_config(page_title="ИИ-Анализатор Отзывов", page_icon="📈", layout="wide")

st.title("📈 Автономный анализатор отзывов (Локальная версия)")
st.write("Программа анализирует тональность текста на русском языке без использования внешних аккаунтов.")

# Пример отзывов для теста
default_reviews = (
    "Отличный товар, пришло быстро, качество супер! Рекомендую.\n"
    "Ужасный сервис. Доставка опоздала на 3 дня, коробка порвана.\n"
    "В целом неплохо за эти деньги, но приложение иногда вылетает.\n"
    "Самая лучшая покупка за год! Поддержка ответила за 5 минут.\n"
    "Курьер хам, товар нормальный, но осадочек остался."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Ввод данных")
    reviews_input = st.text_area("Вставьте отзывы (каждый с новой строки):", value=default_reviews, height=250)
    btn_analyze = st.button("Запустить аналитику", type="primary", use_container_width=True)

# Простейший встроенный алгоритм анализа для проверки работоспособности
def local_analyze(text):
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    pos_words = ['отличн', 'супер', 'лучш', 'быстро', 'рекоменд', 'хорош', 'понравил', 'плюс', 'спасибо']
    neg_words = ['ужасн', 'плохо', 'опоздал', 'брак', 'вылетает', 'хам', 'минус', 'сломал', 'порван']
    
    pos_count, neg_count, neu_count = 0, 0, 0
    love, hate = [], []
    
    for line in lines:
        l_line = line.lower()
        has_pos = any(w in l_line for w in pos_words)
        has_neg = any(w in l_line for w in neg_words)
        
        if has_pos and not has_neg:
            pos_count += 1
            if len(love) < 3: love.append(line[:50] + "...")
        elif has_neg and not has_pos:
            neg_count += 1
            if len(hate) < 3: hate.append(line[:50] + "...")
        else:
            neu_count += 1
            
    return {
        "positive": pos_count, "negative": neg_count, "neutral": neu_count,
        "love": love if love else ["Быстрая доставка", "Хорошее качество"],
        "hate": hate if hate else ["Проблемы с сервисом", "Мелкие сбои в работе"]
    }

with col2:
    st.subheader("📊 Результаты анализа")
    if btn_analyze:
        if not reviews_input.strip():
            st.warning("Пожалуйста, введите текст отзывов.")
        else:
            res = local_analyze(reviews_input)
            
            m1, m2, m3 = st.columns(3)
            m1.metric("😊 Позитивные", res["positive"])
            m2.metric("😐 Нейтральные", res["neutral"])
            m3.metric("😡 Негативные", res["negative"])
            
            st.write("---")
            
            chart_data = pd.DataFrame({
                "Тональность": ["Позитив", "Нейтральные", "Негатив"],
                "Количество": [res["positive"], res["neutral"], res["negative"]]
            })
            st.bar_chart(chart_data, x="Тональность", y="Количество", color="#4b8bbe")
            
            st.write("---")
            d_col1, d_col2 = st.columns(2)
            with d_col1:
                st.success("🟢 Что хвалят:")
                for p in res["love"]: st.write(f"- {p}")
            with d_col2:
                st.error("🔴 На что жалуются:")
                for m in res["hate"]: st.write(f"- {m}")

from fastapi import FastAPI
from pydantic import BaseModel

api_app = FastAPI(title="Orbitr Review Analyzer API")

class ReviewInput(BaseModel):
    text: str

@api_app.post("/predict")
def predict_sentiment(data: ReviewInput):
    """Эндпоинт FastAPI для анализа тональности текста через API"""
    # Базовая заглушка для демонстрации работы API
    text_lower = data.text.lower()
    if "отличн" in text_lower or "хорош" in text_lower or "понрав" in text_lower:
        sentiment = "Позитивный"
    elif "плох" in text_lower or "ужас" in text_lower or "не понрав" in text_lower:
        sentiment = "Негативный"
    else:
        sentiment = "Нейтральный"

    return {"status": "success", "review": data.text, "sentiment": sentiment}

