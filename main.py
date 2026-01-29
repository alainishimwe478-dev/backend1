from fastapi import FastAPI
from database import engine
from models import Base
from routes.users import router as users_router
from routes.payments import router as payments_router
from routes.admin import router as admin_router

app = FastAPI(title="RSSB HealthPay API")

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(payments_router)
app.include_router(admin_router)


@app.get("/")
def root():
    return {"status": "Admin backend running"}
