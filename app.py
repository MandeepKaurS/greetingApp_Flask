from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "maano123"


@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["GET", "POST"])
def greet():
    flash("Hi " + request.form["txtName"] + "! great to see you!")
    return render_template("response.html")