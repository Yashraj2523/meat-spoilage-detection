# 🥩 Meat Spoilage Detection using Deep Learning

An AI-powered web application to classify meat freshness into:
- Fresh
- Half Spoiled
- Spoiled

## 🧠 Tech Stack
- TensorFlow / Keras (CNN)
- FastAPI (Backend API)
- HTML, CSS, JavaScript (Frontend)

## ⚙️ How It Works
1. User uploads a meat image
2. Backend processes the image
3. CNN model predicts freshness
4. Result displayed with confidence and safety guidance

## 🚀 How to Run
### Backend
```bash
cd backend
uvicorn main:app --reload
