from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")
print("SQLAlchemy is working ✅")
