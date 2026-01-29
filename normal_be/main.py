from fastapi import FastAPI
import json
import requests
from pathlib import Path

app = FastAPI(title="Normal Backend")

AI_BE_URL = "http://ai_be:8000/analyze-jobs"


@app.post("/send-jobs")
def send_jobs():
    jobs_file = Path("jobs_small.json")

    if not jobs_file.exists():
        return {"error": "jobs.json not found"}

    with open(jobs_file, "r", encoding="utf-8") as f:
        jobs = json.load(f)
    
    payload={
        "jobs": jobs
    }

    res = requests.post(
        AI_BE_URL,
        # json={"jobs": jobs},
        json=payload,
        timeout=15
    )

    if res.status_code != 200:
        return {"error": "AI backend failed"}

    return {
        "status": "sent",
        "ai_response": res.json()
    }














# from fastapi import FastAPI
# from pydantic import BaseModel
# import requests

# app = FastAPI(title="Normal Backend")

# AI_BE_URL = "http://ai_be:8001/analyze"

# class UserInput(BaseModel):
#     text: str

# @app.post("/process")
# def process_user_input(user_input: UserInput):

#     payload = {
#         "text": user_input.text
#     }

#     response = requests.post(
#         AI_BE_URL,
#         json=payload,
#         timeout=10
#     )

#     if response.status_code != 200:
#         return {"error": "AI service failed"}
    

#     ai_result = response.json()

#     return {
#         "user_input": user_input.text,
#         "ai_output": ai_result["result"]
#     }
