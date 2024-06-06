from . import subjects_blp
from .forms import CreateSubjectForm
from flask import redirect, render_template
from flask_login import login_required
from .models import Subject

@login_required
@subjects_blp.route('/subjects', methods=['GET', 'POST'])
def create_subject():
    from app.extensions import db
    form = CreateSubjectForm()
    if form.validate_on_submit():
        subject = Subject(title=form.title, description=form.description, start_time = form.start_time, day_of_week=form.day_of_week, repeat_weekly = form.repeat_weekly)
        db.session.add(subject)
        db.session.commit()
        return redirect('/')
    return render_template('createsubject.html', form=form)