# 🥩 Meat Spoilage Detection System using Deep Learning

## 📌 Overview

This project presents an end-to-end **Meat Spoilage Detection System** using **Deep Learning and Computer Vision**. The system classifies meat images into different freshness categories by analyzing visual features such as color, texture, and surface patterns.

It integrates:

* 🧠 CNN-based image classification model
* ⚙️ FastAPI backend for prediction
* 🌐 Interactive frontend for user interaction
* 🔍 Grad-CAM visualization for model explainability

---

## 🚀 Features

* ✅ Detects meat freshness (e.g., Fresh / Spoiled / Intermediate)
* ✅ Upload image and view prediction instantly
* ✅ Grad-CAM heatmaps for interpretability
* ✅ Improved UI with result visualization
* ✅ Handles invalid inputs (non-meat images detection logic)
* ✅ Modular structure (frontend + backend + model)

---

## 🏗️ Project Structure

```
Meat-Spoilage-Detection/
│
├── backend/              # FastAPI backend
│   ├── app.py
│   ├── main.py
│
├── frontend/             # HTML, CSS, JS UI
│
├── model/                # Model training and related code
│   ├── training.ipynb
│   ├── README.md
│
├── .gitignore
├── README.md
```

---

## 🧠 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Input Size: 224x224 images
* Classes: Fresh, Spoiled, Intermediate
* Training Platform: Google Colab
* Framework: TensorFlow / Keras

---

## 📊 Training Pipeline

The training process includes:

* Data preprocessing and augmentation
* CNN model building
* Model training and validation
* Performance evaluation

The full training code is available in:

```
model/training.ipynb
```

---

## ⚙️ Backend (FastAPI)

The backend is built using **FastAPI** and handles:

* Image input from frontend
* Model inference
* Returning prediction results
* Integration with Grad-CAM

Run backend:

```bash
uvicorn main:app --reload
```

---

## 🌐 Frontend

* Built using HTML, CSS, JavaScript
* Allows image upload and displays results
* Shows prediction and Grad-CAM outputs

---

## 🔍 Grad-CAM Visualization

Grad-CAM is used to highlight important regions in the image that influenced the model’s prediction, improving transparency and trust in the system.

---

## ⚠️ Limitations

* Model may predict incorrectly for non-meat images
* Performance depends on dataset quality
* Requires further validation for real-world deployment

---

## 🔮 Future Enhancements

* 🔹 Improve non-meat image detection
* 🔹 Integrate transfer learning models (ResNet, MobileNet)
* 🔹 Add real-time camera detection
* 🔹 Deploy on cloud (AWS / Azure)
* 🔹 Add mobile app support

---

## 🧑‍💻 Author

**Yashwanth R**
M.Tech Software Engineering
Vellore Institute of Technology

---

## 📌 Conclusion

This project demonstrates the application of deep learning in food quality assessment. It provides a scalable and automated approach for detecting meat spoilage, reducing manual inspection effort and improving food safety.

---
