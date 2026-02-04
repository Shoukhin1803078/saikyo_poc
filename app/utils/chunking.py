# app/services/chunking.py


# --------------------------------------Previous------------------------------------


#from langchain_text_splitters import RecursiveCharacterTextSplitter

# def chunking(job):
#     print("chunking function called")

#     data = {
#         "serial_no": job.serial_no,
#         "media_site": job.Media_site,
#         "company_name": job.Company_name,
#         "company_logo": job.Company_logo,
#         "title": job.Title,
#         "catchphrase": job.Catchphrase,
#         "salary_type": job.Salary_type,
#         "salary": job.Salary,
#         "salary_details": job.Salary_details,
#         "employment_type": job.Employment_Type,
#         "job_industry": job.Job_Industry,
#         "job_category": job.Job_Category,
#         "social_insurances": job.Social_insurances,
#         "benefits_1": job.Job_Benefits_Details1,
#         "benefits_2": job.Job_Benefits_Details2,
#         "holidays_leaves": job.Holidays_Leaves_Details,
#         "description": job.Description,
#         "requirements": job.Requirements,
#         "requirements_summary": job.Requirements_summary,
#         "service_form": job.Service_Form,
#         "working_hours": job.Working_hours,
#         "one_day_work_details": job.One_day_work_details,
#         "nearest_station": job.Nearest_Station,
#         "nearest_station_access": job.Nearest_station_access,
#         "selection_flow": job.Selection_flow,
#         "recruiter_message": job.Recruiter_message,
#         "postal_code": job.Postal_Code,
#         "address_details": job.Address_details,
#         "google_map_url": job.Google_Map_Url,
#         "trial_period_duration": job.Trial_period_duration,
#         "trial_period_details": job.Trial_period_details,
#         "trial_period_salary": job.Trial_period_salary,
#         "trial_period_working_hours": job.Trial_period_working_hours,
#         "tag": job.Tag
#     }
#     print(f"data======{data}")  # Keeping your print for debugging

#     # Setup LangChain splitter
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100,
#         length_function=len,
#         separators=["\n\n", "\n", " ", ""]
#     )

#     chunks = []  # List to store all chunks

#     # Summary chunk: Combine key short fields into one overview chunk
#     summary_text = (
#         f"Media site: {data.get('media_site', '')}\n"
#         f"Company name: {data.get('company_name', '')}\n"
#         f"Title: {data.get('title', '')}\n"
#         f"Catchphrase: {data.get('catchphrase', '')}\n"
#         f"Salary: {data.get('salary_type', '')} {data.get('salary', '')}\n"
#         f"Employment Type: {data.get('employment_type', '')}\n"
#         f"Job Industry: {data.get('job_industry', '')}\n"
#         f"Job Category: {data.get('job_category', '')}\n"
#         f"Working hours: {data.get('working_hours', '')}\n"
#         f"Nearest Station: {data.get('nearest_station', '')}\n"
#         f"Nearest station access: {data.get('nearest_station_access', '')}\n"
#         f"Postal Code: {data.get('postal_code', '')}\n"
#         f"Address details: {data.get('address_details', '')}\n"
#         f"Google Map Url: {data.get('google_map_url', '')}\n"
#         f"Trial period duration: {data.get('trial_period_duration', '')}\n"
#         f"Requirements Summary: {data.get('requirements_summary', '')}\n"
#         f"Tags: {', '.join(data.get('tag', []))}"
#     )
#     chunks.append({
#         "text": summary_text,
#         "metadata": {"serial_no": data["serial_no"], "chunk_type": "summary"}
#     })

#     # Long fields to chunk individually
#     long_fields = {
#         "salary_details": data.get("salary_details", ""),
#         "social_insurances": data.get("social_insurances", ""),
#         "benefits_1": data.get("benefits_1", ""),
#         "benefits_2": data.get("benefits_2", ""),
#         "holidays_leaves": data.get("holidays_leaves", ""),
#         "description": data.get("description", ""),
#         "requirements": data.get("requirements", ""),
#         "one_day_work_details": data.get("one_day_work_details", ""),
#         "selection_flow": data.get("selection_flow", ""),
#         "recruiter_message": data.get("recruiter_message", ""),
#         "trial_period_details": data.get("trial_period_details", ""),
#         "trial_period_salary": data.get("trial_period_salary", ""),
#         "trial_period_working_hours": data.get("trial_period_working_hours", "")
#     }

#     for field_name, field_text in long_fields.items():
#         if field_text:  # Skip if null/empty
#             if len(field_text) > 500:
#                 sub_chunks = text_splitter.split_text(field_text)
#                 for i, sub_chunk_text in enumerate(sub_chunks, 1):
#                     chunks.append({
#                         "text": sub_chunk_text,
#                         "metadata": {"serial_no": data["serial_no"], "chunk_type": f"{field_name}_part{i}"}
#                     })
#             else:
#                 chunks.append({
#                     "text": field_text,
#                     "metadata": {"serial_no": data["serial_no"], "chunk_type": field_name}
#                 })

#     # For debugging: Print chunks (optional, can remove later)
#     # for chunk in chunks:
#     #     print(f"Chunk Text: {chunk['text'][:100]}...")
#     #     print(f"Metadata: {chunk['metadata']}\n")

#     print(f"Total chunks: {len(chunks)}")
#     print(f"chunks: {chunks}")

#     for i in range(0,len(chunks),1):
#         print(f"The {i}th Chunk Text: {chunks[i]['text']}...")
#         print(f"Metadata: {chunks[i]['metadata']}\n")

#     return chunks  # Return list of chunks for further use (e.g., embedding)







# --------------------------------------Gemini------------------------------------



# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def chunking(job):
#     print("chunking function called")

#     # ডাটা ডিকশনারি তৈরি (আপনার দেওয়া ফরম্যাট অনুযায়ী)
#     data = {
#         "serial_no": job.serial_no,
#         "media_site": job.media_site,
#         "company_name": job.company_name,
#         "title": job.title,
#         "catchphrase": job.catchphrase,
#         "salary_type": job.salary_type,
#         "salary": job.salary,
#         "salary_details": job.salary_details,
#         "employment_type": job.employment_type,
#         "job_industry": job.job_industry,
#         "job_category": job.job_category,
#         "social_insurances": job.social_insurances,
#         "benefits_1": job.job_benefits_details1,
#         "benefits_2": job.job_benefits_details2,
#         "holidays_leaves": job.holidays_leaves_details,
#         "description": job.description,
#         "requirements": job.requirements,
#         "requirements_summary": job.requirements_summary,
#         "service_form": job.service_form,
#         "working_hours": job.working_hours,
#         "one_day_work_details": job.one_day_work_details,
#         "nearest_station": job.nearest_station,
#         "nearest_station_access": job.nearest_station_access,
#         "selection_flow": job.selection_flow,
#         "recruiter_message": job.recruiter_message,
#         "postal_code": job.postal_code,
#         "address_details": job.address_details,
#         "google_map_url": job.google_map_url,
#         "trial_period_duration": job.trial_period_duration,
#         "trial_period_details": job.trial_period_details,
#         "trial_period_salary": job.trial_period_salary,
#         "trial_period_working_hours": job.trial_period_working_hours,
#         "tag": job.tag,
#         "image_data": job.image_data
#     }
#     print(f"data======{data}")

#     # হাইব্রিড সার্চের জন্য কি-ওয়ার্ড এবং আইডেন্টিটি তৈরি
#     identity = f"Media: {data['media_site']} | Company: {data['company_name']} | Title: {data['title']}"
#     keywords = (
#         f"Keywords: {data['company_name']}, {data['job_category']}, {data['job_industry']}, "
#         f"{data['address_details']}, {data['nearest_station']}, {data['employment_type']}, "
#         f"{', '.join(data['tag']) if data['tag'] else ''}"
#     )

#     # জাপানিজ টেক্সট অপ্টিমাইজড স্প্লিটার
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100,
#         separators=["\n\n", "\n", "。", "！", " ", ""]
#     )

#     chunks = []

#     # --- গ্রুপ ১: ওভারভিউ চাঙ্ক ---
#     overview_text = (
#         f"{identity}\n"
#         f"Catchphrase: {data['catchphrase']}\n"
#         f"Industry: {data['job_industry']} | Category: {data['job_category']}\n"
#         f"Service Form: {data['service_form']}\n"
#         f"{keywords}"
#     )
#     chunks.append({
#         "text": overview_text,
#         "metadata": {"serial_no": data["serial_no"], "group": "overview"}
#     })

#     # --- গ্রুপ ২: আর্থিক ও সুবিধা (Compensation) চাঙ্ক ---
#     compensation_text = (
#         f"{identity}\n"
#         f"Salary: {data['salary_type']} {data['salary']}\n"
#         f"Details: {data['salary_details']}\n"
#         f"Social Insurances: {data['social_insurances']}\n"
#         f"Benefits: {data['benefits_1']} / {data['benefits_2']}\n"
#         f"Holidays: {data['holidays_leaves']}\n"
#         f"Trial: {data['trial_period_duration']} (Details: {data['trial_period_details']}, Salary: {data['trial_period_salary']}, Hours: {data['trial_period_working_hours']})\n"
#         f"{keywords}"
#     )
#     chunks.append({
#         "text": compensation_text,
#         "metadata": {"serial_no": data["serial_no"], "group": "compensation"}
#     })

#     # --- গ্রুপ ৩: কাজের বিবরণ (Description) - যদি বড় হয় তবে স্প্লিট হবে ---
#     if data['description']:
#         desc_main = f"Description: {data['description']}\nDaily Routine: {data['one_day_work_details']}"
#         desc_parts = text_splitter.split_text(desc_main)
#         for i, part in enumerate(desc_parts, 1):
#             chunks.append({
#                 "text": f"{identity} (Details Part {i})\n{part}\n{keywords}",
#                 "metadata": {"serial_no": data["serial_no"], "group": f"description_part_{i}"}
#             })

#     # --- গ্রুপ ৪: রিকোয়ারমেন্টস ও লজিস্টিকস চাঙ্ক ---
#     logistics_text = (
#         f"{identity}\n"
#         f"Requirements: {data['requirements']}\n"
#         f"Summary: {data['requirements_summary']}\n"
#         f"Hours: {data['working_hours']}\n"
#         f"Station: {data['nearest_station']} ({data['nearest_station_access']})\n"
#         f"Address: {data['postal_code']}, {data['address_details']}\n"
#         f"Map: {data['google_map_url']}\n"
#         f"Flow: {data['selection_flow']}\n"
#         f"Message: {data['recruiter_message']}\n"
#         f"{keywords}"
#     )
#     chunks.append({
#         "text": logistics_text,
#         "metadata": {"serial_no": data["serial_no"], "group": "logistics"}
#     })

#     # ডিবাগিং প্রিন্ট
#     print(f"Total chunks generated: {len(chunks)}")
#     for i, chunk in enumerate(chunks):
#         print(f"Chunk {i} Group: {chunk['metadata']['group']}")
#         print(f"Text: {chunk['text']}\n")
#         print(f"metadata: {chunk['metadata']}\n")

#     return chunks













# --------------------------------------Openai--------------------------------------  

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def chunking(job):
#     """
#     Convert a single job object into multiple semantic chunks for RAG.
#     This version does NOT use a safe() helper; all fields are directly concatenated.
#     """

#     # -------------------------------
#     # Job data extraction (image_data ignored)
#     # -------------------------------
#     data = {
#         "serial_no": job.serial_no,
#         "media_site": job.media_site,
#         "company_name": job.company_name,
#         "title": job.title,
#         "catchphrase": job.catchphrase,
#         "salary_type": job.salary_type,
#         "salary": job.salary,
#         "salary_details": job.salary_details,
#         "employment_type": job.employment_type,
#         "job_industry": job.job_industry,
#         "job_category": job.job_category,
#         "social_insurances": job.social_insurances,
#         "benefits_1": job.job_benefits_details1,
#         "benefits_2": job.job_benefits_details2,
#         "holidays_leaves": job.holidays_leaves_details,
#         "description": job.description,
#         "requirements": job.requirements,
#         "requirements_summary": job.requirements_summary,
#         "service_form": job.service_form,
#         "working_hours": job.working_hours,
#         "one_day_work_details": job.one_day_work_details,
#         "nearest_station": job.nearest_station,
#         "nearest_station_access": job.nearest_station_access,
#         "selection_flow": job.selection_flow,
#         "recruiter_message": job.recruiter_message,
#         "postal_code": job.postal_code,
#         "address_details": job.address_details,
#         "google_map_url": job.google_map_url,
#         "trial_period_duration": job.trial_period_duration,
#         "trial_period_details": job.trial_period_details,
#         "trial_period_salary": job.trial_period_salary,
#         "trial_period_working_hours": job.trial_period_working_hours,
#         "tag": job.tag,
#     }

#     # -------------------------------
#     # Identity block (shared context)
#     # -------------------------------
#     identity = (
#         f"Media: {data['media_site']} | "
#         f"Company: {data['company_name']} | "
#         f"Title: {data['title']}"
#     )

#     # -------------------------------
#     # Tag normalization
#     # -------------------------------
#     tag_text = ""
#     if isinstance(data["tag"], list):
#         tag_text = ", ".join(data["tag"])
#     elif isinstance(data["tag"], dict):
#         tag_text = ", ".join(map(str, data["tag"].values()))
#     elif isinstance(data["tag"], str):
#         tag_text = data["tag"]

#     # -------------------------------
#     # Keywords (NO nearest_station)
#     # -------------------------------
#     keywords = (
#         f"Keywords: "
#         f"{data['company_name']}, "
#         f"{data['job_category']}, "
#         f"{data['job_industry']}, "
#         f"{data['employment_type']}, "
#         f"{tag_text}"
#     )

#     # -------------------------------
#     # Japanese-friendly text splitter
#     # -------------------------------
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=600,
#         chunk_overlap=100,
#         separators=["\n\n", "\n", "。", "！", " ", ""]
#     )

#     chunks = []

#     # =========================================================
#     # GROUP 1: OVERVIEW
#     # =========================================================
#     overview_text = (
#         f"{identity}\n"
#         f"Catchphrase: {data['catchphrase']}\n"
#         f"Industry: {data['job_industry']}\n"
#         f"Category: {data['job_category']}\n"
#         f"Employment Type: {data['employment_type']}\n"
#         f"Service Form: {data['service_form']}\n"
#         f"{keywords}"
#     )

#     chunks.append({
#         "text": overview_text,
#         "metadata": {
#             "serial_no": data["serial_no"],
#             "group": "overview"
#         }
#     })

#     # =========================================================
#     # GROUP 2: COMPENSATION
#     # =========================================================
#     compensation_text = (
#         f"{identity}\n"
#         f"Salary: {data['salary_type']} {data['salary']}\n"
#         f"Salary Details: {data['salary_details']}\n"
#         f"Social Insurances: {data['social_insurances']}\n"
#         f"Benefits: {data['benefits_1']} / {data['benefits_2']}\n"
#         f"Holidays: {data['holidays_leaves']}\n"
#         f"Trial Period: {data['trial_period_duration']}\n"
#         f"Trial Details: {data['trial_period_details']}\n"
#         f"Trial Salary: {data['trial_period_salary']}\n"
#         f"Trial Working Hours: {data['trial_period_working_hours']}\n"
#         f"{keywords}"
#     )

#     chunks.append({
#         "text": compensation_text,
#         "metadata": {
#             "serial_no": data["serial_no"],
#             "group": "compensation"
#         }
#     })

#     # =========================================================
#     # GROUP 3: DESCRIPTION (chunked)
#     # =========================================================
#     if data["description"]:
#         desc_parts = text_splitter.split_text(
#             f"Job Description:\n{data['description']}\n{keywords}"
#         )
#         for i, part in enumerate(desc_parts, 1):
#             chunks.append({
#                 "text": f"{identity} | Description Part {i}\n{part}",
#                 "metadata": {
#                     "serial_no": data["serial_no"],
#                     "group": f"description_part_{i}"
#                 }
#             })

#     # =========================================================
#     # GROUP 4: DAILY WORK DETAILS
#     # =========================================================
#     if data["one_day_work_details"]:
#         daily_parts = text_splitter.split_text(
#             f"Daily Work Details:\n{data['one_day_work_details']}\n{keywords}"
#         )
#         for i, part in enumerate(daily_parts, 1):
#             chunks.append({
#                 "text": f"{identity} | Daily Work Part {i}\n{part}",
#                 "metadata": {
#                     "serial_no": data["serial_no"],
#                     "group": f"daily_work_part_{i}"
#                 }
#             })

#     # =========================================================
#     # GROUP 5: REQUIREMENTS + LOGISTICS
#     # =========================================================
#     logistics_text = (
#         f"{identity}\n"
#         f"Requirements: {data['requirements']}\n"
#         f"Requirements Summary: {data['requirements_summary']}\n"
#         f"Working Hours: {data['working_hours']}\n"
#         f"Nearest Station: {data['nearest_station']} ({data['nearest_station_access']})\n"
#         f"Address: {data['postal_code']} {data['address_details']}\n"
#         f"Google Map: {data['google_map_url']}\n"
#         f"Selection Flow: {data['selection_flow']}\n"
#         f"Recruiter Message: {data['recruiter_message']}\n"
#         f"{keywords}"
#     )

#     chunks.append({
#         "text": logistics_text,
#         "metadata": {
#             "serial_no": data["serial_no"],
#             "group": "logistics"
#         }
#     })

#     return chunks







# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def chunking(job):
#     """
#     Convert a single job object into multiple semantic chunks for RAG.
#     This version does NOT use a safe() helper; all fields are directly concatenated.
#     """

#     # -------------------------------
#     # Job data extraction (image_data ignored)
#     # -------------------------------
#     data = {
#         "serial_no": job.serial_no,
#         "media_site": job.media_site,
#         "company_name": job.company_name,
#         "title": job.title,
#         "catchphrase": job.catchphrase,
#         "salary_type": job.salary_type,
#         "salary": job.salary,
#         "salary_details": job.salary_details,
#         "employment_type": job.employment_type,
#         "job_industry": job.job_industry,
#         "job_category": job.job_category,
#         "social_insurances": job.social_insurances,
#         "benefits_1": job.job_benefits_details1,
#         "benefits_2": job.job_benefits_details2,
#         "holidays_leaves": job.holidays_leaves_details,
#         "description": job.description,
#         "requirements": job.requirements,
#         "requirements_summary": job.requirements_summary,
#         "service_form": job.service_form,
#         "working_hours": job.working_hours,
#         "one_day_work_details": job.one_day_work_details,
#         "nearest_station": job.nearest_station,
#         "nearest_station_access": job.nearest_station_access,
#         "selection_flow": job.selection_flow,
#         "recruiter_message": job.recruiter_message,
#         "postal_code": job.postal_code,
#         "address_details": job.address_details,
#         "google_map_url": job.google_map_url,
#         "trial_period_duration": job.trial_period_duration,
#         "trial_period_details": job.trial_period_details,
#         "trial_period_salary": job.trial_period_salary,
#         "trial_period_working_hours": job.trial_period_working_hours,
#         "tag": job.tag,
#     }

#     # -------------------------------
#     # Identity block (shared context)
#     # -------------------------------
#     identity = (
#         f"Media: {data['media_site']} | "
#         f"Company: {data['company_name']} | "
#         f"Title: {data['title']}"
#     )

#     # -------------------------------
#     # Tag normalization
#     # -------------------------------
#     tag_text = ""
#     if isinstance(data["tag"], list):
#         tag_text = ", ".join(data["tag"])
#     elif isinstance(data["tag"], dict):
#         tag_text = ", ".join(map(str, data["tag"].values()))
#     elif isinstance(data["tag"], str):
#         tag_text = data["tag"]

#     # -------------------------------
#     # Keywords (NO nearest_station)
#     # -------------------------------
#     keywords = (
#         f"Keywords: "
#         f"{data['company_name']}, "
#         f"{data['job_category']}, "
#         f"{data['job_industry']}, "
#         f"{data['employment_type']}, "
#         f"{tag_text}"
#     )

#     # -------------------------------
#     # Japanese-friendly text splitter
#     # -------------------------------
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100,
#         separators=["\n\n", "\n", "。", "！", " ", ""]
#     )

#     chunks = []

#     # =========================================================
#     # GROUP 1: OVERVIEW
#     # =========================================================
#     overview_text = (
#         f"{identity}\n"
#         f"Catchphrase: {data['catchphrase']}\n"
#         f"Industry: {data['job_industry']}\n"
#         f"Category: {data['job_category']}\n"
#         f"Employment Type: {data['employment_type']}\n"
#         f"Service Form: {data['service_form']}\n"
#         f"{keywords}"
#     )

#     chunks.append({
#         "text": overview_text,
#         "metadata": {
#             "serial_no": data["serial_no"],
#             "group": "overview"
#         }
#     })

#     # =========================================================
#     # GROUP 2: COMPENSATION
#     # =========================================================
#     compensation_text = (
#         f"{identity}\n"
#         f"Salary: {data['salary_type']} {data['salary']}\n"
#         f"Salary Details: {data['salary_details']}\n"
#         f"Social Insurances: {data['social_insurances']}\n"
#         f"Benefits: {data['benefits_1']} / {data['benefits_2']}\n"
#         f"Holidays: {data['holidays_leaves']}\n"
#         f"Trial Period: {data['trial_period_duration']}\n"
#         f"Trial Details: {data['trial_period_details']}\n"
#         f"Trial Salary: {data['trial_period_salary']}\n"
#         f"Trial Working Hours: {data['trial_period_working_hours']}\n"
#         f"{keywords}"
#     )

#     chunks.append({
#         "text": compensation_text,
#         "metadata": {
#             "serial_no": data["serial_no"],
#             "group": "compensation"
#         }
#     })

#     # =========================================================
#     # GROUP 3: DESCRIPTION (chunked)
#     # =========================================================
#     if data["description"]:
#         desc_parts = text_splitter.split_text(
#             f"Job Description:\n{data['description']}\n{keywords}"
#         )
#         for i, part in enumerate(desc_parts, 1):
#             chunks.append({
#                 "text": f"{identity} | Description Part {i}\n{part}",
#                 "metadata": {
#                     "serial_no": data["serial_no"],
#                     "group": f"description_part_{i}"
#                 }
#             })

#     # =========================================================
#     # GROUP 4: DAILY WORK DETAILS
#     # =========================================================
#     if data["one_day_work_details"]:
#         daily_parts = text_splitter.split_text(
#             f"Daily Work Details:\n{data['one_day_work_details']}\n{keywords}"
#         )
#         for i, part in enumerate(daily_parts, 1):
#             chunks.append({
#                 "text": f"{identity} | Daily Work Part {i}\n{part}",
#                 "metadata": {
#                     "serial_no": data["serial_no"],
#                     "group": f"daily_work_part_{i}"
#                 }
#             })

#     # =========================================================
#     # GROUP 5: REQUIREMENTS + LOGISTICS
#     # =========================================================
#     logistics_text = (
#         f"{identity}\n"
#         f"Requirements: {data['requirements']}\n"
#         f"Requirements Summary: {data['requirements_summary']}\n"
#         f"Working Hours: {data['working_hours']}\n"
#         f"Nearest Station: {data['nearest_station']} ({data['nearest_station_access']})\n"
#         f"Address: {data['postal_code']} {data['address_details']}\n"
#         f"Google Map: {data['google_map_url']}\n"
#         f"Selection Flow: {data['selection_flow']}\n"
#         f"Recruiter Message: {data['recruiter_message']}\n"
#         f"{keywords}"
#     )

#     chunks.append({
#         "text": logistics_text,
#         "metadata": {
#             "serial_no": data["serial_no"],
#             "group": "logistics"
#         }
#     })

#     return chunks













from langchain_text_splitters import RecursiveCharacterTextSplitter


def normalize_tag(tag):
    if isinstance(tag, list):
        return tag
    if isinstance(tag, dict):
        return list(tag.values())
    if isinstance(tag, str):
        return [tag]
    return []


# -----------------------------------
# Token Guard Configuration
# -----------------------------------
MAX_SAFE_CHARS = 6000   # ~ safe for 8k token model


splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n", "\n", "。", "、", "！", "？", " ", ""]
)


def apply_token_guard(text):
    """
    Ensures text never exceeds safe embedding length.
    Splits text only when necessary.
    """
    if not text or len(text) <= MAX_SAFE_CHARS:
        return [text]

    return splitter.split_text(text)


def chunking(job):

    tags = normalize_tag(job.tag)

    chunks = []

    base_meta = {
        "serial_no": job.serial_no,
        "company_name": job.company_name,
        "title": job.title,
        "job_category": job.job_category,
        "employment_type": job.employment_type,
        "tags": tags
    }

    # =========================================================
    # CHUNK 1 — Identity
    # =========================================================
    identity_text = f"""
Media Site: {job.media_site or ""}
Company: {job.company_name or ""}
Title: {job.title or ""}
Catchphrase: {job.catchphrase or ""}
Industry: {job.job_industry or ""}
Category: {job.job_category or ""}
Employment Type: {job.employment_type or ""}
Service Form: {job.service_form or ""}
"""

    for part in apply_token_guard(identity_text):
        chunks.append({
            "text": part.strip(),
            "metadata": {**base_meta, "intent": "identity"}
        })

    # =========================================================
    # CHUNK 2 — Work Content
    # =========================================================
    work_text = f"""
Job Description:
{job.description or ""}

One Day Work Details:
{job.one_day_work_details or ""}
"""

    for i, part in enumerate(apply_token_guard(work_text)):
        chunks.append({
            "text": part.strip(),
            "metadata": {**base_meta, "intent": "work_content", "part": i + 1}
        })

    # =========================================================
    # CHUNK 3 — Requirements
    # =========================================================
    requirement_text = f"""
                    Requirements:
                    {job.requirements or ""}

                    Requirement Summary:
                    {job.requirements_summary or ""}
                """

    for part in apply_token_guard(requirement_text):
        chunks.append({
            "text": part.strip(),
            "metadata": {**base_meta, "intent": "requirements"}
        })

    # =========================================================
    # CHUNK 4 — Compensation
    # =========================================================
    compensation_text = f"""
Salary Type: {job.salary_type or ""}
Salary: {job.salary or ""}
Salary Details:{job.salary_details or ""}
Trial Period Duration: {job.trial_period_duration or ""}
Trial Period Details: {job.trial_period_details or ""}
Trial Period Salary: {job.trial_period_salary or ""}
Trial Working Hours: {job.trial_period_working_hours or ""}
"""

    for part in apply_token_guard(compensation_text):
        chunks.append({
            "text": part.strip(),
            "metadata": {**base_meta, "intent": "compensation"}
        })

    # =========================================================
    # CHUNK 5 — Benefits
    # =========================================================
    benefits_text = f"""
Social Insurances:
{job.social_insurances or ""}

Benefits:
{job.job_benefits_details1 or ""}
{job.job_benefits_details2 or ""}

Holidays & Leaves:
{job.holidays_leaves_details or ""}

Tags:
{", ".join(tags)}
"""

    for part in apply_token_guard(benefits_text):
        chunks.append({
            "text": part.strip(),
            "metadata": {**base_meta, "intent": "benefits"}
        })

    # =========================================================
    # CHUNK 6 — Logistics
    # =========================================================
    logistics_text = f"""
Working Hours: {job.working_hours or ""}

Nearest Station:
{job.nearest_station or ""}

Station Access:
{job.nearest_station_access or ""}

Postal Code: {job.postal_code or ""}
Address: {job.address_details or ""}
Google Map: {job.google_map_url or ""}
"""

    for part in apply_token_guard(logistics_text):
        chunks.append({
            "text": part.strip(),
            "metadata": {**base_meta, "intent": "logistics"}
        })

    # =========================================================
    # CHUNK 7 — Hiring Flow
    # =========================================================
    hiring_text = f"""
Selection Flow:
{job.selection_flow or ""}

Recruiter Message:
{job.recruiter_message or ""}
"""

    for part in apply_token_guard(hiring_text):
        chunks.append({
            "text": part.strip(),
            "metadata": {**base_meta, "intent": "hiring_flow"}
        })

    return chunks




# ---------------------------Output-----------------------------
# chunks[0]={
# 'text': 'Media Site: Fudosanworks\n                    Company: 株式会社バンダイ\n                    Title: 不動産事務／地域密着・ネイル自由✨にぎやかオフィスの“秘密兵器”募集！\n                   Catchphrase: 髪色・ネイルOKで“自分らしさ”も働きやすさも両方ゲット♪PC作業から外での撮影まで、動きのある事務ワークで営業をサポート◎\n                    Industry: 営業・仲介・販売系\n                    Category: 営業事務\n                    Employment Type: 正社員\n                    Service Form: 出社勤務', 
# 'metadata': {'serial_no': 2, 'company_name': '株式会社バンダイ', 'title': '不動産事務／地域密着・ネイル自由✨にぎやかオフィスの“秘密兵器”募集！', 'job_category': '営業事務', 'employment_type': '正社員', 'tags': ['出社勤務', '資格手当あり', '未経験歓迎', '経験者優遇', '第二新卒歓迎', '異業種からの転職歓迎', 'マネジメント経験者歓迎', 'ネイルOK', '髪色自由'], 'intent': 'identity'}
# }


