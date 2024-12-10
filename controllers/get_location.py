import requests
import os
from dotenv import load_dotenv


load_dotenv()

location_api_key = os.getenv("location_api_3")

url1 = "https://linkedin-data-scraper.p.rapidapi.com/suggestion_location"
url2 = "https://linkedin-bulk-data-scraper.p.rapidapi.com/suggestion_location"
host1 = "linkedin-data-scraper.p.rapidapi.com"
host2 = "linkedin-bulk-data-scraper.p.rapidapi.com"


def get_linkedin_location(location):
    url = url2

    querystring = {"query": location}

    headers = {
        "x-rapidapi-key": location_api_key,
        "x-rapidapi-host": host2,
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        formatted_data = response.json()
        location_id = formatted_data["suggestions"][0]["urn"]
        # location_id = formatted_data
        # print(location_id)
        return location_id
    except requests.exceptions.RequestException as e:
        print(f"Error occured: {e}")


# get_linkedin_location("Chicago, IL")
