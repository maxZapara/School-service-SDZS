from flask import render_template
from .forms import LoginForm
from . import user_blp

@user_blp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("d")
    return render_template('sign_in.html', form=form)