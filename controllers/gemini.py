import google.generativeai as genai
from dotenv import load_dotenv
import os
import typing_extensions as typing
import json

from models.gemini_response_schemas import ResumeSummary, JobPosting


load_dotenv()


# data structure gemini returns
# class ResumeSummary(typing.TypedDict):
#     name: str
#     email: str
#     linkedin_profile: str
#     location: str
#     job_title: str
#     skills: list[str]
#     possible_jobs: list[str]
#     summary: str


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)

resume_analysis_prompt = "Pull the name, email, linkedin profile/link (if is given), location (city only), job title, skills, some possible job titles that fit this resume, and a summary from each of the resumes: "
job_match_prompt = "With this JSON of these jobs, return me an array with all the jobs with the best match with the given resume."


def get_summary_of_resume(resume_filename):
    resume = genai.upload_file(f"resume_uploads/{resume_filename}")
    response = model.generate_content(
        [resume_analysis_prompt, resume],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=list[ResumeSummary]
        ),
    )
    # convert data to json
    json_form = json.loads(response.text)
    location = json_form[0]["location"]
    skills = json_form[0]["skills"]
    res_skills = json_form[0]["skills"]
    job_title = json_form[0]["job_title"]
    job_titles = json_form[0]["possible_jobs"]
    list(skills).append(job_title)
    list(skills).append(job_titles)
    return json_form, location, skills, res_skills


# find good matching jobs with gemini api
def matched_jobs(resume_filename, jobs):
    print("in filtered jobs func")
    resume = genai.upload_file(f"resume_uploads/{resume_filename}")
    response = model.generate_content(
        [
            f"For each element of jobs in this array: {jobs}, find the jobs that are matches to this resume and remove the ones that are not matches. Use the resume's job title, possible job titles, skills, and experience to make your decision. Make sure each job follows the response_schema given.",
            resume,
        ],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=list[JobPosting]
        ),
    )

    json_form = json.loads(response.text)
    # print(json_form)
    print(len(json_form))
    print(type(json_form))
    return json_form
