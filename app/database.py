from sqlmodel import SQLModel, create_engine, Session
import os

DB_URL = os.getenv("DB_URL", "sqlite:///./app.db")
engine = create_engine(DB_URL, echo=False)

# Für FastAPI dependency injection

def get_session():
with Session(engine) as session:
yield session


def init_db():
# Tabellen anlegen, falls nicht vorhanden
SQLModel.metadata.create_all(engine)