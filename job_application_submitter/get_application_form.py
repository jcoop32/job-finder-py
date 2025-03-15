import requests
from bs4 import BeautifulSoup


def get_form_structure(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        form = soup.find("form")
        # print(f"Form found on {url}:\n{form.prettify()}")
        if form:
            form_data = {
                "url": response.url,
                "action": form.get("action"),
                "method": form.get("method", "POST").upper(),  # Default to GET
                "enctype": form.get("enctype", "application/x-www-form-urlencoded"),
                "fields": [],
            }
            for field in form.find_all(["input"]):
                id = field.get("id")
                name = field.get("name")
                print(f"  Found field: id: {id}, name: {name}")
                if field.has_attr("required") or field.has_attr("aria-required"):
                    print(f"    Field is required.")
                    print("-" * 100)
                    print(field)
                    print("-" * 100)
                    field_data = {
                        "name": field.get("name"),
                        "id": field.get("id"),
                        "type": field.get(
                            "type", "text"
                        ),  # Default to text for textarea
                    }

                    if field_data["type"] != "submit":
                        if field.name == "select":
                            field_data["options"] = [
                                option.get("value", "")
                                for option in field.find_all("option")
                            ]
                        elif field.name == "textarea":
                            field_data["type"] = "textarea"

                        # get default value
                        field_data["value"] = field.get("value", "")
                        if field.name == "textarea":
                            field_data["value"] = field.text

                        form_data["fields"].append(field_data)
            print(form_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# get_form_structure(
#     "https://job-boards.greenhouse.io/reddit/jobs/6365165?gh_src=8a8a4d8a1us"
# )


# get_form_structure(
#     "https://boards.greenhouse.io/tempus/jobs/7722351002?source=LinkedIn"
# )
