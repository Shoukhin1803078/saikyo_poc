# app/models/jobs.py
from sqlalchemy import Column, Integer, String, Text, Float, JSON
from pgvector.sqlalchemy import Vector
from app.core.database import Base

class AllJob(Base):
    __tablename__ = "all_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_no = Column(Integer)
    media_site = Column(String(255))
    company_name = Column(Text)
    company_logo = Column(String(500), nullable=True)
    title = Column(Text)
    catchphrase = Column(Text)
    salary_type = Column(String(200))
    salary = Column(String(200)) 
    salary_max=Column(String(200),nullable=True)
    salary_min=Column(String(200),nullable=True)
    salary_details = Column(Text)
    employment_type = Column(String(200))
    job_industry = Column(String(200))
    job_category = Column(String(200))
    social_insurances = Column(Text)
    job_benefits_details1 = Column(Text)
    job_benefits_details2 = Column(Text)
    holidays_leaves_details = Column(Text)
    description = Column(Text)
    requirements = Column(Text)
    requirements_summary = Column(Text)
    service_form = Column(String(200))
    working_hours = Column(Text)
    one_day_work_details = Column(Text, nullable=True)
    nearest_station = Column(Text)
    nearest_station_access = Column(Text)
    selection_flow = Column(Text)
    recruiter_message = Column(Text, nullable=True)
    postal_code = Column(String(20))
    address_details = Column(Text)
    google_map_url = Column(Text)
    trial_period_duration = Column(String(200))
    trial_period_details = Column(Text)
    trial_period_salary = Column(Text)
    trial_period_working_hours = Column(String(200))
    tag = Column(JSON)
    # image_data = Column(Text,nullable=True)
    


# ------------------------Previous------------------------
# class JobEmbedding(Base):
#     __tablename__ = "job_embeddings"

#     id = Column(Integer, primary_key=True,autoincrement=True)
#     job_id = Column(Integer)  # Added to link to AllJob
#     # title = Column(String(500))
#     # description = Column(Text)
#     # postal_code = Column(String(20))
#     serial_no = Column(Integer, nullable=True)
#     company_name = Column(String(255), nullable=True)
#     embedding = Column(Vector(1024))
#     chunk_metadata = Column(JSON, nullable=True)






# ------------------------Gemini------------------------

class JobEmbedding(Base):
    __tablename__ = "job_embeddings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer)
    serial_no = Column(Integer, index=True) # মূল জবের সাথে লিঙ্ক করার জন্য
    company_name = Column(String(255), nullable=True)
    
    # চাঙ্ক করা টেক্সট যা সার্চের জন্য এবং ইউজারের সামনে দেখানোর জন্য ব্যবহৃত হবে
    chunk_text = Column(Text, nullable=False) 
    
    # আমরা ১০২৪ ডাইমেনশনের ভেক্টর ব্যবহার করছি (যেমন: Google/OpenAI/Cohere এর ওপর নির্ভর করে)
    embedding = Column(Vector(1024)) 
    
    # চাঙ্কিং এর মেটাডেটা (যেমন: group_type: "logistics" বা "compensation")
    chunk_metadata = Column(JSON, nullable=True)

    # নোট: হাইব্রিড সার্চের জন্য PostgreSQL-এ এই chunk_text কলামের ওপর 
    # একটি GIN Index তৈরি করা জরুরি যাতে কি-ওয়ার্ড সার্চ দ্রুত হয়।