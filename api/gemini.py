import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from gemini_prompts.resume_analysis_prompt import prompt as resume_analysis_prompt
from gemini_prompts.job_match_prompt import prompt as job_match_prompt

from schemas.resume_analysis_schema import ResumeAnalysis
from schemas.job_api_schema import JobPosting

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)


def get_summary_of_resume(resume_filename):
    resume = genai.upload_file(f"resume_uploads/{resume_filename}")
    response = model.generate_content(
        [resume_analysis_prompt, resume],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=ResumeAnalysis
        ),
    )
    # convert data to json
    json_form = json.loads(response.text)
    # print(json_form)
    data: ResumeAnalysis = json_form
    location = data["location"]
    skills = data["skills"] + data["suggested_job_titles"] + [data["current_job_title"]]

    return data, location, skills


# find good matching jobs with gemini api
def matched_jobs(resume_filename, jobs: list[JobPosting]):
    print("in filtered jobs func")
    resume = genai.upload_file(f"resume_uploads/{resume_filename}")
    response = model.generate_content(
        [
            job_match_prompt,
            jobs,
            resume,
        ],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=list[JobPosting]
        ),
    )

    json_form = json.loads(response.text)
    data: list[JobPosting] = json_form[0]
    print(data)
    return data
