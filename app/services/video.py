# import google.generativeai as genai
# from sqlalchemy.orm import Session
# from app.services.gemini import get_gemini_model
# from app.services.history import add_history
# import os

# def gemini_video(db: Session, user_id: int, video_bytes: bytes, mime_type: str, prompt: str):
#     model = get_gemini_model()
#     temp_file = f"temp_video_{user_id}.mp4"
#     with open(temp_file, "wb") as f:
#         f.write(video_bytes)
#     uploaded_file = genai.upload_file(temp_file, mime_type=mime_type)
#     response = model.generate_content([prompt, uploaded_file])
#     text = response.text
#     add_history(db, user_id, f"Video analyzed: {prompt}")
#     os.remove(temp_file)
#     return text

import google.generativeai as genai
import tempfile
import os
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.gemini import get_gemini_model
from app.services.history import add_history
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def gemini_video(db: Session, user_id: int, video_bytes: bytes, mime_type: str, prompt: str):
    try:
        model = get_gemini_model()
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4', dir='/tmp') as temp_file:
            temp_file.write(video_bytes)
            temp_path = temp_file.name
        logger.info(f"Created temp file: {temp_path}")
        uploaded_file = genai.upload_file(temp_path, mime_type=mime_type)
        response = model.generate_content([prompt, uploaded_file])
        text = response.text
        add_history(db, user_id, f"Video analyzed: {prompt}")
        os.unlink(temp_path)
        return text
    except Exception as e:
        logger.error(f"Video processing error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Video processing error: {str(e)}")
    finally:
        if 'temp_path' in locals():
            try:
                os.unlink(temp_path)
            except Exception as e:
                logger.warning(f"Failed to delete temp file {temp_path}: {str(e)}")