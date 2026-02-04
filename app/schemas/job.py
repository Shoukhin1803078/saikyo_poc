# app/schemas/job.py
from pydantic import BaseModel, Field,field_validator
from typing import List, Optional, Any

class MultipleJobResponseModel(BaseModel):
    status: str
    ingested_count: int
    jobs: List[dict]

class JobInput(BaseModel):
    serial_no: int
    media_site: Optional[str] = Field(None, alias="Media site")
    company_name: str = Field(..., alias="Company name")
    company_logo: Optional[str] = Field(None, alias="Company logo")
    title: Optional[str] = Field(None, alias="Title")
    catchphrase: Optional[str] = Field(None, alias="Catchphrase")
    salary_type: Optional[str] = Field(None, alias="Salary type")
    salary: Optional[str] = Field(None, alias="Salary")
    salary_details: Optional[str] = Field(None, alias="Salary details")
    employment_type: Optional[str] = Field(None, alias="Employment Type")
    job_industry: Optional[str] = Field(None, alias="Job Industry")
    job_category: Optional[str] = Field(None, alias="Job Category")
    social_insurances: Optional[str] = Field(None, alias="Social insurances")
    job_benefits_details1: Optional[str] = Field(None, alias="Job Benefits Details1")
    job_benefits_details2: Optional[str] = Field(None, alias="Job Benefits Details2")
    holidays_leaves_details: Optional[str] = Field(None, alias="Holidays & Leaves Details")
    description: Optional[str] = Field(None, alias="Description")
    requirements: Optional[str] = Field(None, alias="Requirements")
    requirements_summary: Optional[str] = Field(None, alias="Requirements summary")
    service_form: Optional[str] = Field(None, alias="Service Form")
    working_hours: Optional[str] = Field(None, alias="Working hours")
    one_day_work_details: Optional[str] = Field(None, alias="One day work details")
    nearest_station: Optional[str] = Field(None, alias="Nearest Station")
    nearest_station_access: Optional[str] = Field(None, alias="Nearest station access")
    selection_flow: Optional[str] = Field(None, alias="Selection flow")
    recruiter_message: Optional[str] = Field(None, alias="Recruiter message")
    postal_code: Optional[str] = Field(None, alias="Postal Code")
    address_details: Optional[str] = Field(None, alias="Address details")
    google_map_url: Optional[str] = Field(None, alias="Google Map Url")
    trial_period_duration: Optional[str] = Field(None, alias="Trial period duration")
    trial_period_details: Optional[str] = Field(None, alias="Trial period details")
    trial_period_salary: Optional[str] = Field(None, alias="Trial period salary")
    trial_period_working_hours: Optional[str] = Field(None, alias="Trial period working hours")
    # tag: List[str] = []
    tag: list[str] = Field(default_factory=list, alias="Tag")
    image_data: Optional[str] = Field(None, alias="image data")

    @field_validator("salary", mode="before")
    @classmethod
    def normalize_salary(cls, v):
        if v is None:
            return None
        return str(v)
    class Config:
        populate_by_name = True


class MultipleJobInputModel(BaseModel):
    jobs: List[JobInput]


class SearchRequest(BaseModel):
    query: str