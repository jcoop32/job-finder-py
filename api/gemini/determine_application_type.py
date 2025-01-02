import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
from gemini_prompts.determine_application_type import (
    prompt as determine_application_type,
)

# from aws.s3.s3_utilities import get_presigned_url

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)


def application_type(url):
    prompt = determine_application_type(url)
    response = model.generate_content(
        [
            prompt,
        ],
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json", response_schema=bool
        ),
    )
