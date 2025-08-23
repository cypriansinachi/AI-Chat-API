from pydantic import BaseModel
from datetime import datetime

class HistoryOut(BaseModel):
    action: str
    timestamp: datetime
    class Config:
        from_attributes = True