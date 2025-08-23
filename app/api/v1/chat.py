# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.models.chat import ChatRequest, ChatResponse
# from app.services.chat import gemini_chat
# from app.services.database import get_db
# from app.dependencies.auth import get_current_user_id  # Assume you have this for auth

# router = APIRouter()

# @router.post("/", response_model=ChatResponse)
# def chat(request: ChatRequest, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
#     reply = gemini_chat(user_id, request.message, request.history)
#     return ChatResponse(reply=reply)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.chat import ChatRequest, ChatResponse
from app.services.chat import gemini_chat
from app.services.database import get_db
from app.dependencies.auth import get_current_user_id

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    reply = gemini_chat(db, user_id, request.message, request.history)
    return ChatResponse(reply=reply)