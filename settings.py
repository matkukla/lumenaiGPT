import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Raise an error if the API key is missing
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in your .env file!")
