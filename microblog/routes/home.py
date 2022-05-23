from flask import Blueprint, redirect, render_template, request, current_app

bp = Blueprint("home", __name__)

@bp.route("/", methods=("GET", "POST"))
def home():
    form = current_app.entry_form()
    if form.validate_on_submit():
        entry_form = {
            "content": form.content.data,
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "date_posted": form.date_posted.data,
        }
        current_app.db.entries.insert_one(entry_form)
        return redirect(request.url)
    entries = [{'content' : entry['content'], 'date_posted' : entry['date_posted'],  'first_name' : entry['first_name'], 'last_name' : entry['last_name']} for entry in current_app.db.entries.find()]
    
    if request.content_type == "application/json":
        return {
            "entries" : entries,
        }
    return render_template("home.html", entries=entries, form=form)
