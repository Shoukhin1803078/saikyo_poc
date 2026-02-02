# app/services/chunking.py
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunking(job):
    print("chunking function called")

    data = {
        "serial_no": job.serial_no,
        "media_site": job.Media_site,
        "company_name": job.Company_name,
        "company_logo": job.Company_logo,
        "title": job.Title,
        "catchphrase": job.Catchphrase,
        "salary_type": job.Salary_type,
        "salary": job.Salary,
        "salary_details": job.Salary_details,
        "employment_type": job.Employment_Type,
        "job_industry": job.Job_Industry,
        "job_category": job.Job_Category,
        "social_insurances": job.Social_insurances,
        "benefits_1": job.Job_Benefits_Details1,
        "benefits_2": job.Job_Benefits_Details2,
        "holidays_leaves": job.Holidays_Leaves_Details,
        "description": job.Description,
        "requirements": job.Requirements,
        "requirements_summary": job.Requirements_summary,
        "service_form": job.Service_Form,
        "working_hours": job.Working_hours,
        "one_day_work_details": job.One_day_work_details,
        "nearest_station": job.Nearest_Station,
        "nearest_station_access": job.Nearest_station_access,
        "selection_flow": job.Selection_flow,
        "recruiter_message": job.Recruiter_message,
        "postal_code": job.Postal_Code,
        "address_details": job.Address_details,
        "google_map_url": job.Google_Map_Url,
        "trial_period_duration": job.Trial_period_duration,
        "trial_period_details": job.Trial_period_details,
        "trial_period_salary": job.Trial_period_salary,
        "trial_period_working_hours": job.Trial_period_working_hours,
        "tag": job.Tag
    }
    print(f"data======{data}")  # Keeping your print for debugging

    # Setup LangChain splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = []  # List to store all chunks

    # Summary chunk: Combine key short fields into one overview chunk
    summary_text = (
        f"Media site: {data.get('media_site', '')}\n"
        f"Company name: {data.get('company_name', '')}\n"
        f"Title: {data.get('title', '')}\n"
        f"Catchphrase: {data.get('catchphrase', '')}\n"
        f"Salary: {data.get('salary_type', '')} {data.get('salary', '')}\n"
        f"Employment Type: {data.get('employment_type', '')}\n"
        f"Job Industry: {data.get('job_industry', '')}\n"
        f"Job Category: {data.get('job_category', '')}\n"
        f"Working hours: {data.get('working_hours', '')}\n"
        f"Nearest Station: {data.get('nearest_station', '')}\n"
        f"Nearest station access: {data.get('nearest_station_access', '')}\n"
        f"Postal Code: {data.get('postal_code', '')}\n"
        f"Address details: {data.get('address_details', '')}\n"
        f"Google Map Url: {data.get('google_map_url', '')}\n"
        f"Trial period duration: {data.get('trial_period_duration', '')}\n"
        f"Requirements Summary: {data.get('requirements_summary', '')}\n"
        f"Tags: {', '.join(data.get('tag', []))}"
    )
    chunks.append({
        "text": summary_text,
        "metadata": {"serial_no": data["serial_no"], "chunk_type": "summary"}
    })

    # Long fields to chunk individually
    long_fields = {
        "salary_details": data.get("salary_details", ""),
        "social_insurances": data.get("social_insurances", ""),
        "benefits_1": data.get("benefits_1", ""),
        "benefits_2": data.get("benefits_2", ""),
        "holidays_leaves": data.get("holidays_leaves", ""),
        "description": data.get("description", ""),
        "requirements": data.get("requirements", ""),
        "one_day_work_details": data.get("one_day_work_details", ""),
        "selection_flow": data.get("selection_flow", ""),
        "recruiter_message": data.get("recruiter_message", ""),
        "trial_period_details": data.get("trial_period_details", ""),
        "trial_period_salary": data.get("trial_period_salary", ""),
        "trial_period_working_hours": data.get("trial_period_working_hours", "")
    }

    for field_name, field_text in long_fields.items():
        if field_text:  # Skip if null/empty
            if len(field_text) > 500:
                sub_chunks = text_splitter.split_text(field_text)
                for i, sub_chunk_text in enumerate(sub_chunks, 1):
                    chunks.append({
                        "text": sub_chunk_text,
                        "metadata": {"serial_no": data["serial_no"], "chunk_type": f"{field_name}_part{i}"}
                    })
            else:
                chunks.append({
                    "text": field_text,
                    "metadata": {"serial_no": data["serial_no"], "chunk_type": field_name}
                })

    # For debugging: Print chunks (optional, can remove later)
    # for chunk in chunks:
    #     print(f"Chunk Text: {chunk['text'][:100]}...")
    #     print(f"Metadata: {chunk['metadata']}\n")

    print(f"Total chunks: {len(chunks)}")
    print(f"chunks: {chunks}")

    for i in range(0,len(chunks),1):
        print(f"The {i}th Chunk Text: {chunks[i]['text']}...")
        print(f"Metadata: {chunks[i]['metadata']}\n")

    return chunks  # Return list of chunks for further use (e.g., embedding)