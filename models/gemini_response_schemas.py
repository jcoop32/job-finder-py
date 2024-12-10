import typing_extensions as typing


class ResumeSummary(typing.TypedDict):
    name: str
    email: str
    linkedin_profile: str
    location: str
    job_title: str
    skills: list[str]
    possible_jobs: list[str]
    summary: str


class Company(typing.TypedDict):
    company_id: str
    name: str
    logo_url: str
    url: str


class JobPosting(typing.TypedDict):
    job_id: str
    title: str
    url: str
    company: Company  # Now a nested TypedDict
    location: str
    job_type: str
    benefits: str
