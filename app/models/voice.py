from pydantic import BaseModel

class VoiceRequest(BaseModel):
    prompt: str = "Transcribe and summarize this audio"  # Optional prompt
    generate_tts: bool = False  # If true, return TTS audio of response

class VoiceResponse(BaseModel):
    text: str
    audio_url: str = None  # If TTS generated