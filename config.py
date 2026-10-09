
import os
from dotenv import load_dotenv

load_dotenv()


EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2:3b"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
RETRIEVAL_K = 4


def validate_config():
    # Local Ollama models do not require an API key.
    pass

