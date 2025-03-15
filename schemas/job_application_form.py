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
