from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField('', validators=[DataRequired(), Email()])
    password = PasswordField('', validators=[DataRequired(), Length(min=8)])