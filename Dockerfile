# Використовуємо базовий образ Python 3.11
FROM python:3.11-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо requirements.txt і встановлюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest
# Копіюємо весь код (включаючи конфігураційні файли) у контейнер
COPY . /app

 # Вказуємо, що порт 80 буде відкритий для використання
EXPOSE 80

# Запускаємо FastAPI додаток через Uvicorn
#CMD ["uvicorn", "notification_dispatcher:app", "--host", "0.0.0.0", "--port", "80"]

# Якщо ви хочете запускати тести, використовуйте цю команду (якщо потрібен запуск тестів)
CMD ["sh", "-c", "uvicorn notification_dispatcher:app --host 0.0.0.0 --port 80 & sleep 5 && tail -f /dev/null"]
