from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Hospital, Claim
from auth import get_current_admin

router = APIRouter(prefix="/api/admin", tags=["Admin"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 ADMIN STATS
@router.get("/stats")
def admin_stats(current_admin: User=Depends(get_current_admin), db: Session=Depends(get_db)):
    return {
        "totalUsers": db.query(User).count(),
        "totalHospitals": db.query(Hospital).count(),
        "totalClaims": db.query(Claim).count(),
        "totalPayments": 45678,  # mock for now
        "totalPaidAmount": {
            "_sum": {
                "amount": 45678
            }
        }
    }


# 🔹 RECENT CLAIMS
@router.get("/recent-claims")
def recent_claims(db: Session=Depends(get_db)):
    claims = db.query(Claim).order_by(Claim.createdAt.desc()).limit(5).all()

    return [
        {
            "id": c.id,
            "amount": c.amount,
            "aiRisk": c.aiRisk,
            "createdAt": c.createdAt,
            "user": {
                "name": "User " + str(c.user_id)
            }
        }
        for c in claims
    ]


@router.get("/fraud-claims")
def fraud_claims(current_admin: User=Depends(get_current_admin), db: Session=Depends(get_db)):
    claims = (
        db.query(Claim)
        .filter(Claim.aiRisk == "HIGH")
        .order_by(Claim.createdAt.desc())
        .limit(5)
        .all()
    )

    return [
        {
            "id": c.id,
            "amount": c.amount,
            "createdAt": c.createdAt,
            "user": {
                "name": "User " + str(c.user_id)
            }
        }
        for c in claims
    ]
