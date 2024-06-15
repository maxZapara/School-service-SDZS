from . import main_blp
from flask import render_template

@main_blp.route("/")
def home():
    return render_template('homepage/homepage.html')

@main_blp.route("/students")
def students():
    from users.models import User
    users=User.query.filter_by(is_student = True).all() 
    return render_template('homepage/students.html', users=users)

@main_blp.route("/teachers")
def teachers():
    return render_template('homepage/teachers.html')

@main_blp.route("/student")
def studentspage():
    return render_template('homepage/studentspage.html')

@main_blp.route("/teacher")
def teacherspage():
    from users.models import User
    teachers=User.query.filter_by(is_teacher = True).all() 
    return render_template('homepage/teacherspage.html', techers=teachers)

@main_blp.route("/cratecourse")
def cratecourse():
    return render_template('homepage/addcourse.html')

@main_blp.route("/coursepage/c")
def coursepage():
    return render_template('homepage/coursepage.html')

@main_blp.route("/subjects/a")
def lessonpage():
    return render_template('homepage/lessonpage.html')

