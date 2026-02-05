from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")
    risk_score = Column(Float, default=0.0)


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="paid")
    created_at = Column(DateTime, default=datetime.utcnow)


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    aiRisk = Column(String)  # LOW / MEDIUM / HIGH
    createdAt = Column(DateTime, default=datetime.utcnow)


class Symptons(Base):
    __tablename__ = "symptons"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symptoms = Column(String, nullable=False)
    activity_level = Column(String)
    note = Column(String)
    # `time` stores a timestamp (when the symptom was recorded)
    time = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
