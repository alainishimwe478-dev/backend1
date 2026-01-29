from database import SessionLocal, engine
from models import Base, User
from auth import hash_password

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Check if admin already exists
existing_admin = db.query(User).filter(User.email == "admin@gmail.com").first()
if existing_admin:
    print("Admin user already exists")
else:
    hashed_password = hash_password("admin123")
    admin = User(
        full_name="Admin User",
        email="admin@gmail.com",
        phone="1234567890",
        password=hashed_password,
        role="admin"
    )
    db.add(admin)
    db.commit()
    print("Admin user created successfully")

db.close()
