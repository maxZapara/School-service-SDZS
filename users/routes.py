from . import user_blp
from .forms import RegistrationForm
from flask import redirect, render_template

@user_blp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('autorization/sign_up/signup.html', form=form)