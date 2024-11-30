from flask import Flask, render_template, request, redirect
from controllers.gemini import get_summary_of_resume
from controllers.job_search import search_for_jobs


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/ai", methods=["POST", "GET"])
def ai():
    json_form, location, keywords = get_summary_of_resume()
    jobs = search_for_jobs(keywords, location)
    return render_template("ai.html", res=json_form, jobs=jobs)


# @app.route("/job-results", methods=["GET"])
# def jobs():
#     _, location, keywords = get_summary_of_resume()

#     print(jobs)
#     return render_template("job-results.html", jobs=jobs)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
