from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from auth import hash_password, verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])


class SignupRequest(BaseModel):
    full_name: str
    email: str
    phone: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup")
def signup(request: SignupRequest, db: Session=Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    existing_phone = db.query(User).filter(User.phone == request.phone).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    hashed_password = hash_password(request.password)
    user = User(
        full_name=request.full_name,
        email=request.email,
        phone=request.phone,
        password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "user_id": user.id}


@router.post("/login")
def login(request: LoginRequest, db: Session=Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"id": user.id, "role": user.role})
    return {
        "token": token,
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role
        }
    }


@router.get("/")
def get_users(db: Session=Depends(get_db)):
    return db.query(User).all()
