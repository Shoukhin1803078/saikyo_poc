# app/repositories/job_repo.py
from app.core.database import SessionLocal
from app.models.jobs import AllJob, JobEmbedding
from app.ai.embeddings import embeddings

def ingest_raw_job(job):
    db = SessionLocal()
    try:
        raw_job = AllJob(
            serial_no=job.serial_no,
            media_site=job.Media_site,
            company_name=job.Company_name,
            company_logo=job.Company_logo,
            title=job.Title,
            catchphrase=job.Catchphrase,
            salary_type=job.Salary_type,
            salary=str(job.Salary) if job.Salary is not None else None,
            salary_details=job.Salary_details,
            employment_type=job.Employment_Type,
            job_industry=job.Job_Industry,
            job_category=job.Job_Category,
            social_insurances=job.Social_insurances,
            benefits_1=job.Job_Benefits_Details1,
            benefits_2=job.Job_Benefits_Details2,
            holidays_leaves=job.Holidays_Leaves_Details,
            description=job.Description,
            requirements=job.Requirements,
            requirements_summary=job.Requirements_summary,
            service_form=job.Service_Form,
            working_hours=job.Working_hours,
            one_day_work_details=job.One_day_work_details,
            nearest_station=job.Nearest_Station,
            nearest_station_access=job.Nearest_station_access,
            selection_flow=job.Selection_flow,
            recruiter_message=job.Recruiter_message,
            postal_code=job.Postal_Code,
            address_details=job.Address_details,
            google_map_url=job.Google_Map_Url,
            trial_period_duration=job.Trial_period_duration,
            trial_period_details=job.Trial_period_details,
            tag=job.Tag
        )
        db.add(raw_job)
        # db.flush() 
        db.commit()
        db.refresh(raw_job) 
        row_job_id=raw_job.id
        return row_job_id
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()




def create_embedding_entry(chunks,raw_job_id, job):
    db = SessionLocal()

    for i in range(0, len(chunks)):
        print(f"chunk {i} ===== {chunks[i]}")

    try:
        for chunk in chunks:
            text=chunk["text"]
            metadata=chunk["metadata"]
            vector = embeddings.embed_query(text)
            vector_entry = JobEmbedding(
                job_id=raw_job_id,         # use raw_job_id directly
                serial_no=job.serial_no,
                company_name=job.Company_name,
                embedding=vector,
                chunk_metadata=metadata
            )
            db.add(vector_entry)
        db.commit()

    except Exception as e:
        db.rollback()
        db.close()
        raise e

    db.close()







def search_jobs(query):
    db = SessionLocal()
    try:
        q_vector = embeddings.embed_query(query)
        results = (
            db.query(
                JobEmbedding,
                JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
            )
            .order_by("distance")
            .limit(3)
            .all()
        )
        return [
            {
                "id": job.id, 
                "serial_no": job.serial_no,
                "company_name": job.company_name, 
                "score": round(1 - distance, 4)
            } for job, distance in results
        ]
    finally:
        db.close()