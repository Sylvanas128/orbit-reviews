import streamlit as st
from fastapi.testclient import TestClient
import main  # Импортируем ваш FastAPI бэкенд напрямую

# 🚀 ИНИЦИАЛИЗАЦИЯ ИМИТАЦИИ СЕРВЕРА
@st.cache_resource
def get_fastapi_client():
    return TestClient(main.app)

client = get_fastapi_client()

# 🍬 НАСТРОЙКА ИНТЕРФЕЙСА STREAMLIT
st.set_page_config(page_title="Orbit Reviews", page_icon="🍬")

st.title("🍬 Orbit Reviews — Анализ отзывов")
st.write("Проект реализован на базе связки Streamlit + FastAPI и модели машинного обучения (NLP).")
st.write("Введите отзыв на любой товар или услугу, и модель определит его тональность.")

user_input = st.text_area(
    "Ваш отзыв:", 
    placeholder="Например: Товар пришел быстро, качество отличное, всё работает!"
)

if st.button("Определить тональность"):
    if user_input.strip():
        with st.spinner("Бэкенд FastAPI обрабатывает запрос..."):
            try:
                response = client.post("/predict", json={"text": user_input})
                
                if response.status_code == 200:
                    result = response.json()
                    
                    if "error" in result:
                        st.error(f"Ошибка бэкенда: {result['error']}")
                    else:
                        sentiment = result["sentiment"]
                        
                        if sentiment == "positive":
                            st.success("🎉 **Положительный отзыв!** Модель считает, что клиент доволен.")
                        elif sentiment == "negative":
                            st.error("😡 **Отрицательный отзыв!** Модель обнаружила критику или недовольство.")
                        else:
                            st.info(f"🤖 **Результат модели:** {sentiment}")
                else:
                    st.error(f"Ошибка бэкенда FastAPI. Статус-код: {response.status_code}")
                    
            except Exception as e:
                st.error(f"❌ Произошла ошибка при обращении к API: {e}")
    else:
        st.warning("Пожалуйста, введите хоть какой-нибудь текст отзыва.")
