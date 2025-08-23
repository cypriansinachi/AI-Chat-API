from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    target_lang: str = "en"

class TranslationResponse(BaseModel):
    translated_text: str