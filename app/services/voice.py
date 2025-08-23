# import base64
# from google.generativeai.types import Blob
# from app.services.gemini import get_gemini_model
# from app.services.history import add_history
# from gtts import gTTS
# import os

# def gemini_voice(user_id: int, audio_bytes: bytes, mime_type: str, prompt: str, generate_tts: bool):
#     model = get_gemini_model()
#     # For small files (<20MB); for large, use genai.upload_file first
#     response = model.generate_content([prompt, {"inline_data": {"data": base64.b64encode(audio_bytes).decode("utf-8"), "mime_type": mime_type}}])
#     text = response.text
#     add_history(user_id, f"Voice processed: {prompt}")
    
#     audio_url = None
#     if generate_tts:
#         tts = gTTS(text)
#         audio_path = f"tts_{user_id}.mp3"
#         tts.save(audio_path)
#         audio_url = audio_path  # Serve via FastAPI static files
#     return text, audio_url


# import google.generativeai as genai
# from app.services.gemini import get_gemini_model
# from app.services.history import add_history
# from gtts import gTTS
# import os

# def gemini_voice(user_id: int, audio_bytes: bytes, mime_type: str, prompt: str, generate_tts: bool):
#     model = get_gemini_model()
#     # Upload file to Gemini
#     temp_file = f"temp_audio_{user_id}.wav"  # Adjust extension based on mime_type
#     with open(temp_file, "wb") as f:
#         f.write(audio_bytes)
#     uploaded_file = genai.upload_file(temp_file, mime_type=mime_type)
    
#     # Generate response
#     response = model.generate_content([prompt, uploaded_file])
#     text = response.text
#     add_history(user_id, f"Voice processed: {prompt}")
    
#     # Clean up temporary file
#     os.remove(temp_file)
    
#     audio_url = None
#     if generate_tts:
#         tts = gTTS(text)
#         audio_path = f"tts_{user_id}.mp3"
#         tts.save(audio_path)
#         audio_url = audio_path
#     return text, audio_url




import google.generativeai as genai
from sqlalchemy.orm import Session
from app.services.gemini import get_gemini_model
from app.services.history import add_history
from gtts import gTTS
import os

def gemini_voice(db: Session, user_id: int, audio_bytes: bytes, mime_type: str, prompt: str, generate_tts: bool):
    model = get_gemini_model()
    temp_file = f"temp_audio_{user_id}.wav"
    with open(temp_file, "wb") as f:
        f.write(audio_bytes)
    uploaded_file = genai.upload_file(temp_file, mime_type=mime_type)
    response = model.generate_content([prompt, uploaded_file])
    text = response.text
    add_history(db, user_id, f"Voice processed: {prompt}")
    os.remove(temp_file)
    
    audio_url = None
    if generate_tts:
        tts = gTTS(text)
        audio_path = f"tts_{user_id}.mp3"
        tts.save(audio_path)
        audio_url = audio_path
    return text, audio_url