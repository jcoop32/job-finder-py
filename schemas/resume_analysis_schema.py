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
    name: str
    email: str
    linkedin_profile: str
    location: str
    current_job_title: str
    past_experience: list[PastExperience]
    skills: list[str]
    suggested_job_titles: list[str]
    summary: str
