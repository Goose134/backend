import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Создаём Flask-приложение
app = Flask(__name__)
CORS(app)

# Определяем директорию для хранения данных
# Если DATA_DIR не указана, используется текущая папка
DATA_DIR = os.environ.get("DATA_DIR", ".")

# Создаём директорию, если её ещё нет
os.makedirs(DATA_DIR, exist_ok=True)

# Полный путь к файлу с данными
DATA_FILE = os.path.join(DATA_DIR, "data.txt")


# Обработчик сохранения данных
@app.post("/save")
def save_text():
    data = request.get_json()

    text = data.get("text", "")

    # Сохраняем полученный текст в файл
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        file.write(text)

    return jsonify({
        "message": "Данные успешно сохранены"
    })


# Обработчик получения данных
@app.get("/data")
def get_data():

    # Если файла нет, возвращаем пустую строку
    if not os.path.exists(DATA_FILE):
        return jsonify({"text": ""})

    # Читаем ранее сохранённые данные
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    return jsonify({
        "text": text
    })


# Запуск Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)