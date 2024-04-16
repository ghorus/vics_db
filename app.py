from flask import Flask, render_template, url_for
import socket
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return render_template("index.html",title="Help")

@app.route('/pushups_tracker')
def project_pushups_tracker():
    return render_template("pushups_tracker.html",title="Keep Track of Pushups")

if __name__ == "__main__":
    app.run(debug=True)