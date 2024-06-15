from flask_login import login_required, logout_user
from . import user_blp
from .forms import RegistrationForm, LoginForm
from flask import redirect, render_template, url_for
from .models import User
from werkzeug.security import generate_password_hash

@user_blp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    from app.extensions import db
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, password=generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.sign_in'))
    return render_template('autorization/sign_up/signup.html', form=form)

@user_blp.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    from flask_login import login_user
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        return redirect('/')
    return render_template('autorization/sign_in/signin.html', form=form)

@user_blp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")