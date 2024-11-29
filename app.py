from flask import Flask, render_template, request, redirect
from controllers.gemini import get_summary_of_resume, get_person


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/ai", methods=["POST", "GET"])
def ai():
    # if request.method == "POST":
    #     summary_of_resume = get_summary_of_resume()
    #     return redirect("/ai")
    # else:
    summary_of_resume = get_summary_of_resume()
    return render_template("ai.html", res=summary_of_resume)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
