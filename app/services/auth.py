# from sqlalchemy.orm import Session
# from app.schemas.user import User
# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain: str, hashed: str) -> bool:
#     return pwd_context.verify(plain, hashed)

# def create_user(db: Session, username: str, password: str):
#     hashed = hash_password(password)
#     user = User(username=username, password_hash=hashed)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# def get_user(db: Session, username: str):
#     return db.query(User).filter(User.username == username).first()


from sqlalchemy.orm import Session
from app.schemas.user import User
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_user(db: Session, username: str, password: str):
    hashed = hash_password(password)
    user = User(username=username, password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)  # Token expires in 30 minutes
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt