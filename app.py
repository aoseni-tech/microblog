from datetime import datetime, timezone
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import dotenv_values

app = Flask(__name__)
config = dotenv_values(".env")
client = MongoClient(config["DB_URL"])

entries = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("entry")
        date_posted = datetime.now(tz=timezone.utc)
        local_date = date_posted.astimezone()
        entries.append((entry_content, local_date))
    return render_template("home.html", entries=entries)