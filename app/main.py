# app/main.py
from fastapi import FastAPI
from app.core.database import engine
from app.models.jobs import Base
from sqlalchemy import text
from app.routers.jobs import router as jobs_router

app = FastAPI()

@app.on_event("startup")
def startup():
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    Base.metadata.create_all(bind=engine)

app.include_router(jobs_router)