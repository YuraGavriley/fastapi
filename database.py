from sqlmodel import SQLModel, create_engine, Session
from .config import DATABASE_URL
from .models import User

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
