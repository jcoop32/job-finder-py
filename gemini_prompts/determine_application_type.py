def is_application_submit(url):
    prompt_with_url = f"""
    You are a program designed to analyze the structure of online job application forms. You need to determine whether a given form is a "single-page form" or a "multi-page form" and return a boolean value (`true` or `false`) as your output.

**Here's how to define these terms:**

*   **Single-Page Form:** The entire job application is presented on a single, continuous page. The user can scroll through all the questions and fields without clicking "Next" or similar buttons to advance to a new page. The form will have a single "Submit," "Apply," or similarly named button, usually at the end, to complete the application. Return `true` in this case.
*   **Multi-Page Form:** The job application is divided into multiple sections, each presented on a separate page. The user must click a "Next" or similar button to move from one page to the next. Each page may have its own submission-like button (e.g. "Save and Continue"), but ultimately the user will fully submit the job application at the end of the last page. Return `false` in this case.
*   **Unknown:** If the form's structure cannot be definitively classified as either single-page or multi-page based on these criteria, return `false`.

**Website to Analyze:** {url}

**Analysis Steps:**

1.  **Navigation:** Check if the user needs to click any "Next," "Previous," "Back," "Continue," or similarly labeled buttons to access different sections of the application.
2.  **Form Structure:** Determine if the entire application is visible on one page (allowing for scrolling), or if it's broken down into distinct pages or steps.
3.  **Submit Button(s):** Check if there are multiple buttons that appear to save or submit portions of the form, or if there's only one main "Submit," "Apply," or equivalent button at the end of the application. It should also be sending a POST request becuase its sending data to a database and not GET request to another page.
4.  **Progress Indicator:** Look for a progress bar or indicator of steps. Determine if it suggests a single, continuous form or a sequence of separate pages.

**Output:**

Based on your analysis, return one of the following boolean values:

*   `true` if the form is a single-page form.
*   `false` if the form is a multi-page form or if the structure is unknown or ambiguous.

**Provide only the boolean value (`true` or `false`) as your response. Do not include any explanations or reasoning.**

    """
    return prompt_with_url
