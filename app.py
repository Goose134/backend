from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.post("/save")
def save_text():
    data = request.get_json()

    text = data.get("text", "")

    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(text)

    return jsonify({
        "message": "Данные успешно сохранены"
    })

@app.get("/data")
def get_data():
    with open("data.txt", "r", encoding="utf-8") as file:
        text = file.read()

    return jsonify({
        "text": text
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)