from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
import cv2
import os

app = FastAPI(title="Meat Spoilage Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "meat_freshness_model.h5")
model = tf.keras.models.load_model(MODEL_PATH)

classes = ["Fresh", "Half Spoiled", "Spoiled"]

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

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    contents = await image.read()
    img = preprocess_image(contents)

    prediction = model.predict(img)
    class_index = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    return {
        "prediction": classes[class_index],
        "confidence": round(confidence * 100, 2)
    }
