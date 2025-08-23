# from fastapi import APIRouter, Depends, UploadFile, File
# from sqlalchemy.orm import Session
# import speech_recognition as sr
# from app.services.database import get_db
# from app.services.history import add_history

# router = APIRouter()

# @router.post("/speech-to-text")
# async def speech_to_text(file: UploadFile = File(...), user_id: int = 1, db: Session = Depends(get_db)):
#     recognizer = sr.Recognizer()
#     audio_data = await file.read()
#     with open("temp.wav", "wb") as f:
#         f.write(audio_data)
#     with sr.AudioFile("temp.wav") as source:
#         audio = recognizer.record(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             add_history(db, user_id, f"Speech-to-text: {text}")
#             return {"text": text}
#         except sr.UnknownValueError:
#             return {"error": "Could not understand audio"}



# from fastapi import APIRouter, Depends, UploadFile, File
# from sqlalchemy.orm import Session
# from app.models.voice import VoiceRequest, VoiceResponse
# from app.services.voice import gemini_voice
# from app.services.database import get_db
# from app.dependencies.auth import get_current_user_id

# router = APIRouter()

# @router.post("/", response_model=VoiceResponse)
# async def voice(file: UploadFile = File(...), request: VoiceRequest = Depends(), user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
#     audio_bytes = await file.read()
#     mime_type = file.content_type
#     text, audio_url = gemini_voice(user_id, audio_bytes, mime_type, request.prompt, request.generate_tts)
#     return VoiceResponse(text=text, audio_url=audio_url)



from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.models.voice import VoiceRequest, VoiceResponse
from app.services.voice import gemini_voice
from app.services.database import get_db
from app.dependencies.auth import get_current_user_id

router = APIRouter()

@router.post("/", response_model=VoiceResponse)
async def voice(file: UploadFile = File(...), request: VoiceRequest = Depends(), user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    audio_bytes = await file.read()
    mime_type = file.content_type
    text, audio_url = gemini_voice(db, user_id, audio_bytes, mime_type, request.prompt, request.generate_tts)
    return VoiceResponse(text=text, audio_url=audio_url)