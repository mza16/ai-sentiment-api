# 📊 Sentiment Analysis API using FastAPI and Hugging Face Transformers

## 🚀 Overview

This project provides a RESTful API built with FastAPI to analyze the sentiment of a given text input. It uses Hugging Face’s pre-trained DistilBERT model for sentiment classification and runs completely locally — no API keys or internet access required once installed.

---

## ⚙️ Features

- Text-based sentiment analysis using `distilbert-base-uncased-finetuned-sst-2-english`
- Runs offline using Hugging Face's `transformers` and `torch`
- FastAPI-powered endpoint with auto-generated Swagger documentation
- Easy to test via Swagger UI or `curl`

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-sentiment-api.git
cd ai-sentiment-api
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚦 Running the API

```bash
uvicorn main:app --reload
```

Then open your browser and go to:

📍 `http://127.0.0.1:8000/docs` — this opens the Swagger UI

---

## 📤 Example Request (via Swagger)

**Endpoint:**
```
POST /sentiment
```

**Request body:**

```json
{
  "text": "I really love this project!"
}
```

**Response:**

```json
[
  {
    "label": "POSITIVE",
    "score": 0.9995
  }
]
```

---

## 📦 Project Structure

```
ai-sentiment-api/
├── main.py              # FastAPI app with sentiment analysis endpoint
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 👤 Contributors

- [Your Full Name]
- [Teammate’s Full Name]

---

## 📌 Version

- **v1.0**: Sentiment API using local transformer model — no secrets or tokens required.

---

## 📝 License

This project is for academic use under the terms of your institution’s course policies.
