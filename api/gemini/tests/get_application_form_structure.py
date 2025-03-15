import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# from schemas.job_application_form import FormStructure
# from gemini_prompts.get_application_form_structure_prompt import get_form_prompt

# from aws.s3.s3_utilities import get_presigned_url

load_dotenv()

import typing_extensions as typing


class SelectOption(typing.TypedDict):
    """Represents a single option within a <select> field."""

    value: str


class FormField(typing.TypedDict):
    """Represents a single field within the job application form."""

    name: str  # The 'name' attribute of the field
    type: str  # The 'type' attribute (e.g., "text", "email", "select")
    required: bool  # True if the field is required, False otherwise
    value: str  # The default 'value' attribute, or inner text for textarea
    options: typing.Optional[
        typing.List[SelectOption]
    ]  # List of options (for select fields only)
    label: typing.Optional[str]  # The associated label text (for select fields only)


class FormStructure(typing.TypedDict):
    """Represents the overall structure of a job application form."""

    url: str  # The URL of the page containing the form
    action: str  # The URL where the form data is submitted
    method: str  # The HTTP method ("GET" or "POST")
    enctype: str  # The encoding type (e.g., "application/x-www-form-urlencoded")
    fields: typing.List[FormField]  # A list of FormField dictionaries


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
)
res_data = {
    "current_job_title": "Software Engineer Intern",
    "email": "joshuacooper332@gmail.com",
    "first_name": "Joshua",
    "full_name": "Joshua Jamal Mitt Cooper",
    "last_name": "Cooper",
    "linkedin_profile": "linkedin.com/in/joshuacooper11",
    "location": "Chicago",
    "past_experience": [
        {
            "company": "Vail Systems",
            "dates": "Jun. 2024 - Aug. 2024",
            "job_title": "Software Engineer Intern",
            "skills_and_keywords": [
                "Node.js",
                "Typescript",
                "NestJS",
                "Next.js",
                "GraphQL",
                "SCSS",
                "API development",
                "UI development",
                "backend development",
                "database integration",
                "IVR systems",
                "Telekit",
                "Text-to-Speech",
                "SMS notifications",
                "Square API",
                "FreeClimb API",
                "AWS Polly",
                "user interface design",
                "data pagination",
                "real-time insights",
                "appointment and order management",
                "self-service",
            ],
            "summary": "Worked with fellow interns to create a new Live Calls feature for the Telekit Interactive Voice Response (IVR) system. Built the backend API and UI for this feature, ensuring fast response times and integrating data pagination.  Also, developed an appointment and order management IVR feature, integrating with various APIs for different functionalities (payments, SMS notifications, etc.). Created user-friendly draggable components.",
        }
    ],
    "skills": [
        "Node.js",
        "TypeScript",
        "Next.js",
        "GraphQL",
        "SCSS",
        "API Development",
        "UI Development",
        "Backend Development",
        "Database Integration",
        "IVR Systems",
        "Java",
        "Python",
        "HTML",
        "CSS",
        "Git",
        "AWS",
        "Agile Development",
        "React",
        "PostgreSQL",
        "MongoDB",
        "Jest",
    ],
    "suggested_job_titles": [
        "Software Engineer",
        "Full-Stack Developer",
        "Web Developer",
    ],
    "summary": "Highly motivated Computer Science senior with internship experience in software engineering, focusing on full-stack development for telecommunication IVR systems.  Proficient in various programming languages and frameworks, adept at building APIs and user interfaces, and eager to contribute to a software engineering team.",
}


def application_form(url, resume_data):
    # prompt = get_form_prompt(url)
    prompt = f"""You are an expert in web scraping, HTML analysis, and data input. I need you to perform a two-part task:

**Part 1: Form Structure Extraction**

First, extract the structure of a job application form from a given website and represent it in a clear and structured way.  **Focus only on the required fields.**

**Website URL:** {url}

**Resume Data:** {resume_data}

**Task (Part 1):**

1.  **Fetch the HTML:** Retrieve the HTML content of the provided webpage.

2.  **Identify the Form:** Locate the HTML `<form>` element that represents the job application form.  If multiple `<form>` elements exist, focus on the one that appears to be the main job application form (consider context, labels, and the presence of typical application fields).  If no form is found, state "No job application form found."

3.  **Extract Form Details:**  If a form is found, extract the following information:

    *   **Form URL:** The full URL of the page containing the form.
    *   **Action:** The URL where the form data is submitted (the `action` attribute of the `<form>` tag). If the `action` is relative, provide the absolute URL.
    *   **Method:** The HTTP method used to submit the form (the `method` attribute of the `<form>` tag).  This should be either "GET" or "POST" (case-insensitive). If not specified, assume "GET".
    *   **Enctype:** The encoding type of the form (the `enctype` attribute of the `<form>` tag). If not specified, assume "application/x-www-form-urlencoded".

4.  **Extract Required Field Details:** For *each* **required** input field within the form (including `<input>`, `<select>`, and `<textarea>` elements), extract the following:  *Only include fields that have the `required` attribute.*

    *   **Name:** The `name` attribute of the field.
    *   **Type:** The `type` attribute of the field (e.g., "text", "email", "password", "checkbox", "radio", "file", "hidden", "submit", "select", "textarea").  If the field is a `<textarea>`, the type should be "textarea". If it's a `<select>`, the type should be "select".
    *   **Required:** A boolean value (`true`).  (Since we're only dealing with required fields.)
    *   **Value:**  **Initially, set this to the default `value` attribute of the field, if present, or an empty string if no default value is provided in the HTML.  For textareas, use the initial inner text.  This will be updated in Part 2.**
    *   **Options (for select fields only):** If the field is a `<select>` element, provide a list of the `value` attributes of its `<option>` elements. If an `<option>` does not have a `value` attribute, use its text content.
    *   **Label (for select fields only):** If the field is a  `<select>` element, attempt to find the associated label text and include it as a "label" field. If no label can be reliably found, set "label" to `null`.

**Part 2: Data Population**

Second, use the provided **Resume Data** (in JSON format) to fill in the `value` fields of the extracted form structure.  Match resume data to form fields based on the field's `name` and `type`.

*   **Matching Logic:**  Use a best-effort approach to map resume data to form fields.  For example:
    *   A resume field named "firstName" should map to a form field with `name` containing "first_name" (case-insensitive and allowing for variations like underscores, camel case, etc.).
    *   A resume field named "email" should map to a form field with `type="email"`.
    *   If a direct match isn't found, try to infer the mapping based on context and common field names.
    *   For file uploads (`type="file"`), use a placeholder string like "RESUME_FILE_PATH" or "COVER_LETTER_FILE_PATH" in the `value` field.  Do *not* attempt to include actual file content.
    *   For `<select>` fields, choose the most appropriate option from the `options` list based on the resume data. If no suitable option is found, leave the `value` as the default (likely an empty string).

**Output Format:**

Present the *final*, data-populated form structure in a JSON format, as follows:

```json
{{
  "url": "...",
  "action": "...",
  "method": "...",
  "enctype": "...",
  "fields": [
    {{
      "name": "...",
      "type": "...",
      "required": true,
      "value": "...", // Populated from resume data
      "options": ["...", "..."], // Only for select fields
      "label": "..." // Only for select fields, may be null
    }},
    {{
      "name": "...",
      "type": "...",
      "required": true,
      "value": "..."  // Populated from resume data
    }},
    ...
  ]
}}

If no form is found, return the string "No job application form found."  If a form is found, but there are no *required* fields, return an empty `fields` array: `{{"url": "...", "action": "...", "method": "...", "enctype": "...", "fields": []}}`

**Important Considerations:**

*   Only give the JSON as your response.
*   Do not include extra text besides the JSON object.
*   **Handle Relative URLs:** If the `action` attribute contains a relative URL, convert it to an absolute URL based on the page's URL.
*   **Default Values:**  Use default values for `method` ("GET") and `enctype` ("application/x-www-form-urlencoded") if they are not explicitly specified in the `<form>` tag.
*   **Focus on Relevant Attributes:**  Only extract the attributes specified above. Ignore other attributes like `class`, etc., unless they are directly relevant to determining the form structure (as with finding labels for selects).
*   **Label Association:**  Be as accurate as possible in associating labels with their corresponding `<select>` elements, but prioritize getting the correct field data even if a label cannot be confidently identified.
*   **Required Fields Only:** The output JSON should *only* contain information about fields that have the `required` attribute.

"""
    response = model.generate_content(
        [
            prompt,
        ],
        generation_config=genai.GenerationConfig(response_mime_type="application/json"),
    )
    json_form = json.loads(response.text)
    data: FormStructure = json_form

    return data


# print(application_form("https://tally.so/r/wQJKRY"))
# print(
#     application_form(
#         "https://underdog.io/candidates/apply?idealrole=software-engineer&utm_medium=jobpost&utm_source=linkedin&utm_campaign=candidates-apply&utm_content=full-stack-sofware-engineer"
#     )
# )

# print(
#     application_form(
#         "https://job-boards.greenhouse.io/reddit/jobs/6365165?gh_src=8a8a4d8a1us",
#         res_data,
#     )
# )

# print(application_form("https://boards.greenhouse.io/tempus/jobs/7722351002"))


# print(
#     application_form("https://boards.greenhouse.io/udacity/jobs/7791911002", res_data)
# )
