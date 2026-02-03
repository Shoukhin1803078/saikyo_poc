# app/repositories/job_repo.py
from app.core.database import SessionLocal
from app.models.jobs import AllJob, JobEmbedding
from app.ai.embeddings import embeddings
from app.services.salary_splitting import salary_splitting

def ingest_raw_job(job):
    db = SessionLocal()
    salary=job.salary
    max_salary,min_salary=salary_splitting(salary)

    try:
        data = {
        "serial_no": job.serial_no,
        "media_site": job.media_site,
        "company_name": job.company_name,
        "company_logo": job.company_logo,
        "title": job.title,
        "catchphrase": job.catchphrase,
        "salary_type": job.salary_type,
        "salary": job.salary,
        "salary_max": max_salary,
        "salary_min": min_salary,
        "salary_details": job.salary_details,
        "employment_type": job.employment_type,
        "job_industry": job.job_industry,
        "job_category": job.job_category,
        "social_insurances": job.social_insurances,
        "job_benefits_details1": job.job_benefits_details1,
        "job_benefits_details2": job.job_benefits_details2,
        "holidays_leaves_details": job.holidays_leaves_details,
        "description": job.description,
        "requirements": job.requirements,
        "requirements_summary": job.requirements_summary,
        "service_form": job.service_form,
        "working_hours": job.working_hours,
        "one_day_work_details": job.one_day_work_details,
        "nearest_station": job.nearest_station,
        "nearest_station_access": job.nearest_station_access,
        "selection_flow": job.selection_flow,
        "recruiter_message": job.recruiter_message,
        "postal_code": job.postal_code,
        "address_details": job.address_details,
        "google_map_url": job.google_map_url,
        "trial_period_duration": job.trial_period_duration,
        "trial_period_details": job.trial_period_details,
        "trial_period_salary": job.trial_period_salary,
        "trial_period_working_hours": job.trial_period_working_hours,
        "tag": job.tag
        # "image_data": job.image_data
        }

        
        # raw_job = AllJob(
        #     serial_no=job.serial_no,
        #     media_site=job.media_site,
        #     company_name=job.company_name,
        #     company_logo=job.company_logo,
        #     title=job.title,
        #     catchphrase=job.catchphrase,
        #     salary_type=job.salary_type,
        #     salary=job.salary,
        #     salary_details=job.salary_details,
        #     employment_type=job.employment_type,
        #     job_industry=job.job_industry,
        #     job_category=job.job_category,
        #     social_insurances=job.social_insurances,
        #     benefits_1=job.job_benefits_details1,
        #     benefits_2=job.job_benefits_details2,
        #     holidays_leaves=job.holidays_leaves_details,
        #     description=job.description,
        #     requirements=job.requirements,
        #     requirements_summary=job.requirements_summary,
        #     service_form=job.service_form,
        #     working_hours=job.working_hours,
        #     one_day_work_details=job.one_day_work_details,
        #     nearest_station=job.nearest_station,
        #     nearest_station_access=job.nearest_station_access,
        #     selection_flow=job.selection_flow,
        #     recruiter_message=job.recruiter_message,
        #     postal_code=job.postal_code,
        #     address_details=job.address_details,
        #     google_map_url=job.google_map_url,
        #     trial_period_duration=job.trial_period_duration,
        #     trial_period_details=job.trial_period_details,
        #     trial_period_salary=job.trial_period_salary,
        #     trial_period_working_hours=job.trial_period_working_hours,
        #     tag=job.tag
        # )

        raw_job = AllJob(**data) 
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

# ---------------------------------------Previous------------------------------------


# def create_embedding_entry(chunks,raw_job_id, job):
#     db = SessionLocal()

#     for i in range(0, len(chunks)):
#         print(f"chunk {i} ===== {chunks[i]}")

#     try:
#         for chunk in chunks:
#             text=chunk["text"]
#             metadata=chunk["metadata"]
#             vector = embeddings.embed_query(text)
#             vector_entry = JobEmbedding(
#                 job_id=raw_job_id,         # use raw_job_id directly
#                 serial_no=job.serial_no,
#                 company_name=job.company_name,
#                 embedding=vector,
#                 chunk_metadata=metadata
#             )
#             db.add(vector_entry)
#         db.commit()

#     except Exception as e:
#         db.rollback()
#         db.close()
#         raise e

#     db.close()







# def search_jobs(query):
#     db = SessionLocal()
#     try:
#         q_vector = embeddings.embed_query(query)
#         results = (
#             db.query(
#                 JobEmbedding,
#                 JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
#             )
#             .order_by("distance")
#             .limit(3)
#             .all()
#         )
#         return [
#             {
#                 "id": job.id, 
#                 "serial_no": job.serial_no,
#                 "company_name": job.company_name, 
#                 "score": round(1 - distance, 4)
#             } for job, distance in results
#         ]
#     finally:
#         db.close()




# ---------------------------------------Gemini------------------------------------



def create_embedding_entry(chunks, raw_job_id, job):
    db = SessionLocal()
    try:
        for chunk in chunks:
            text = chunk["text"]
            metadata = chunk["metadata"]
            
            # এম্বেডিং জেনারেট করা
            vector = embeddings.embed_query(text)
            
            # নতুন মডেল অনুযায়ী ডেটা এন্ট্রি
            vector_entry = JobEmbedding(
                job_id=raw_job_id,         
                serial_no=job.serial_no,
                company_name=job.company_name,
                chunk_text=text,           # অবশ্যই এটি সেভ করতে হবে
                embedding=vector,
                chunk_metadata=metadata    # এখানে 'group' ইনফো থাকছে
            )
            db.add(vector_entry)
        
        db.commit()
        print(f"Successfully ingested {len(chunks)} chunks for Serial No: {job.serial_no}")

    except Exception as e:
        db.rollback()
        print(f"Error during ingestion: {e}")
        raise e
    finally:
        db.close()






# def search_jobs(query):
#     db = SessionLocal()
#     try:
        
#         q_vector = embeddings.embed_query(query)
        
#         # search logic
#         results = (
#             db.query(
#                 JobEmbedding,
#                 JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
#             )
#             # .filter(JobEmbedding.embedding.cosine_distance(q_vector) < 0.5) # থ্রেশহোল্ড একটু বাড়ানো হয়েছে
#             .order_by("distance")
#             .limit(5)
#             .all()
#         )
        
#         # result processing
#         formatted_results = []
#         for job_chunk, distance in results:
#             score = round(1 - distance, 4)
            
#             # আপনার মডেল অনুযায়ী কলামের নামগুলো নিশ্চিত করুন:
#             # text -> chunk_text
#             # metadata -> chunk_metadata
#             formatted_results.append({
#                 "chunk_id": job_chunk.id,
#                 "serial_no": job_chunk.serial_no,
#                 "company_name": job_chunk.company_name,
#                 "text": job_chunk.chunk_text, 
#                 "group": job_chunk.chunk_metadata.get("group") if job_chunk.chunk_metadata else "N/A",
#                 "score": score
#             })
            
#         # ৪. স্কোর অনুযায়ী Ascending (ছোট থেকে বড়) অর্ডারে সাজানো
#         # key=lambda x: x['score'] মানে স্কোরের মানের ওপর ভিত্তি করে সর্টিং হবে
#         final_results = sorted(formatted_results, key=lambda x: x['score'])
            
#         return final_results


#     except Exception as e:
#         # ডিবাগিংয়ের জন্য পুরো এররটি প্রিন্ট করা ভালো
#         print(f"Search error details: {str(e)}")
#         return {"error": str(e)}
#     finally:
#         db.close()








# -----------------------------------Openai------------------------------------
def search_jobs(query):
    """
    Vector-based semantic job search using pgvector.
    Returns top relevant job chunks with score.
    Fixed parameters:
        top_k = 5
        distance_threshold = 0.7
    """

    top_k = 5
    distance_threshold = 0.7

    db = SessionLocal()
    try:
        # ---------------------------
        # Step 1: Embed user query
        # ---------------------------
        q_vector = embeddings.embed_query(query)

        # ---------------------------
        # Step 2: Vector search with threshold
        # ---------------------------
        results = (
            db.query(
                JobEmbedding,
                JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
            )
            .filter(JobEmbedding.embedding.cosine_distance(q_vector) < distance_threshold)
            .order_by("distance")   # smaller distance = better
            .limit(top_k * 3)       # extra for de-duplication
            .all()
        )

        # ---------------------------
        # Step 3: Format results & avoid duplicate jobs
        # ---------------------------
        seen_jobs = set()
        formatted_results = []

        for job_chunk, distance in results:
            if job_chunk.serial_no in seen_jobs:
                continue
            seen_jobs.add(job_chunk.serial_no)

            score = round(1 - distance, 4)

            formatted_results.append({
                "chunk_id": job_chunk.id,
                "serial_no": job_chunk.serial_no,
                "company_name": job_chunk.company_name,
                "group": job_chunk.chunk_metadata.get("group") if job_chunk.chunk_metadata else "N/A",
                "text": job_chunk.chunk_text,
                "score": score
            })

            if len(formatted_results) >= top_k:
                break

        # ---------------------------
        # Step 4: Sort by score descending
        # ---------------------------
        final_results = sorted(
            formatted_results,
            key=lambda x: x["score"],
            reverse=True
        )

        return final_results

    except Exception as e:
        print(f"Search error details: {str(e)}")
        return {"error": str(e)}

    finally:
        db.close()

