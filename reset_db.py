from database import engine
from models import Base

def reset_db():
    # Drop all tables (handles dependent FKs) and recreate schema
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    reset_db()
    print('Database schema dropped and recreated')
