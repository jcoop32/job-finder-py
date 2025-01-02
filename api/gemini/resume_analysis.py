import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from gemini_prompts.resume_analysis_prompt import prompt as resume_analysis_prompt

# from aws.s3.s3_utilities import get_presigned_url

from schemas.resume_analysis_schema import ResumeAnalysis

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)


def get_summary_of_resume(resume_filename):
    resume = genai.upload_file(f"resume_uploads/{resume_filename}")
    # resume_file_path = get_presigned_url(resume_filename)
    # resume = genai.upload_file(path=resume_file_path, mime_type="application/pdf")
    response = model.generate_content(
        [resume_analysis_prompt, resume],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=ResumeAnalysis
        ),
    )
    # convert data to json
    json_form = json.loads(response.text)

    data: ResumeAnalysis = json_form
    location = data["location"]
    skills = data["skills"] + data["suggested_job_titles"] + [data["current_job_title"]]

    return data, location, skills
