from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Symptons
from datetime import datetime
from typing import List

router = APIRouter(prefix="/symptons", tags=["Symptons"])


class SymptonsCreate(BaseModel):
    user_id: int
    symptoms: str
    activity_level: str
    note: str | None = None
    # `time` represents number of times (e.g., 3, 4, 5)
    time: int | None = None
    # also accept `times` to avoid confusion
    times: int | None = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_sympton(payload: SymptonsCreate, db: Session = Depends(get_db)):
    # DB currently expects `time` as timestamp; store timestamp for `time` and
    # keep numeric occurrence in `note` if provided (temporary workaround).
    sym = Symptons(
        user_id=payload.user_id,
        symptoms=payload.symptoms,
        activity_level=payload.activity_level,
        note=(f"occurrences={payload.times or payload.time}") if (payload.times or payload.time) else payload.note,
        time=datetime.utcnow(),
    )
    db.add(sym)
    db.commit()
    db.refresh(sym)
    return {"message": "Sympton recorded", "id": sym.id}


@router.get("/")
def list_symptons(db: Session = Depends(get_db)):
    return db.query(Symptons).all()


@router.get("/user/{user_id}")
def get_symptons_for_user(user_id: int, db: Session = Depends(get_db)):
    results = db.query(Symptons).filter(Symptons.user_id == user_id).all()
    return results


@router.get("/{sympton_id}")
def get_sympton(sympton_id: int, db: Session = Depends(get_db)):
    sym = db.query(Symptons).filter(Symptons.id == sympton_id).first()
    if not sym:
        raise HTTPException(status_code=404, detail="Sympton not found")
    return sym
