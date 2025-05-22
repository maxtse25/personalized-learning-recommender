from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, init_db
from models import models

app = FastAPI()

# Initialize DB tables
init_db()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API is running"}
