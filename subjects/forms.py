from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeLocalField, BooleanField
from wtforms.validators import DataRequired, Length

class CreateSubjectForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=3, max=250)])
    description = StringField('description')
    start_time = DateTimeLocalField('start_time', validators=[DataRequired()])
    day_of_week = StringField('day_of_week', validators=[DataRequired()])
    repeat_weekly = BooleanField('repeat_weekly', validators=[DataRequired()], default=True)