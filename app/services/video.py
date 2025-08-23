# import base64
# from google.generativeai.types import Blob
# from app.services.gemini import get_gemini_model
# from app.services.history import add_history

# def gemini_video(user_id: int, video_bytes: bytes, mime_type: str, prompt: str):
#     model = get_gemini_model()
#     # For small files; for large (>20MB or long), use genai.upload_file
#     response = model.generate_content([prompt, {"inline_data": {"data": base64.b64encode(video_bytes).decode("utf-8"), "mime_type": mime_type}}])
#     add_history(user_id, f"Video analyzed: {prompt}")
#     return response.text



# import google.generativeai as genai
# from app.services.gemini import get_gemini_model
# from app.services.history import add_history
# import os

# def gemini_video(user_id: int, video_bytes: bytes, mime_type: str, prompt: str):
#     model = get_gemini_model()
#     # Upload file to Gemini
#     temp_file = f"temp_video_{user_id}.mp4"  # Adjust extension based on mime_type
#     with open(temp_file, "wb") as f:
#         f.write(video_bytes)
#     uploaded_file = genai.upload_file(temp_file, mime_type=mime_type)
    
#     # Generate response
#     response = model.generate_content([prompt, uploaded_file])
#     text = response.text
#     add_history(user_id, f"Video analyzed: {prompt}")
    
#     # Clean up temporary file
#     os.remove(temp_file)
#     return text


import google.generativeai as genai
from sqlalchemy.orm import Session
from app.services.gemini import get_gemini_model
from app.services.history import add_history
import os

def gemini_video(db: Session, user_id: int, video_bytes: bytes, mime_type: str, prompt: str):
    model = get_gemini_model()
    temp_file = f"temp_video_{user_id}.mp4"
    with open(temp_file, "wb") as f:
        f.write(video_bytes)
    uploaded_file = genai.upload_file(temp_file, mime_type=mime_type)
    response = model.generate_content([prompt, uploaded_file])
    text = response.text
    add_history(db, user_id, f"Video analyzed: {prompt}")
    os.remove(temp_file)
    return text