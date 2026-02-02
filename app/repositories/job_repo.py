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
#                 company_name=job.Company_name,
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
                company_name=job.Company_name,
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






def search_jobs(query):
    db = SessionLocal()
    try:
        # ১. ইউজারের কুয়েরিকে এম্বেডিংয়ে রূপান্তর করা
        q_vector = embeddings.embed_query(query)
        
        # ২. সার্চ লজিক
        results = (
            db.query(
                JobEmbedding,
                JobEmbedding.embedding.cosine_distance(q_vector).label("distance")
            )
            # .filter(JobEmbedding.embedding.cosine_distance(q_vector) < 0.5) # থ্রেশহোল্ড একটু বাড়ানো হয়েছে
            .order_by("distance")
            .limit(5)
            .all()
        )
        
        # ৩. রেজাল্ট প্রসেসিং
        formatted_results = []
        for job_chunk, distance in results:
            score = round(1 - distance, 4)
            
            # আপনার মডেল অনুযায়ী কলামের নামগুলো নিশ্চিত করুন:
            # text -> chunk_text
            # metadata -> chunk_metadata
            formatted_results.append({
                "chunk_id": job_chunk.id,
                "serial_no": job_chunk.serial_no,
                "company_name": job_chunk.company_name,
                "text": job_chunk.chunk_text, 
                "group": job_chunk.chunk_metadata.get("group") if job_chunk.chunk_metadata else "N/A",
                "score": score
            })
            
        # ৪. স্কোর অনুযায়ী Ascending (ছোট থেকে বড়) অর্ডারে সাজানো
        # key=lambda x: x['score'] মানে স্কোরের মানের ওপর ভিত্তি করে সর্টিং হবে
        final_results = sorted(formatted_results, key=lambda x: x['score'])
            
        return final_results


    except Exception as e:
        # ডিবাগিংয়ের জন্য পুরো এররটি প্রিন্ট করা ভালো
        print(f"Search error details: {str(e)}")
        return {"error": str(e)}
    finally:
        db.close()