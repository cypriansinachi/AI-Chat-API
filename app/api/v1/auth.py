# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.models.user import UserCreate, UserOut
# from app.services.auth import create_user, get_user, verify_password, create_access_token
# from app.services.database import get_db

# router = APIRouter()

# @router.post("/register", response_model=UserOut)
# async def register(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user(db, user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already exists")
#     new_user = create_user(db, user.username, user.password)
#     return new_user

# @router.post("/login")
# async def login(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user(db, user.username)
#     if not db_user or not verify_password(user.password, db_user.password_hash):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     access_token = create_access_token(data={"sub": db_user.username})
#     return {"access_token": access_token, "token_type": "bearer", "user_id": db_user.id}


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.user import UserCreate, UserOut
from app.services.auth import create_user, get_user, verify_password, create_access_token
from app.services.database import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = create_user(db, user.username, user.password)
    return new_user

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = get_user(db, form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer", "user_id": db_user.id}