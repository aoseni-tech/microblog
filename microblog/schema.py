from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField
from wtforms.validators import InputRequired, Length
from datetime import datetime

class EntryForm(FlaskForm):
    content = TextAreaField(validators=[Length(min=20)])
    first_name = StringField(validators=[InputRequired()])
    last_name = StringField(validators=[InputRequired()])
    date_posted = DateTimeField(default=datetime.now)