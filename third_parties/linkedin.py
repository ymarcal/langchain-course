import os
import requests
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_API_URL = "https://api.linkedin.com/v2"
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN")

def get_linkedin_profile():
    headers = {
        "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{LINKEDIN_API_URL}/me", headers=headers)
    return response.json()