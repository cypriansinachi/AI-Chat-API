import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-1.5-flash"  # Multimodal model (supports text, audio, video)

def get_gemini_model():
    return genai.GenerativeModel(MODEL_NAME)