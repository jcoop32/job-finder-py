import requests
import os
from dotenv import load_dotenv
import numpy as np
from controllers.get_location import get_linkedin_location

load_dotenv()

job_api_key = os.getenv("job_api_6")
job_api_key2 = os.getenv("job_api_7")


def search_for_jobs(key_words, location):
    location_id = get_linkedin_location(location)
    url = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"

    querystring = {
        "keywords": key_words,
        "locationId": location_id,
        "datePosted": "past24Hours",
        "jobType": "fullTime, internship",
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


# jobs = search_for_jobs("software engineer", "chicago")


def get_job_details(job_id):
    url = "https://linkedin-data-api.p.rapidapi.com/get-job-details"

    querystring = {"id": job_id}

    headers = {
        "x-rapidapi-key": job_api_key2,
        "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_form = response.json()
    jobs_with_details = []
    details = json_form["data"]
    # return details
    print(details)


# get_job_details("4086033586")


def filtered_jobs(jobs, resume_skills):
    matched_jobs = []
    for job in jobs:
        skills_from_job = get_job_details(job["id"])
        if skills_from_job["skills"]:
            similar_skills = np.intersect1d(
                str(resume_skills).lower(), str(skills_from_job["skills"]).lower()
            )
            if len(similar_skills) >= 3:
                matched_jobs.append(job)

    print(matched_jobs)


res_skills = [
    "Node.js",
    "TypeScript",
    "NestJS",
    "Next.js",
    "Java",
    "Python",
    "HTML",
    "CSS",
]

# filtered_jobs(jobs, res_skills)
