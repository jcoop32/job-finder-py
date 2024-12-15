import typing_extensions as typing


class Company(typing.TypedDict):
    # Represents a company in the job posting.
    id: str
    name: str
    logo: str
    url: str


class JobPosting(typing.TypedDict):
    # Represents a single job posting.
    id: str
    title: str
    url: str
    referenceId: str
    posterId: str
    company: Company
    location: str
    type: str
    postDate: str
    benefits: str
