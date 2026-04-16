from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/today")
def today():
    now = datetime.now()
    year  = str(now.year)   # 取得年份 
    month = str(now.month)  # 取得月份 
    day   = str(now.day)    # 取得日期 
    now = year + "年" + month + "月" + day + "日"
    return render_template("today.html", datetime = now)

@app.route("/holand")
def holand():
    return render_template("holand.html")

@app.route("/bio")
def bio():
    return render_template("bio.html")

if __name__ == "__main__":
    app.run()
