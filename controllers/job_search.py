import requests
import os
from dotenv import load_dotenv
from controllers.get_location import get_linkedin_location

load_dotenv()

job_api_key = os.getenv("job_api_2")


def search_for_jobs(key_words, location):
    location_id = get_linkedin_location(location)
    url = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"

    querystring = {
        "keywords": key_words,
        "locationId": location_id,
        "datePosted": "pastWeek",
        "jobType": "fullTime",
        "sort": "mostRelevant",
    }

    headers = {
        "x-rapidapi-key": job_api_key,
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    response_to_json = response.json()
    data = response_to_json["data"]

    # print(data)
    return data


# search_for_jobs("Project manager project manager asssistant", "chicago")
