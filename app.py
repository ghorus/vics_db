from flask import Flask, render_template, request
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db = SQLAlchemy(app)

class ButtonPress(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   count = db.Column(db.Integer, default=0)
   timestamp = db.Column(db.DateTime, default=datetime.datetime.now())

   def __repr__(self):
       return f"Button Count: {self.count}, Timestamp: {self.timestamp}"

@app.route("/")
def home():
    return render_template("index.html",title="Help")

@app.route('/pushups_tracker')
def project_pushups_tracker():
    return render_template("pushups_tracker.html",title="Keep Track of Pushups")

@app.route('/leetcode_1')
def project_leetcode_1():
    desc = "Unlock the power of hash tables with our comprehensive guide! Dive deep into efficient O(n) solutions for the Two Sum problem, comparing them to O(n^2) brute force approaches. Grasp concepts easily and optimize your coding skills."
    return render_template("leetcode_two_sum.html",title="Leetcode Efficient Solutions: Hash Tables for 1. Two Sum",desc=desc)

@app.route('/canvas_save')
def canvas_save():
    return render_template("canvas_save.html",title="Free, No Download, and Save:Canvas Drawing")

@app.route('/button_counter',methods=['GET','POST'])
def button_counter():
    button_press = ButtonPress.query.order_by(ButtonPress.count.desc()).first()
    if button_press is None:
        button_press = ButtonPress(count=1)
        db.session.add(button_press)
        db.session.commit()

    if request.method == 'POST':
        button_press.count += 1
        db.session.commit()

    return render_template("button_counter.html",title="Button Counter",button_press = button_press)



if __name__ == "__main__":
    app.run(debug=True)