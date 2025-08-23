from sqlalchemy.orm import Session
from app.schemas.history import History

def add_history(db: Session, user_id: int, action: str):
    history = History(user_id=user_id, action=action)
    db.add(history)
    db.commit()
    db.refresh(history)
    return history

def get_history(db: Session, user_id: int):
    return db.query(History).filter(History.user_id == user_id).all()