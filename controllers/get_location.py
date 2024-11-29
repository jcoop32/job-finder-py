import requests
import os
from dotenv import load_dotenv

load_dotenv()

job_api_key = os.getenv("job_api_1")


def get_linkedin_location(location):
    url = "https://linkedin-data-api.p.rapidapi.com/search-locations"

    querystring = {"keyword": location}

    headers = {
        "x-rapidapi-key": job_api_key,
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    response_to_json = response.json()
    data = response_to_json["data"]["items"][0]["id"]

    location_id = data[11:]

    # print(location_id)
    return location_id


# get_linkedin_location("berlin")
