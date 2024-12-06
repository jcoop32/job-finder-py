import requests
import os
from dotenv import load_dotenv
import functools


load_dotenv()

job_api_key = os.getenv("location_api_5")


@functools.lru_cache(maxsize=128)
def get_linkedin_location(location):

    url = "https://linkedin-data-scraper.p.rapidapi.com/suggestion_location"

    querystring = {"query": location}

    headers = {
        "x-rapidapi-key": job_api_key,
        "x-rapidapi-host": "linkedin-data-scraper.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    formatted_data = response.json()
    location_id = formatted_data["suggestions"][0]["urn"]
    # location_id = response

    # print(location_id)
    return location_id


# get_linkedin_location("Chicago, IL")
