import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB")
)

conn.autocommit = True





# import psycopg2
# import os
# import time
# from dotenv import load_dotenv

# load_dotenv()

# DB_PARAMS = {
#     "user": os.getenv("POSTGRES_USER"),
#     "password": os.getenv("POSTGRES_PASSWORD"),
#     "host": os.getenv("POSTGRES_HOST"),
#     "port": os.getenv("POSTGRES_PORT"),
#     "dbname": os.getenv("POSTGRES_DB"),
# }

# # Retry loop: wait until Postgres + database exists
# for i in range(30):  # retry up to 30 seconds
#     try:
#         conn = psycopg2.connect(**DB_PARAMS)
#         conn.autocommit = True
#         print("✅ Connected to Postgres database")
#         break
#     except psycopg2.OperationalError:
#         print("⏳ Database not ready, retrying in 1s...")
#         time.sleep(1)
# else:
#     raise Exception("❌ Could not connect to Postgres after retries")






