from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", content = ["AI", "ML", "DS", "Python"])

if __name__ == "__main__":
    app.run(debug=True)