# from app.services.gemini import get_gemini_model
# from app.services.history import add_history

# def gemini_translate(user_id: int, text: str, target_lang: str):
#     model = get_gemini_model()
#     prompt = f"Translate the following text to {target_lang}: {text}"
#     response = model.generate_content(prompt)
#     add_history(user_id, f"Translated text to {target_lang}")
#     return response.text

from sqlalchemy.orm import Session
from app.services.gemini import get_gemini_model
from app.services.history import add_history

def gemini_translate(db: Session, user_id: int, text: str, target_lang: str):
    model = get_gemini_model()
    prompt = f"Translate the following text to {target_lang}: {text}"
    response = model.generate_content(prompt)
    add_history(db, user_id, f"Translated text to {target_lang}")
    return response.text