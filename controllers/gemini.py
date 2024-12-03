import google.generativeai as genai
from dotenv import load_dotenv
import os
import typing_extensions as typing
import json
from linkedin_api import Linkedin


load_dotenv()
linkedin_api = Linkedin("coopj3265@gmail.com", os.getenv("linkedin_pass"))


class ResumeSummary(typing.TypedDict):
    name: str
    email: str
    linkedin_profile: str
    location: str
    job_title: str
    skills: list[str]
    possible_jobs: list[str]
    summary: str


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)
# resume_pdf = genai.upload_file("jc-resume-2024-fe.pdf")

# kayla_resume_pdf = genai.upload_file("kayla_resume.pdf")
# kaycee_resume_pdf = genai.upload_file("kc_resume.pdf")

resume_analysis_prompt = "Pull the name, email, linkedin profile/link (if is given), location (city only), job title, skills, some possible job titles that fit this resume, and a summary from each of the resumes. If only one resume is given do not change the output of the response if prompted with the same resume.: "


def get_summary_of_resume(filename):
    resume = genai.upload_file(f"resume_uploads/{filename}")
    response = model.generate_content(
        [resume_analysis_prompt, resume],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=list[ResumeSummary]
        ),
    )
    json_form = json.loads(response.text)
    location = json_form[0]["location"]
    skills = json_form[0]["skills"]
    job_title = json_form[0]["job_title"]
    list(skills).append(job_title)
    # job_titles = json_form[0]["possible_jobs"]
    un_keywords = skills
    keywords = " ".join(un_keywords)
    return json_form, location, keywords
