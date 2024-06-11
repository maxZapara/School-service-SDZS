from . import subjects_blp
from .forms import CreateSubjectForm
from flask import redirect, render_template
from flask_login import login_required, current_user
from .models import Subject

@login_required
@subjects_blp.route('/subjects', methods=['GET', 'POST'])
def create_subject():
    from app.extensions import db
    form = CreateSubjectForm()
    if form.validate_on_submit():
        subject = Subject(title=form.title.data, description=form.description.data, teacher_id=current_user.id, start_time = form.start_time.data, day_of_week=form.day_of_week.data, repeat_weekly = form.repeat_weekly.data)
        db.session.add(subject)
        db.session.commit()
        return redirect('/')
    return render_template('createsubject.html', form=form)