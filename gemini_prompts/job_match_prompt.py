def job_prompt(jobs):
    prompt = f"""
I have a resume and a JSON object containing a list of job postings. I want you to analyze the resume and filter the job postings based on how well they match the candidate's qualifications.

Step 1: Analyze the Resume

    Perform the following analysis on the provided resume:
        Extract key information:
            Skills (technical, software, languages)
            Past job titles and responsibilities
            Career goals or preferred job types (if explicitly stated)
            Suggested Job Titles: Identify any suggested or desired job titles explicitly mentioned in the resume.

Step 2: Filter Job Postings

    Use the information extracted from the resume to evaluate each job posting in the provided JSON object.
    Remove any job postings that are clearly not a good fit for the candidate. Consider factors such as:
        Required skills: Does the candidate possess the necessary skills and experience?
        Job title and responsibilities: Is the job level and type of work aligned with the candidate's career goals?
        Seniority level: Does the candidate's experience match the seniority level of the position? (You can infer this from their work history)
        Job Title Match: Does the job title in the posting seem to align with the candidate's past job titles or any suggested/desired job titles mentioned in the resume?

Step 3: Return Filtered Job Postings

    Return the same JSON object you received, but with the irrelevant job postings removed. The structure of the JSON object should remain unchanged and strictly follow this format (should be a python dictionary returned):


    {{
    "jobs": [
        {{
        "id": "string", // Unique identifier for the job posting
        "title": "string", // Title of the job
        "url": "string", // URL of the job posting
        "referenceId": "string",
        "posterId": "string",
        "company": {{
            "id": "string", // Unique identifier for the company
            "name": "string", // Name of the company
            "logo": "string", // URL to the company logo
            "url": "string" // URL to the company website
        }},
        "location": "string", // Location of the job
        "type": "string", // Type of job (e.g., "Full-time", "Part-time")
        "postDate": "string", // Date the job was posted
        "benefits": "string" // Description of job benefits
        }}
    ]
    }}



    Here is the json of jobs: {jobs}
"""
    return prompt
