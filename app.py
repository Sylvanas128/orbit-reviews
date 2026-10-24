# Настраиваем профиль Git в Colab
!git config --global user.email "ВАШ_EMAIL_ОТ_GITHUB"
!git config --global user.name "Sylvanas128"

# Добавляем файл app.py
!git add app.py
!git commit -m "Добавлен графический интерфейс Streamlit"

# Отправляем на GitHub (потребуется ввести токен GitHub вместо пароля, если настроен)
!git push origin main
