import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

from schemas.job_application_form import FormStructure
from gemini_prompts.get_application_form_structure_prompt import get_form_prompt

# from aws.s3.s3_utilities import get_presigned_url

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
)


def application_form(url, resume_data):
    prompt = get_form_prompt(url, resume_data)
    response = model.generate_content(
        [
            prompt,
        ],
        generation_config=genai.GenerationConfig(response_mime_type="application/json"),
    )
    json_form = json.loads(response.text)
    data: FormStructure = json_form
    new_data = json.dumps(data)
    print(type(new_data))
    return data


# print(application_form("https://tally.so/r/wQJKRY"))
# print(
#     application_form(
#         "https://underdog.io/candidates/apply?idealrole=software-engineer&utm_medium=jobpost&utm_source=linkedin&utm_campaign=candidates-apply&utm_content=full-stack-sofware-engineer"
#     )
# )

# print(
#     application_form(
#         "https://job-boards.greenhouse.io/reddit/jobs/6365165?gh_src=8a8a4d8a1us"
#     )
# )

# print(application_form("https://boards.greenhouse.io/tempus/jobs/7722351002"))
