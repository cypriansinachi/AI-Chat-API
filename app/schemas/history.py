from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .user import Base

class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    action = Column(String)
    timestamp = Column(DateTime, server_default=func.now())