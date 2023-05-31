from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("templates/index.html")

@app.route("/greet", methods=["POST"])
def greet():
    return render_template("templates/index_2.html")

if __name__ == "__main__":
    app.run(debug=True)