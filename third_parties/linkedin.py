import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Posso tentar achar uma API grátis para fazer o scraping


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from a LinkedIn profile,
    Manually scrape the information from the LinkedIn profile page."""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/ymarcal/3bc6342912265a34f6def3b21a3c406a/raw/0237c2a3583ca045999faacb0b5aaa73c4b4f785/jonatan-lima-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ['SCRAPIN_API_KEY'],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None) and k not in ["certifications"]
    }

    return data

if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/jonatan-de-lima-santos-852j/", mock=True
        )
    )