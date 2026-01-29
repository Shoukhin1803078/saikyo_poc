from langchain_ollama import OllamaEmbeddings
from psycopg2.extras import execute_values
from db import conn

# embeddings = OllamaEmbeddings(model="bge-m3")
# embeddings = OllamaEmbeddings(model="bge-m3:latest")
embeddings = OllamaEmbeddings(
    model="bge-m3:latest",
    base_url="http://host.docker.internal:11434"  # ← add this
)


def build_text(job: dict) -> str:
    return f"""
Title: {job.get('Title')}
Catchphrase: {job.get('Catchphrase')}
Description: {job.get('Description')}
Requirements: {job.get('Requirements')}
"""


def process_jobs_background(jobs: list):
    cursor = conn.cursor()
    rows = []

    for job in jobs:
        text = build_text(job)
        print(f"job_id==={job['serial_no']} whole text===={text}")
        vector = embeddings.embed_query(text)
        print(f"vector of job_id {job['serial_no']}======{vector}")

        rows.append((
            job.get("serial_no"),
            text,
            vector
        ))
        print(f"vector of job_id {job['serial_no']} commited in db successfully")




    execute_values(
        cursor,
        """
        INSERT INTO job_embeddings (serial_no, content, embedding)
        VALUES %s
        """,
        rows
    )

    print(f"final inserted successfully")

    cursor.close()





