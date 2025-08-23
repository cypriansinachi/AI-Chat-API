# from fastapi import APIRouter, Depends, UploadFile, File
# from sqlalchemy.orm import Session
# from app.models.video import VideoRequest, VideoResponse
# from app.services.video import gemini_video
# from app.services.database import get_db
# from app.dependencies.auth import get_current_user_id

# router = APIRouter()

# @router.post("/", response_model=VideoResponse)
# async def video(file: UploadFile = File(...), request: VideoRequest = Depends(), user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
#     video_bytes = await file.read()
#     mime_type = file.content_type
#     analysis = gemini_video(user_id, video_bytes, mime_type, request.prompt)
#     return VideoResponse(analysis=analysis)


from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.models.video import VideoRequest, VideoResponse
from app.services.video import gemini_video
from app.services.database import get_db
from app.dependencies.auth import get_current_user_id

router = APIRouter()

@router.post("/", response_model=VideoResponse)
async def video(file: UploadFile = File(...), request: VideoRequest = Depends(), user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    video_bytes = await file.read()
    mime_type = file.content_type
    analysis = gemini_video(db, user_id, video_bytes, mime_type, request.prompt)
    return VideoResponse(analysis=analysis)