from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=50)])
    surname = StringField('surname', validators=[DataRequired(), Length(max=50)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])

    def validate_email(form, field):
        from .models import User
        from werkzeug.security import check_password_hash

        user = User.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError('Invalid email')
        
        
    def validate_password(form, field):
        from .models import User
        from werkzeug.security import check_password_hash

        user = User.query.filter_by(email=form.email.data).first()

        if user and not check_password_hash(user.password, field.data):
            raise ValidationError('Invalid password')
