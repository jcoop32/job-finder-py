from flask import Flask, render_template, request, redirect, url_for
from controllers.gemini import get_summary_of_resume
from controllers.job_search import search_for_jobs
import os


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "resume_uploads"

filename = ""


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


@app.route("/ai", methods=["POST", "GET"])
def ai():
    json_form, location, keywords = get_summary_of_resume(filename)
    jobs = search_for_jobs(keywords, location)
    return render_template("ai.html", res=json_form, jobs=jobs, filename=filename)


# @app.route("/job-results", methods=["GET"])
# def jobs():
#     _, location, keywords = get_summary_of_resume()

#     print(jobs)
#     return render_template("job-results.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
