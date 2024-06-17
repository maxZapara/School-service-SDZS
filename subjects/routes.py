from . import subjects_blp
from .forms import CreateSubjectForm, MaterialForm
from flask import redirect, render_template
from flask_login import login_required, current_user
from flask_login import login_required, current_user
from .models import Subject, Material, MaterialFile
import os

@login_required
@subjects_blp.route('/subjects', methods=['GET', 'POST'])
def create_subject():
    if not current_user.is_teacher:
        return redirect('/')

    from app.extensions import db
    form = CreateSubjectForm()
    if form.validate_on_submit():
        subject = Subject(title=form.title.data, description=form.description.data, teacher_id=current_user.id, start_time = form.start_time.data, day_of_week=form.day_of_week.data, repeat_weekly = form.repeat_weekly.data)
        db.session.add(subject)
        db.session.commit()
        return redirect('/')
    return render_template('createsubject.html', form=form)

@login_required
@subjects_blp.route('/subjects/<int:subject_id>/materials', methods=['GET', 'POST'])
def create_material(subject_id):
    # if not current_user.is_teacher:
    #     return redirect('/')

    from app.extensions import db
    form = MaterialForm()
    if form.validate_on_submit():
        material = Material(title=form.title.data, subject_id=subject_id)
        db.session.add(material)
        db.session.commit()

        for file in form.files.data:
            if file:
                print(file)
                filename = file.filename
                filepath = os.path.join("./material_files", filename)
                file.save(filepath)
                material_file=MaterialFile(file=filepath, material_id=material.id)
                db.session.add(material_file)

        db.session.commit()
        return redirect('/')
    return render_template('creatematerial.html', form=form, subject_id=subject_id)