# app/schemas/job.py
from pydantic import BaseModel, Field
from typing import List, Optional, Any

class JobInput(BaseModel):
    serial_no: float
    Media_site: Optional[str] = Field(None, alias="Media site")
    Company_name: str = Field(..., alias="Company name")
    Company_logo: Optional[str] = Field(None, alias="Company logo")
    Title: str
    Catchphrase: Optional[str] = None
    Salary_type: Optional[str] = Field(None, alias="Salary type")
    Salary: Optional[Any] = None  # Accepts int or string as-is
    Salary_details: Optional[str] = Field(None, alias="Salary details")
    Employment_Type: Optional[str] = Field(None, alias="Employment Type")
    Job_Industry: Optional[str] = Field(None, alias="Job Industry")
    Job_Category: Optional[str] = Field(None, alias="Job Category")
    Social_insurances: Optional[str] = Field(None, alias="Social insurances")
    Job_Benefits_Details1: Optional[str] = Field(None, alias="Job Benefits Details1")
    Job_Benefits_Details2: Optional[str] = Field(None, alias="Job Benefits Details2")
    Holidays_Leaves_Details: Optional[str] = Field(None, alias="Holidays & Leaves Details")
    Description: str
    Requirements: Optional[str] = None
    Requirements_summary: Optional[str] = Field(None, alias="Requirements summary")
    Service_Form: Optional[str] = Field(None, alias="Service Form")
    Working_hours: Optional[str] = Field(None, alias="Working hours")
    One_day_work_details: Optional[str] = Field(None, alias="One day work details")
    Nearest_Station: Optional[str] = Field(None, alias="Nearest Station")
    Nearest_station_access: Optional[str] = Field(None, alias="Nearest station access")
    Selection_flow: Optional[str] = Field(None, alias="Selection flow")
    Recruiter_message: Optional[str] = Field(None, alias="Recruiter message")
    Postal_Code: Optional[str] = Field(None, alias="Postal Code")
    Address_details: Optional[str] = Field(None, alias="Address details")
    Google_Map_Url: Optional[str] = Field(None, alias="Google Map Url")
    Trial_period_duration: Optional[str] = Field(None, alias="Trial period duration")
    Trial_period_details: Optional[str] = Field(None, alias="Trial period details")
    Trial_period_salary: Optional[str] = Field(None, alias="Trial period salary")
    Trial_period_working_hours: Optional[str] = Field(None, alias="Trial period working hours")
    image_data: Optional[str] = Field(None, alias="image data")
    Tag: List[str] = []

    class Config:
        populate_by_name = True

class SearchRequest(BaseModel):
    query: str