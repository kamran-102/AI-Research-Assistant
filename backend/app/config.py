import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"

MAX_RESULTS = 5          # safe for local PC
MAX_WORKERS = 3          # parallel threads safe for PC
REQUEST_TIMEOUT = 10