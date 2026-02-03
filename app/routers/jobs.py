# app/routers/jobs.py
from fastapi import APIRouter, HTTPException
from app.schemas.job import JobInput, SearchRequest
from app.services.chunking import chunking
from app.repositories.job_repo import ingest_raw_job, create_embedding_entry, search_jobs

router = APIRouter()

@router.post("/ingest-job")
def ingest_job(job: JobInput):
    chunks = chunking(job)

    for i in range (0, len(chunks)):
        print(f"chunk {i} ===== {chunks[i]}")
    raw_job_id= ingest_raw_job(job)
    print(f"row_job_id: {raw_job_id}")
    create_embedding_entry(chunks,raw_job_id,job)
    return {"status": "success", "id": raw_job_id}
    # return {"status": "success"}


@router.post("/search")
def search(payload: SearchRequest):
    user_query=payload.query
    return search_jobs(user_query)