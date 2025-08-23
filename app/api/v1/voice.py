from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import speech_recognition as sr
from app.services.database import get_db
from app.services.history import add_history

router = APIRouter()

@router.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...), user_id: int = 1, db: Session = Depends(get_db)):
    recognizer = sr.Recognizer()
    audio_data = await file.read()
    with open("temp.wav", "wb") as f:
        f.write(audio_data)
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            add_history(db, user_id, f"Speech-to-text: {text}")
            return {"text": text}
        except sr.UnknownValueError:
            return {"error": "Could not understand audio"}