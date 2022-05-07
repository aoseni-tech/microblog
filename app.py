from flask import Flask, redirect, render_template, request
from datetime import datetime, timezone
from models.entry import entries

blog_app = Flask(__name__)

if __name__ == "__main__":
    @blog_app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            form_post = request.form
            article_entries = {key: form_post.get(key) for key in form_post.keys()}
            article_entries["date_posted"] = datetime.now(tz=timezone.utc)
            entries.insert_one(article_entries)
            return redirect(request.url)
        contents = entries.find()
        return render_template("home.html", contents=contents)
