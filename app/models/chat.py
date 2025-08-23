from pydantic import BaseModel
from typing import List, Dict

class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []  # [{"role": "user", "content": "hi"}, ...]

class ChatResponse(BaseModel):
    reply: str