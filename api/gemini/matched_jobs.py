import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from gemini_prompts.job_match_prompt import job_prompt

# from aws.s3.s3_utilities import get_presigned_url

from schemas.job_api_schema import JobPosting

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
)


# find good matching jobs with gemini api
def matched_jobs(resume_filename, jobs: list[JobPosting]):
    prompt_func = job_prompt(jobs)
    resume = genai.upload_file(f"resume_uploads/{resume_filename}")
    # resume_file_path = get_presigned_url(resume_filename)
    # resume = genai.upload_file(path=resume_file_path, mime_type="application/pdf")
    response = model.generate_content(
        [
            prompt_func,
            resume,
        ],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=list[JobPosting]
        ),
    )
    json_form = json.loads(response.text)
    data: list[JobPosting] = json_form
    print(len(data))
    print(type(data))
    print(data)
    return data
