# app/repositories/job_repo.py
from app.core.database import SessionLocal
from app.models.jobs import AllJob, JobEmbedding
from app.ai_service.embeddings import embeddings
from app.utils.salary_splitting import salary_splitting

def ingest_raw_job(job):
    db = SessionLocal()
    salary=job.salary
    min_salary,max_salary=salary_splitting(salary)

    try:

        # -----------------way-1----------------------
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



# def create_embedding_entry(chunks, raw_job_id, job):
#     db = SessionLocal()
#     try:
#         for chunk in chunks:
#             text = chunk["text"]
#             metadata = chunk["metadata"]
#             vector = embeddings.embed_query(text)
#             vector_entry = JobEmbedding(
#                 job_id=raw_job_id,         
#                 serial_no=job.serial_no,
#                 company_name=job.company_name,
#                 chunk_text=text,        
#                 embedding=vector,
#                 chunk_metadata=metadata   
#             )
#             db.add(vector_entry)
        
#         db.commit()
#         print(f"Successfully ingested {len(chunks)} chunks for Serial No: {job.serial_no}")

#     except Exception as e:
#         db.rollback()
#         print(f"Error during ingestion: {e}")
#         raise e
#     finally:
#         db.close()






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
# def search_jobs(query):
#     """
#     Vector-based semantic job search using pgvector.
#     Returns top relevant job chunks with score.
#     Fixed parameters:
#         top_k = 5
#         distance_threshold = 0.7
#     """

#     top_k = 5
#     distance_threshold = 0.7

#     db = SessionLocal()
#     try:
#         # ---------------------------
#         # Step 1: Embed user query
#         # ---------------------------
#         q_vector = embeddings.embed_query(query)

#         # ---------------------------
#         # Step 2: Vector search with threshold
#         # ---------------------------
#         results = (
#             db.query(
#                 JobEmbedding,
#                 JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
#             )
#             .filter(JobEmbedding.embedding.cosine_distance(q_vector) < distance_threshold)
#             .order_by("distance")   # smaller distance = better
#             .limit(top_k * 3)       # extra for de-duplication
#             .all()
#         )

#         print(f"results: {results}")
#         for job_chunk, distance in results:
#             print(f"job_chunk: {job_chunk}")
#             print(f"distance: {distance}")

#         # ---------------------------
#         # Step 3: Format results & avoid duplicate jobs
#         # ---------------------------
#         seen_jobs = set()
#         formatted_results = []

#         for job_chunk, distance in results:
#             if job_chunk.serial_no in seen_jobs:
#                 continue
#             seen_jobs.add(job_chunk.serial_no)

#             score = round(1 - distance, 4)

#             formatted_results.append({
#                 "chunk_id": job_chunk.id,
#                 "serial_no": job_chunk.serial_no,
#                 "company_name": job_chunk.company_name,
#                 "group": job_chunk.chunk_metadata.get("group") if job_chunk.chunk_metadata else "N/A",
#                 "text": job_chunk.chunk_text,
#                 "score": score
#             })

#             if len(formatted_results) >= top_k:
#                 break

#         # ---------------------------
#         # Step 4: Sort by score descending
#         # ---------------------------
#         final_results = sorted(
#             formatted_results,
#             key=lambda x: x["score"],
#             reverse=True
#         )

#         return final_results

#     except Exception as e:
#         print(f"Search error details: {str(e)}")
#         return {"error": str(e)}

#     finally:
#         db.close()





# # ---------simple------------
# def search_jobs(query):
#     db = SessionLocal()
#     try:
#         q_vector = embeddings.embed_query(query)

#         results = (
#             db.query(
#                 JobEmbedding,
#                 JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
#             )
#             .order_by(JobEmbedding.embedding.cosine_distance(q_vector))  #  Ascending order
#             .limit(10)
#             .all()
#         )

#         return [
#             {
#                 "chunk_id": job.id,
#                 "serial_no": job.serial_no,
#                 "company_name": job.company_name,
#                 "chunk_text": job.chunk_text,
#                 "distance": round(distance, 4)   
#             }
#             for job, distance in results
#         ]

#     finally:
#         db.close()






def create_embedding_entry(chunks, raw_job_id, job):
    
    # Here chunks is list[dictionary]

    # From job i can get this values
    job_id_from_job_object=raw_job_id
    serial_no_from_job_object=job.serial_no
    company_name_from_job_object=job.company_name
    title_from_job_object=job.title
    job_category_from_job_object=job.job_category
    employment_type_from_job_object=job.employment_type
    tags_from_job_object=job.tag

    db = SessionLocal()
    try:
        # for chunk in chunks:
        for i in range(0,len(chunks),1):

            chunk_metadata = chunks[i]["metadata"]
            chunk_text=chunks[i]["text"]
            intent=chunks[i]["metadata"]["intent"]
            tags=chunks[i]["metadata"]["tags"]
            vector_embedding = embeddings.embed_query(chunks[i]["text"]) # call embedding function
            
            # ---------------------Prepare obj of JobEmbedding-------------------------
            data={
                # from job
                "job_id":job_id_from_job_object,
                "serial_no":serial_no_from_job_object,
                "company_name":company_name_from_job_object,
                "title": title_from_job_object,
                "job_category": job_category_from_job_object,
                "employment_type": employment_type_from_job_object,
                # from chunks
                "intent": chunks[i]["metadata"]["intent"],
                "tags": tags_from_job_object,
                "chunk_text": chunks[i]["text"],
                "embedding": vector_embedding,
                "chunk_metadata": chunks[i]["metadata"]
            }

            # print(f"data: {data}")

            vector_entry = JobEmbedding(**data)
                
            db.add(vector_entry)
        
        db.commit()
        print(f"Successfully ingested {len(chunks)} chunks for Serial No: {job.serial_no}")

    except Exception as e:
        db.rollback()
        print(f"Error during ingestion: {e}")
        raise e
    finally:
        db.close()









def search_jobs(query,intent_filter=None):
    limit=10
    print(f"intent_filter inside search_jobs function: {intent_filter}")

    db = SessionLocal()
    try:
        q_vector = embeddings.embed_query(query)
        base_query = db.query(
        JobEmbedding,
        JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
        )

        # print(f"base_query: {base_query}")

        # # ------------------meta data filter in single value------------------
        # if intent_filter:
        #     print(f"intent_filter: {intent_filter} applied")
        #     base_query = base_query.filter(JobEmbedding.intent == intent_filter)
        #     print(f"base_query: {base_query}")


        # ------------------meta data filter in list------------------
        if intent_filter:   # If list have any value then apply metadata filter
            print(f"intent_filter applied: {intent_filter}")
            base_query = base_query.filter(JobEmbedding.intent.in_(intent_filter))       # WHERE intent IN ('identity', 'work_content')


        # ------------------vector search------------------
        results = (
            base_query
            .order_by(JobEmbedding.embedding.cosine_distance(q_vector))
            .limit(limit)
            .all()
        )

        output = []

        for job, distance in results:
            output.append({
                "chunk_id": job.id,
                "job_id": job.job_id,
                "serial_no": job.serial_no,
                "company_name": job.company_name,
                "title": job.title,
                "job_category": job.job_category,
                "employment_type": job.employment_type,
                "intent": job.intent,
                # "tags": job.tags,
                "chunk_text": job.chunk_text,
                # "chunk_metadata": job.chunk_metadata,

                "distance": round(distance, 4)
            })
        return output

    finally:
        db.close()
