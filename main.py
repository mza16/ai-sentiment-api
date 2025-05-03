from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load the pre-trained sentiment analysis model from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

# Initialize FastAPI app
app = FastAPI()

# Define the request body structure
class TextInput(BaseModel):
    text: str

# Sentiment analysis endpoint
@app.post("/sentiment")
def analyze_sentiment(input: TextInput):
    result = sentiment_pipeline(input.text)
    return result
