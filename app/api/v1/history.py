from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.history import HistoryOut
from app.services.history import get_history
from app.services.database import get_db

router = APIRouter()

@router.get("/", response_model=list[HistoryOut])
async def view_history(user_id: int, db: Session = Depends(get_db)):
    history = get_history(db, user_id)
    return history