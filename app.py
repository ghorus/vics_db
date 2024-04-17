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

@app.route('/leetcode_1')
def project_leetcode_1():
    desc = "Unlock the power of hash tables with our comprehensive guide! Dive deep into efficient O(n) solutions for the Two Sum problem, comparing them to O(n^2) brute force approaches. Grasp concepts easily and optimize your coding skills."
    return render_template("leetcode_two_sum.html",title="Leetcode Efficient Solutions: Hash Tables for 1. Two Sum",desc=desc)


if __name__ == "__main__":
    app.run(debug=True)