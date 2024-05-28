from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField('', validators=[DataRequired(), Email()])
    password = PasswordField('', validators=[DataRequired(), Length(min=8)])
=======
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, Email

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=50)])
    surname = StringField('surname', validators=[DataRequired(), Length(max=50)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
>>>>>>> 30e29ab1e8a26dd5af01760ac400a4df3fda962d
