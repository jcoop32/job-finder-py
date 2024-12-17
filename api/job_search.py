import requests
import os
from dotenv import load_dotenv

# from schemas.job_api_schema import JobPosting

from api.get_location import get_linkedin_location

# from get_location import get_linkedin_location
from linkedin_api import Linkedin

api = Linkedin("coopj3265@gmail.com", os.getenv("linkedin_pass"))

load_dotenv()

job_api_key = os.getenv("job_api_7")
job_api_key2 = os.getenv("job_api_2")

url1 = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"
url2 = "https://linkedin-api8.p.rapidapi.com/search-jobs-v2"
host1 = "linkedin-data-api.p.rapidapi.com"
host2 = "linkedin-api8.p.rapidapi.com"


key_words_list = [
    "Full stack developer",
    "frontend developer",
    "software engineer",
]

location = "103112676"  # chicago


def search_for_jobs(key_words, location_id):
    url = url2

    querystring = {
        "keywords": key_words,
        "locationId": location_id,
        "datePosted": "pastWeek",
        "jobType": "fullTime",
        "sort": "mostRelevant",
    }

    headers = {
        "x-rapidapi-key": job_api_key,
        "x-rapidapi-host": host2,
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response_to_json = response.json()
        data = response_to_json["data"]
        # print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error occured: {e}")


# jobs = search_for_jobs(key_words_list, location)
# print(jobs)

# get_job_details("4073579367")


def search_for_jobs_without_location(
    key_words, datePosted, jobType, experienceLevel, onSiteRemote
):
    url = url2
    location = "103112676"  # chicago
    if datePosted and jobType and experienceLevel and onSiteRemote:
        querystring = {
            "keywords": key_words,
            "locationId": location,
            "datePosted": "pastWeek",
            "jobType": "fullTime",
            "onSiteRemote": [onSiteRemote],
            "sort": "mostRelevant",
        }
    else:
        querystring = {
            "keywords": key_words,
            "locationId": location,
            "datePosted": "pastWeek",
            "jobType": "fullTime",
            "onSiteRemote": [onSiteRemote],
            "sort": "mostRelevant",
        }

    headers = {
        "x-rapidapi-key": job_api_key,
        "x-rapidapi-host": host2,
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        # print(response)
        response_to_json = response.json()
        data = response_to_json["data"]

        return data
    except requests.exceptions.RequestException as e:
        print(f"Error occured: {e}")


# search_for_jobs_without_location(key_words_list)


def job_details(job_id):
    job = api.get_job_skills(job_id)
    job_skills = [skill["skill"]["name"] for skill in job["skillMatchStatuses"][:10]]

    return job_skills
    # print(job_skills)


# job_details("4089332020")
