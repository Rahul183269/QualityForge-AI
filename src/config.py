import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

AI_API_KEY = os.getenv("AI_API_KEY")