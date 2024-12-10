import requests
import os
from dotenv import load_dotenv
import time
import functools

from controllers.get_location import get_linkedin_location

# from get_location import get_linkedin_location
from linkedin_api import Linkedin

api = Linkedin("coopj3265@gmail.com", os.getenv("linkedin_pass"))

load_dotenv()

job_api_key = os.getenv("job_api_8")
job_api_key2 = os.getenv("job_api_2")

url1 = "https://linkedin-data-api.p.rapidapi.com/search-jobs-v2"
url2 = "https://linkedin-api8.p.rapidapi.com/search-jobs-v2"
host1 = "linkedin-data-api.p.rapidapi.com"
host2 = "linkedin-api8.p.rapidapi.com"


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute."
        )
        return result

    return wrapper


key_words_list = [
    "Full stack developer",
    "frontend developer",
    "software engineer",
]

location = "103112676"  # chicago


@time_it
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


# @time_it
@functools.lru_cache(maxsize=128)
def job_details(job_id):
    job = api.get_job_skills(job_id)
    job_skills = [skill["skill"]["name"] for skill in job["skillMatchStatuses"][:10]]

    return job_skills
    # print(job_skills)


# job_details("4089332020")


@time_it
@functools.lru_cache(maxsize=128)
def filtered_jobs(keywords, location, resume_skills):
    jobs = search_for_jobs(keywords, location)
    matched_jobs = []
    set1 = set(s.lower() for s in resume_skills)
    # print(len(jobs))
    # if len(jobs) > 3:
    #     jobs = jobs[:5]
    for job in jobs:
        job_detail = job_details(job[0]["id"])
        set2 = set(s.lower() for s in job_detail)
        similar_skills = set1.intersection(set2)

        # print(similar_skills)
        if len(similar_skills) >= 1:
            matched_jobs.append(job)

    # print(f"{len(matched_jobs)} job(s) found: \n {matched_jobs}")
    return matched_jobs


# res_skills = [
#     "Node.js",
#     "TypeScript",
#     "NestJS",
#     "Next.js",
#     "Java",
#     "Python",
#     "HTML",
#     "CSS",
# ]


# cached_res = filtered_jobs(key_words_list, "Chicago", tuple(res_skills))
# print(cached_res)


@time_it
def search_for_jobs_without_location(key_words):
    url = url2
    location = "103112676"  # chicago

    querystring = {
        "keywords": key_words,
        "locationId": location,
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


# search_for_jobs_without_location(key_words_list)
