from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Hii Naveen </h1>"

@app.route("/study")
def study():
    return "Maters in Data Science"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/<name>")
def name(name):
    return f" Hello {name} "

if __name__ == "__main__":
    app.run()