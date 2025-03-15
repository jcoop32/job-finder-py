import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import typing_extensions as typing

from gemini_prompts.determine_application_type_prompt import is_application_submit

# from aws.s3.s3_utilities import get_presigned_url

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
)


class IsAppSinglePage(typing.TypedDict):
    # Represents a company in the job posting.
    isSinglePage: bool


def application_type(url):
    prompt = is_application_submit(url)
    response = model.generate_content(
        [
            prompt,
        ],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=IsAppSinglePage
        ),
    )
    json_form = json.loads(response.text)
    descision = json_form["isSinglePage"]
    return descision


# print(application_type("https://tally.so/r/wQJKRY"))
# print(
#     application_type(
#         "https://underdog.io/candidates/apply?idealrole=software-engineer&utm_medium=jobpost&utm_source=linkedin&utm_campaign=candidates-apply&utm_content=full-stack-sofware-engineer"
#     )
# )
