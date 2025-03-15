import typing_extensions as typing


class PastExperience(typing.TypedDict):
    # Represents a past job experience entry.
    job_title: str
    company: str
    dates: str
    summary: str
    skills_and_keywords: list[str]


class ResumeAnalysis(typing.TypedDict):
    # Represents the overall analysis of the resume
    first_name: str
    last_name: str
    full_name: str
    email: str
    phone: str
    linkedin_profile: str
    location: str
    current_job_title: str
    past_experience: list[PastExperience]
    skills: list[str]
    suggested_job_titles: list[str]
    summary: str
    resume_filepath: str
