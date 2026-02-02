# app/main.py
from fastapi import FastAPI
from app.core.database import engine
from app.models.jobs import Base
from sqlalchemy import text
from app.routers.jobs import router as jobs_router

app = FastAPI()

# @app.on_event("startup")
# def startup():
#     with engine.begin() as conn:
#         conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
#     Base.metadata.create_all(bind=engine)
# app.include_router(jobs_router)

# -------------------------------Gemini------------------------------------

# app/main.py
# app/main.py

@app.on_event("startup")
def startup():
    print("Application starting up... Configuring Database.")
    with engine.begin() as conn:
        # ১. vector এক্সটেনশন নিশ্চিত করা
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        
        # ২. SQLAlchemy মডেল অনুযায়ী টেবিল তৈরি করা
        Base.metadata.create_all(bind=engine)
        
        # ৩. HNSW Index তৈরি (Vector Similarity Search এর জন্য)
        # এটি ভেক্টর সার্চকে অনেক দ্রুত করবে।
        conn.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_job_embeddings_vector 
            ON job_embeddings USING hnsw (embedding vector_cosine_ops);
        """))
        
        # ৪. Full-Text Search Index তৈরি (Keyword Search এর জন্য)
        # 'japanese' এর বদলে 'simple' ব্যবহার করা হয়েছে কারণ ডিফল্ট ইমেজে জাপানিজ ডিকশনারি থাকে না।
        # 'simple' সব ভাষাতেই বেসিক কি-ওয়ার্ড ম্যাচিং করতে পারে।
        conn.execute(text("""
            CREATE INDEX IF NOT EXISTS idx_chunk_text_gin 
            ON job_embeddings USING gin (to_tsvector('simple', chunk_text));
        """))
    print("Database configuration completed successfully.")

app.include_router(jobs_router)

