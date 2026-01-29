from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Payment

router = APIRouter(prefix="/payments", tags=["Payments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def make_payment(user_id: int, amount: float, db: Session=Depends(get_db)):
    payment = Payment(
        user_id=user_id,
        amount=amount,
        status="paid"
    )
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment


@router.get("/")
def get_payments(db: Session=Depends(get_db)):
    return db.query(Payment).all()
