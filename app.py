from flask import Flask, render_template, request, redirect, url_for
from api.gemini import get_summary_of_resume, matched_jobs
from api.job_search import search_for_jobs_without_location
from api.get_location import get_linkedin_location
import os


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "resume_uploads"

filename = ""
outer_jobs = []


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            global filename
            filename = file.filename
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(
                url_for("ai"),
            )

    return render_template("index.html")


@app.route("/ai")
def ai():
    data, location, skills = get_summary_of_resume(filename)
    # location_id = get_linkedin_location(location)
    jobs = search_for_jobs_without_location(skills)
    global outer_jobs
    outer_jobs = jobs
    # test_prompt = matched_jobs(filename, jobs)
    # print(test_prompt)
    return render_template(
        "ai.html", res=data, jobs=jobs, filename=filename, count=len(jobs)
    )


@app.route("/gemini")
def gemini():
    filtered_jobs = matched_jobs(filename, outer_jobs)
    return render_template("gemini.html", jobs=filtered_jobs, count=len(filtered_jobs))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
