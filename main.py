from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
from routes.users import router as users_router
from routes.payments import router as payments_router
from routes.admin import router as admin_router
from routes.symptons import router as symptons_router

app = FastAPI(title="RSSB HealthPay API")

Base.metadata.create_all(bind=engine)

# Allow CORS from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(payments_router)
app.include_router(admin_router)
app.include_router(symptons_router)


@app.get("/")
def root():
    return {"status": "Admin backend running"}
