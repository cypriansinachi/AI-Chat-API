# from app.services.gemini import get_gemini_model
# from app.services.history import add_history

# def gemini_chat(user_id: int, message: str, history: list):
#     model = get_gemini_model()
#     chat_session = model.start_chat(history=history)
#     response = chat_session.send_message(message)
#     add_history(user_id, f"Chat: {message}")
#     return response.text


from sqlalchemy.orm import Session
from app.services.gemini import get_gemini_model
from app.services.history import add_history

def gemini_chat(db: Session, user_id: int, message: str, history: list):
    model = get_gemini_model()
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(message)
    add_history(db, user_id, f"Chat: {message}")
    return response.text