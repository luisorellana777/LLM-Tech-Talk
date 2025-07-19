import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
REGION = os.getenv("REGION") 
ENDPOINT_ID = os.getenv("ENDPOINT_ID")

if PROJECT_ID is None:
    raise RuntimeError("Missing required environment variable: PROJECT_ID")
if REGION is None:
    raise RuntimeError("Missing required environment variable: REGION")
if ENDPOINT_ID is None:
    raise RuntimeError("Missing required environment variable: ENDPOINT_ID")