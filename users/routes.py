<<<<<<< HEAD
from flask import render_template
from .forms import LoginForm
from . import user_blp

@user_blp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("d")
    return render_template('sign_in.html', form=form)
=======
from . import user_blp
from .forms import RegistrationForm
from flask import redirect, render_template

@user_blp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('autorization/sign_up/signup.html', form=form)
>>>>>>> 30e29ab1e8a26dd5af01760ac400a4df3fda962d
