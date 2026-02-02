# app/ai/embeddings.py
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="bge-m3",
    base_url="http://host.docker.internal:11434"
)