import requests


def submit_application(url, data):
    print(data)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",  # Adjust if needed
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # Add other headers as necessary.  Inspect the headers in your browser's
        # Network tab when submitting the form manually.
    }
    try:
        response = requests.post(url=url, data=data, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        raise
