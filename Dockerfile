# app/Dockerfile (unchanged except for CMD to point to app.main:app)
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]