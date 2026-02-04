# app/ai_service/embeddings.py
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="bge-m3",  # The model excels in processing varied text lengths (up to 8192 tokens) 
    base_url="http://host.docker.internal:11434"
)

