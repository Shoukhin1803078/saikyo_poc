# app/models/jobs.py
from sqlalchemy import Column, Integer, String, Text, Float, JSON
from pgvector.sqlalchemy import Vector
from app.core.database import Base

class AllJob(Base):
    __tablename__ = "all_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_no = Column(Float)
    media_site = Column(String(255))
    company_name = Column(String(255))
    company_logo = Column(String(500), nullable=True)
    title = Column(String(500))
    catchphrase = Column(Text)
    salary_type = Column(String(100))
    salary = Column(Text)  # Changed to Text to accept any format
    salary_details = Column(Text)
    employment_type = Column(String(100))
    job_industry = Column(String(255))
    job_category = Column(String(255))
    social_insurances = Column(Text)
    benefits_1 = Column(Text)
    benefits_2 = Column(Text)
    holidays_leaves = Column(Text)
    description = Column(Text)
    requirements = Column(Text)
    requirements_summary = Column(Text)
    service_form = Column(String(100))
    working_hours = Column(String(255))
    one_day_work_details = Column(Text, nullable=True)
    nearest_station = Column(Text)
    nearest_station_access = Column(Text)
    selection_flow = Column(Text)
    recruiter_message = Column(Text, nullable=True)
    postal_code = Column(String(20))
    address_details = Column(Text)
    google_map_url = Column(String(500))
    trial_period_duration = Column(String(100))
    trial_period_details = Column(Text)
    tag = Column(JSON)

class JobEmbedding(Base):
    __tablename__ = "job_embeddings"

    id = Column(Integer, primary_key=True,autoincrement=True)
    job_id = Column(Integer)  # Added to link to AllJob
    # title = Column(String(500))
    # description = Column(Text)
    # postal_code = Column(String(20))
    serial_no = Column(Integer, nullable=True)
    company_name = Column(String(255), nullable=True)
    embedding = Column(Vector(1024))
    chunk_metadata = Column(JSON, nullable=True)