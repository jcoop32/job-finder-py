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
    job_title: str
    skills: list[str]
    possible_jobs: list[str]
    summary: str


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)
# resume_pdf = genai.upload_file("jc-resume-2024-fe.pdf")
# resume_pdf_2 = genai.upload_file("jjmc-resume-2024-fs.pdf")
kayla_resume_pdf = genai.upload_file("kayla_resume.pdf")
kaycee_resume_pdf = genai.upload_file("kc_resume.pdf")

resume_analysis_prompt = "Pull the name, email, linkedin profile/link (if is given), job title, skills, some possible job titles that fit this resume, and a summary from ech of the resumes: "


def get_summary_of_resume():
    response = model.generate_content(
        [resume_analysis_prompt, kayla_resume_pdf, kaycee_resume_pdf],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=list[ResumeSummary]
        ),
    )
    json_form = json.loads(response.text)
    return json_form


# TODO: Find a way to search for jobs with linkedin api or another job site with large db
def get_person():
    profile = linkedin_api.get_profile("joshuacooper11")
    # print(profile)
