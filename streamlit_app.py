import streamlit as st
import requests

# Настройка страницы Streamlit
st.set_page_config(page_title="Orbit Reviews", page_icon="🍬")

st.title("🍬 Orbit Reviews — Анализ отзывов")
st.write("Связка Streamlit + FastAPI. Введите отзыв на жвачку Orbit, и модель определит его тональность.")

# Поле для ввода текста
user_input = st.text_area(
    "Ваш отзыв:", 
    placeholder="Например: Отличная жвачка, вкус держится очень долго, рекомендую!"
)

# Кнопка отправки
if st.button("Определить тональность"):
    if user_input.strip():
        with st.spinner("Запрос к FastAPI серверу..."):
            try:
                # Отправляем POST-запрос на локальный FastAPI (порт 8000)
                # Когда будете деплоить на Streamlit Cloud / HuggingFace, 
                # этот URL можно будет поменять на адрес вашего веб-сервера.
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
                        
                        # Красивый вывод результата
                        if sentiment == "positive":
                            st.success("🎉 **Положительный отзыв!** Модели Orbit понравился ваш отзыв.")
                        elif sentiment == "negative":
                            st.error("😡 **Отрицательный отзыв!** Модель считает, что отзыв содержит критику.")
                        else:
                            st.info(f"🤖 **Результат модели:** {sentiment}")
                else:
                    st.error(f"Ошибка сервера API. Статус-код: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Не удалось связаться с FastAPI сервером. Убедитесь, что бэкенд (main.py) запущен на порту 8000.")
    else:
        st.warning("Пожалуйста, введите хоть какой-нибудь текст отзыва.")
