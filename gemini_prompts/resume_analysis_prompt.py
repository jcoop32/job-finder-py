prompt = """
I have a resume that I want you to analyze. Please follow these steps carefully to extract the information:

Step 1: Identify the Candidate

    First Name: Find the candidate's first name.
    Last Name: Find the candidate's last name.
    Name: Find the candidate's full name.
    Location: Determine their city or state (or country, if provided) (ex. Chicago, California, Miami, etc.). If both state and city are present, pick the city.
    Email Address: Extract the candidate's email address.
    Phone Number: If provided, extract the candidate's phone number (xxx-xxx-xxxx).
    LinkedIn Profile URL: If provided, extract the URL of the candidate's LinkedIn profile.

Step 2:  Analyze their Current or Most Recent Role

    Current Job Title (or Most Recent): Identify the title of their current or most recent position.

Step 3: Summarize Past Experience

    Past Experience Summary: For each job listed in their work history:
        Provide the job title, company name, and dates of employment.
        Write a concise summary of their responsibilities and achievements in that role (e.g., 'Managed a team of 5 developers, delivered 3 major projects on time and within budget, and increased user engagement by 15%').
        Extract and list any relevant skills and keywords associated with that position (e.g., project management, data analysis, customer service).

Step 4: Compile a Skills List

    Skills: Grab the 12 most relevant skills mentioned throughout the resume (e.g., technical skills, software proficiency, languages).

Step 5: Suggest Potential Job Titles

    Suggested Job Titles: Based on the information you've gathered from the resume, suggest 3 job titles that you think would be a suitable match for this candidate.

Step 4: Resume Summary

    Resume Summary: If there does not seem to be a resume summary already, Write a very short (no more than three lines) and impactful summary of the candidate's overall qualifications and experience based on the information in the resume.
"""
