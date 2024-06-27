from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/car-project")
def car_project():
    return render_template("car-project.html")