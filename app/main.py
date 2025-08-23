from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.history import router as history_router
from app.api.v1.chat import router as chat_router
from app.api.v1.translation import router as translation_router
from app.api.v1.voice import router as voice_router
from app.api.v1.video import router as video_router
from app.services.database import engine
from app.schemas import user, history

app = FastAPI(title="My FastAPI App")

# Create tables
user.Base.metadata.create_all(bind=engine)
history.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(history_router, prefix="/api/v1/history", tags=["history"])
app.include_router(chat_router, prefix="/api/v1/chat", tags=["chat"])
app.include_router(translation_router, prefix="/api/v1/translation", tags=["translation"])
app.include_router(voice_router, prefix="/api/v1/voice", tags=["voice"])
app.include_router(video_router, prefix="/api/v1/video", tags=["video"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}