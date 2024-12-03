import requests
import os
from dotenv import load_dotenv
import numpy as np

from controllers.get_location import get_linkedin_location

# from get_location import get_linkedin_location
from linkedin_api import Linkedin

api = Linkedin("coopj3265@gmail.com", os.getenv("linkedin_pass"))

load_dotenv()

job_api_key = os.getenv("job_api_7")
job_api_key2 = os.getenv("job_api_8")


def search_for_jobs(key_words, location):
    location_id = get_linkedin_location(location)
    url = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"

    querystring = {
        "keywords": key_words,
        "locationId": location_id,
        "datePosted": "past24Hours",
        "jobType": "fullTime",
        "sort": "mostRelevant",
    }

    headers = {
        "x-rapidapi-key": job_api_key2,
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    response_to_json = response.json()
    data = response_to_json["data"]

    # print(data)
    return data


# jobs = search_for_jobs("software engineer", "chicago")


# def get_job_details(job_id):
#     url = "https://linkedin-data-api.p.rapidapi.com/get-job-details"

#     querystring = {"id": job_id}

#     headers = {
#         "x-rapidapi-key": job_api_key,
#         "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
#     }

#     response = requests.get(url, headers=headers, params=querystring)
#     json_form = response.json()
#     details = json_form
#     # return details
#     print(details)


# get_job_details("4073579367")


def job_details(job_id):
    job = api.get_job_skills(job_id)
    job_skills = []
    # append first 10 skills to arr
    for skill in job["skillMatchStatuses"][:10]:
        job_skills.append(skill["skill"]["name"])

    return job_skills
    # print(job_skills)


# job_details("4089332020")


def filtered_jobs(keywords, location, resume_skills):
    jobs = search_for_jobs(keywords, location)
    matched_jobs = []
    set1 = set(s.lower() for s in resume_skills)
    # print(len(jobs))
    # if len(jobs) > 3:
    #     jobs = jobs[:5]
    for job in jobs:
        job_detail = job_details(job["id"])
        set2 = set(s.lower() for s in job_detail)
        similar_skills = set1.intersection(set2)

        # print(similar_skills)
        if len(similar_skills) >= 1:
            matched_jobs.append(job)

    # print(f"{len(matched_jobs)} job(s) found: \n {matched_jobs}")
    return matched_jobs


# filtered_jobs(jobs, res_skills)
