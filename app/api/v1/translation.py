# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.models.translation import TranslationRequest, TranslationResponse
# from app.services.translation import gemini_translate
# from app.services.database import get_db
# from app.dependencies.auth import get_current_user_id

# router = APIRouter()

# @router.post("/", response_model=TranslationResponse)
# def translate(request: TranslationRequest, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
#     translated = gemini_translate(user_id, request.text, request.target_lang)
#     return TranslationResponse(translated_text=translated)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.translation import TranslationRequest, TranslationResponse
from app.services.translation import gemini_translate
from app.services.database import get_db
from app.dependencies.auth import get_current_user_id

router = APIRouter()

@router.post("/", response_model=TranslationResponse)
async def translate(request: TranslationRequest, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    translated = gemini_translate(db, user_id, request.text, request.target_lang)
    return TranslationResponse(translated_text=translated)