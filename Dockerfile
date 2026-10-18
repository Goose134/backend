# Используем образ Python
FROM python:3.12-slim

# Рабочая директория контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY app.py .

# Порт Flask
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]