from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal, engine
from app import schemas, services, models
from app.cache import cache
from app.config import settings

# ... rest of your code
# Add this at the top of app/main.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from app import schemas, services, models, cache
from app.database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ... (rest of your existing endpoints)