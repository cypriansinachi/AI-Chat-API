# import google.generativeai as genai
# from sqlalchemy.orm import Session
# from app.services.gemini import get_gemini_model
# from app.services.history import add_history
# from gtts import gTTS
# import os

# def gemini_voice(db: Session, user_id: int, audio_bytes: bytes, mime_type: str, prompt: str, generate_tts: bool):
#     model = get_gemini_model()
#     temp_file = f"temp_audio_{user_id}.wav"
#     with open(temp_file, "wb") as f:
#         f.write(audio_bytes)
#     uploaded_file = genai.upload_file(temp_file, mime_type=mime_type)
#     response = model.generate_content([prompt, uploaded_file])
#     text = response.text
#     add_history(db, user_id, f"Voice processed: {prompt}")
#     os.remove(temp_file)
    
#     audio_url = None
#     if generate_tts:
#         tts = gTTS(text)
#         audio_path = f"tts_{user_id}.mp3"
#         tts.save(audio_path)
#         audio_url = audio_path
#     return text, audio_url


import google.generativeai as genai
import tempfile
import os
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.gemini import get_gemini_model
from app.services.history import add_history
from gtts import gTTS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def gemini_voice(db: Session, user_id: int, audio_bytes: bytes, mime_type: str, prompt: str, generate_tts: bool):
    try:
        model = get_gemini_model()
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav', dir='/tmp') as temp_file:
            temp_file.write(audio_bytes)
            temp_path = temp_file.name
        logger.info(f"Created temp file: {temp_path}")
        uploaded_file = genai.upload_file(temp_path, mime_type=mime_type)
        response = model.generate_content([prompt, uploaded_file])
        text = response.text
        add_history(db, user_id, f"Voice processed: {prompt}")
        os.unlink(temp_path)
        
        audio_url = None
        if generate_tts:
            tts = gTTS(text)
            audio_path = f"/tmp/tts_{user_id}.mp3"
            tts.save(audio_path)
            audio_url = f"/static/tts_{user_id}.mp3"
            logger.info(f"Generated TTS file: {audio_path}")
        return text, audio_url
    except Exception as e:
        logger.error(f"Voice processing error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Voice processing error: {str(e)}")
    finally:
        if 'temp_path' in locals():
            try:
                os.unlink(temp_path)
            except Exception as e:
                logger.warning(f"Failed to delete temp file {temp_path}: {str(e)}")