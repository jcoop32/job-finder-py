def prompt(url):
    prompt_with_url = f"""
    based on this link to this job application, is it a single or multi page job application?
    I would say if there is a button that says something along the lines of submit application, then its a single page job application.
    If single-page application return True, else return False: {url}

    """
    return prompt_with_url
