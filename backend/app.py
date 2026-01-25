from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# Load Model
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "meat_freshness_model.h5")

model = tf.keras.models.load_model(MODEL_PATH)

# -----------------------------
# CLASS LABELS (3 classes)
# IMPORTANT: Order must match training
# -----------------------------
classes = [
    "Fresh",
    "Half Spoiled",
    "Spoiled"
]

# -----------------------------
# Image Preprocessing
# -----------------------------
def preprocess_image(image_bytes):
    npimg = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Invalid image")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    return img

# -----------------------------
# Prediction API
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]

    try:
        img = preprocess_image(file.read())
        prediction = model.predict(img)

        class_index = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        return jsonify({
            "prediction": classes[class_index],
            "confidence": round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
