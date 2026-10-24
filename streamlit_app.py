import streamlit as st
import requests

st.title("🍬 Анализ отзывов Orbit")
st.write("Определение тональности отзыва с помощью ML-модели.")

# Полностью пустое поле ввода без какого-либо текста
review_text = st.text_area("Введите отзыв об Orbit:", value="")

if st.button("Проверить отзыв"):
    if not review_text.strip():
        st.warning("Пожалуйста, введите текст отзыва.")
    else:
        try:
            # Отправляем запрос на наш сервер FastAPI
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"text": review_text}
            )
            
            if response.status_code == 200:
                result = response.json()["sentiment"]
                if result == "Положительный":
                    st.success(f"Результат: {result} 👍")
                else:
                    st.error(f"Результат: {result} 👎")
            else:
                st.error("Ошибка при обработке запроса сервером.")
        except Exception:
            st.error("Сервер FastAPI не запущен. Запустите сначала бэкенд.")
