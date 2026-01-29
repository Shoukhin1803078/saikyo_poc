from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict
from worker import process_jobs_background

app = FastAPI(title="AI Backend")


class JobsRequest(BaseModel):        #. payload={ "jobs": [{....},{....},{....}] }
    jobs: List[Dict]


@app.post("/analyze-jobs")
def analyze_jobs(data: JobsRequest, background_tasks: BackgroundTasks):

    print(f"recieved jobs are ====={data.jobs}")

    background_tasks.add_task(process_jobs_background,data.jobs)

    return {
        "message": "Jobs received. Embedding + DB insert running in background ......"
    }





# from fastapi import FastAPI
# from pydantic import BaseModel
# from llm import llm

# app = FastAPI(title="AI Backend")

# class AIRequest(BaseModel):
#     text: str

# class AIResponse(BaseModel):
#     result: str

# @app.post("/analyze", response_model=AIResponse)
# def analyze_text(data: AIRequest):
#     response = llm(data.text)
#     return {"result": response}
