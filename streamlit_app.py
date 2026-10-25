import streamlit as st
import requests
import subprocess
import time

# 🚀 АВТОЗАПУСК FASTAPI В ФОНЕ (для работы на сервере Streamlit Cloud)
@st.cache_resource
def start_fastapi():
    # Запускаем uvicorn на локальном порту 8000 внутри контейнера Streamlit
    process = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Даем серверу 3 секунды, чтобы проснуться и загрузить модель model.pkl
    time.sleep(3)
    return process

# Запускаем бэкенд
start_fastapi()

# 🍬 НАСТРОЙКА ИНТЕРФЕЙСА STREAMLIT
st.set_page_config(page_title="Orbit Reviews", page_icon="🍬")

st.title("🍬 Orbit Reviews — Анализ отзывов")
st.write("Полноценная связка Streamlit + FastAPI. Введите отзыв на жвачку Orbit, и модель определит его тональность.")

user_input = st.text_area(
    "Ваш отзыв:", 
    placeholder="Например: Отличная жвачка, вкус держится очень долго, рекомендую!"
)

if st.button("Определить тональность"):
    if user_input.strip():
        with st.spinner("Запрос к фоновому FastAPI серверу..."):
            try:
                # Так как они запущены в одном контейнере, запрос идет на 127.0.0.1:8000
                response = requests.post(
                    "http://127.0.0", 
                    json={"text": user_input}
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    if "error" in result:
                        st.error(f"Ошибка бэкенда: {result['error']}")
                    else:
                        sentiment = result["sentiment"]
                        
                        if sentiment == "positive":
                            st.success("🎉 **Положительный отзыв!** Модели Orbit понравился ваш отзыв.")
                        elif sentiment == "negative":
                            st.error("😡 **Отрицательный отзыв!** Модель считает, что отзыв содержит критику.")
                        else:
                            st.info(f"🤖 **Результат модели:** {sentiment}")
                else:
                    st.error(f"Ошибка сервера API. Статус-код: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Не удалось связаться с внутренним FastAPI. Попробуйте обновить страницу.")
    else:
        st.warning("Пожалуйста, введите хоть какой-нибудь текст отзыва.")
