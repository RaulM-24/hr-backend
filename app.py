from flask_cors import CORS
from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
CORS(app)  # 👈 ESTA LÍNEA ES CLAVE

DATA_FILE = os.path.join("data", "message.json")

# ---------- RUTA DE PRUEBA ----------
@app.route("/")
def home():
    return "Backend HR activo 🔥"

# ---------- OBTENER MENSAJE ----------
@app.route("/api/message", methods=["GET"])
def get_message():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = {
            "text": "💙",
            "updated_at": None
        }

    return jsonify(data)


# ---------- ACTUALIZAR MENSAJE ----------
@app.route("/api/message", methods=["POST"])
def update_message():
    new_text = request.json.get("text")

    data = {
        "text": new_text,
        "updated_at": "hoy"
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok"})

# ---------- ARRANQUE ----------
if __name__ == "__main__":
    app.run()


