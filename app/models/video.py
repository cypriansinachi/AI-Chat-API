from pydantic import BaseModel

class VideoRequest(BaseModel):
    prompt: str = "Summarize this video and answer questions about it"

class VideoResponse(BaseModel):
    analysis: str