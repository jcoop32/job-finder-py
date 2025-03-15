from flask import Flask, render_template, request, redirect, url_for

# gemini
from api.gemini.resume_analysis import get_summary_of_resume
from api.gemini.matched_jobs import matched_jobs
from api.gemini.determine_application_type import application_type
from api.gemini.get_application_form_structure import application_form

# job api
from api.job_search import search_for_jobs_without_location, job_application_url

# job application submitter
from job_application_submitter.submit_job_application import submit_application

# mappings
import mappings.job_search_mapping as job_search_mappings

# from api.get_location import get_linkedin_location

# from job_application_submitter.application_submitter import ApplicationPage, driver

# from aws.s3.s3_utilities import upload_file_to_s3, get_presigned_url
import os


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "resume_uploads"


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        global datePosted
        datePosted = request.form.get("datePosted")
        global jobType
        jobType = request.form.get("jobType")
        global experienceLevel
        experienceLevel = request.form.get("experienceLevel")
        global onSiteRemote
        onSiteRemote = request.form.get("onSiteRemote")
        settings = {
            "datePosted": datePosted,
            "jobType": jobType,
            "experienceLevel": experienceLevel,
            "onsiteRemote": onSiteRemote,
        }
        global job_search_settings
        job_search_settings = settings
        file = request.files["file"]
        if file:
            global filename
            filename = file.filename
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            # try:
            #     upload_file_to_s3(file)
            #     time.sleep(2)
            #     print(get_presigned_url(filename))
            # except:
            #     print("Error uploading file")
            return redirect(
                url_for("ai"),
            )

    return render_template("index.html")


@app.route("/ai")
def ai():
    data, location, skills = get_summary_of_resume(filename)
    global resume_data
    resume_data = data
    global resume_filepath
    resume_filepath = data["resume_filepath"]
    # location_id = get_linkedin_location(location)
    jobs = search_for_jobs_without_location(skills, job_search_settings)
    date_posted = job_search_mappings.date_posted_mapping.get(datePosted)
    job_title = job_search_mappings.job_type_mapping.get(jobType)
    experience_level = job_search_mappings.experience_level_mapping.get(experienceLevel)
    onsite_remote = job_search_mappings.onsiteremote_type.get(onSiteRemote)
    global outer_jobs
    outer_jobs = jobs
    # test_prompt = matched_jobs(filename, jobs)
    # print(test_prompt)
    return render_template(
        "ai.html",
        res=data,
        jobs=jobs,
        filename=filename,
        count=len(jobs),
        dp=date_posted,
        jt=job_title,
        el=experience_level,
        osr=onsite_remote,
    )


@app.route("/gemini")
def gemini():
    filtered_jobs = matched_jobs(filename, outer_jobs)
    return render_template("gemini.html", jobs=filtered_jobs)


@app.route("/job-submitter/<int:job_id>")
def job_app_submitter(job_id):
    print("In job submitter")
    # print(type(resume_data))
    company_application_url = job_application_url(job_id)
    if company_application_url:
        can_submit = application_type(company_application_url)
        job_application_form_structure = application_form(
            company_application_url, resume_data
        )
        send_application = submit_application(
            company_application_url, job_application_form_structure
        )
        if send_application:
            submitted = True
        else:
            submitted = False
    else:
        can_submit = False
    # return str(can_submit)
    # return f"Can use automatic job submitter?: {application.is_one_page_application()} \nAlso {application.find_info_inputs()}"
    return render_template(
        "job-submitter.html",
        can_submit=can_submit,
        form=job_application_form_structure,
        sent=submitted,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)
