def is_application_submit(url):
    prompt_with_url = f"""
    You are a program designed to analyze the structure of online job application forms. You need to determine whether a given form is a "single-page form" or a "multi-page form" and return a boolean value (`true` or `false`) as your output.

**Here's how to define these terms:**

*   **Single-Page Form:** The entire job application is presented on a single, continuous page. The user can scroll through all the questions and fields without clicking "Next" or similar buttons to advance to a new page. The form will have a single "Submit," "Apply," or similarly named button, usually at the end, that **submits the data using a POST request.** Return `true` in this case.
*   **Multi-Page Form:** The job application is divided into multiple sections, each presented on a separate page. The user must click a "Next" or similar button to move from one page to the next. Each page may have its own submission-like button (e.g., "Save and Continue"), but ultimately the user will fully submit the job application at the end of the last page. **An "Apply" or "Apply Now" button that initiates a GET request (loads a new URL) to a different website is a strong indicator of a multi-page form.** Return `false` in this case.
*   **Unknown:** If the form's structure cannot be definitively classified as either single-page or multi-page based on these criteria, return `false`.

**Special Rules:**

*   **True (Single-Page):** If the URL of the job application page originates from one of the following domains, automatically classify it as a **single-page form** and return `true` without further analysis:
    *   `jobs.ashbyhq.com`
    *   `boards.greenhouse.io`
    *   `underdog.io`
*   **False (Multi-Page):** If the URL of the job application page **OR the URL an "Apply," "Apply Now," or similar button redirects to** contains the following domain, automatically classify it as a **multi-page form** and return `false` without further analysis:
    *   `myworkdayjobs.com`

**Website to Analyze:** {url}

**Analysis Steps (Only if the URL does not match the domains in the Special Rules):**

1.  **Initial Assessment:**
    *   If the URL matches the domains in the Special Rules, return the corresponding boolean value (`true` or `false`) immediately.
    *   Otherwise, proceed to the next steps.

2.  **"Apply" Button Analysis:**
    *   Check if the page has buttons labeled "Apply," "Apply Now," or similar (e.g., "Start Application").
    *   **Determine the Destination URL:** If possible, determine the URL that the "Apply" button links to. This might involve:
        *   **Inspecting the button's `<a>` tag:** If it's an `<a>` (anchor) tag, check its `href` attribute. This attribute will contain the destination URL.
    *   **Check if Destination is a Different Website:**
        * If the destination URL's domain is **different** from the initial page's domain classify the form as **multi-page** and return `false`.
    *   **Check Destination Against "False" Domains:** If the destination URL contains `myworkdayjobs.com`, classify the form as **multi-page** and return `false`.
    *   **Determine the Request Type:** If the destination URL is not in our list of false domains, try to determine whether clicking the "Apply" button would trigger a `GET` or a `POST` request by:
        *   **Looking for `<form>` tag:** If the button is inside a `<form>` tag, check the `method` attribute of the form. If it's `method="POST"`, then it is most likely a `POST` request.
        *   **If no `<form>` tag with `method="POST"` is found:** If there is no form tag, then it is most likely a `GET` request.

    *   **If the "Apply" button initiates a GET request (loads a new URL) to the same domain not caught in our special rules:** Classify the form as **multi-page** and return `false`.
    *   **If the "Apply" button initiates a POST request (submits data):** This suggests a single-page form, but proceed with further analysis to confirm.
    *   **If there is no "Apply" button or if its destination or request type cannot be determined:** Proceed with the remaining analysis steps.

3.  **Navigation:** Check if the user needs to click any "Next," "Previous," "Back," "Continue," or similarly labeled buttons to access different sections of the application.

4.  **Form Structure:** Determine if the entire application is visible on one page (allowing for scrolling), or if it's broken down into distinct pages or steps.

5.  **Submit Button(s):** If a final "Submit" or "Apply" button is found (other than the initial "Apply" button analyzed in Step 2), check if there are multiple buttons that appear to save or submit portions of the form, or if there's only one main "Submit," "Apply," or equivalent button at the end of the application.

6.  **Progress Indicator:** Look for a progress bar or indicator of steps. Determine if it suggests a single, continuous form or a sequence of separate pages.

**Output:**

Based on your analysis, return one of the following boolean values:

*   `true` if the form is a single-page form.
*   `false` if the form is a multi-page form or if the structure is unknown or ambiguous.

**Provide only the boolean value (`true` or `false`) as your response. Do not include any explanations or reasoning.**

    """
    print(f"url from company: {url}")
    return prompt_with_url
