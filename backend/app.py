# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import sqlite3

app = Flask(__name__)
CORS(app)

# Load trained model
with open("../ai_model/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Database connection
def get_db_connection():
    conn = sqlite3.connect("../dataset/materials.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/recommend", methods=["POST"])
def recommend_material():
    data = request.json
    features = [
        data["strength"], data["durability"], data["toughness"],
        data["hardness"], data["elasticity"], data["plasticity"],
        data["density"], data["thermal_conductivity"], data["porosity"],
        data["permeability"], data["fire_resistance"], data["weather_resistance"]
    ]
    prediction = model.predict([features])
    conn = get_db_connection()
    material = conn.execute("SELECT * FROM materials WHERE id = ?", (int(prediction[0]),)).fetchone()
    conn.close()
    return jsonify(dict(material))

if __name__ == "__main__":
    app.run(debug=True)
