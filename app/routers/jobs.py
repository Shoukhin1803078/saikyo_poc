# app/routers/jobs.py
from fastapi import APIRouter, HTTPException
from app.schemas.job import  JobInput, SearchRequest,MultipleJobInputModel,MultipleJobResponseModel
from app.utils.chunking import chunking
from app.repositories.job_repo import ingest_raw_job, create_embedding_entry, search_jobs
from app.ai_service.intent_finding import classify_intent
from app.utils.extract_unique_job_urls import extract_job_urls_from_output

router = APIRouter()


# ---------------------------Single Job Ingestion---------------------------
# @router.post("/ingest-job")
# def ingest_job(job: JobInput):
#     chunks = chunking(job)
#     for i in range (0, len(chunks)):
#         print(f"chunk {i} ===== {chunks[i]}")

#     raw_job_id= ingest_raw_job(job)
#     print(f"row_job_id: {raw_job_id}")
#     create_embedding_entry(chunks,raw_job_id,job)
#     return {"status": "success", "id": raw_job_id}

#     # return {"status": "success"}


# ---------------------------Multiple Job Ingestion---------------------------
@router.post("/ingest-job", response_model=MultipleJobResponseModel)
def ingest_job(payload: MultipleJobInputModel):
    job_list=payload.jobs
    results = []

    for job in job_list:
        chunks = chunking(job)

        for i in range(0, len(chunks)):
            print(f"chunk {i} text ===== {chunks[i]['text']}")
            print(f"chunk {i} metadata ===== {chunks[i]['metadata']}")

        raw_job_id = ingest_raw_job(job)
        print(f"row_job_id: {raw_job_id}")



        create_embedding_entry(chunks, raw_job_id, job)
        results.append({"serial_no": job.serial_no,"raw_job_id": raw_job_id})


    return {
        "status": "success",
        "ingested_count": len(results),
        "jobs": results
    }



@router.post("/search")
def search(payload: SearchRequest):
    user_query=payload.query
    print(f"user_query======= {user_query}")
    intent_filter=classify_intent(user_query)
    print(f"intent_filter======= {intent_filter}") 
    output= search_jobs(user_query,intent_filter)
    job_urls = extract_job_urls_from_output(output)
    print(f"job_urls====={job_urls}")
    return {
        "results": output,
        "job_urls": job_urls
    }

    # return output