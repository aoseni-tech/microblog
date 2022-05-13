from flask import Blueprint, redirect, render_template, request, current_app

# from ..models.entry import entries
from datetime import datetime, timezone

bp = Blueprint("home", __name__)


@bp.route("/", methods=("GET", "POST"))
def hello():
    if request.method == "POST":
        entry_form = request.form.to_dict()
        entry_form["date_posted"] = datetime.now(tz=timezone.utc)
        current_app.db.entries.insert_one(entry_form)
        return redirect(request.url)
    contents = [
        (entry["content"], entry["first_name"], entry["last_name"], entry["date_posted"].astimezone())
        for entry in current_app.db.entries.find()
    ]
    return render_template("home.html", contents=contents)
