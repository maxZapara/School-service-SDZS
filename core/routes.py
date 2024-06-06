from . import main_blp
from flask import render_template

@main_blp.route("/")
def home():
    return render_template('homepage/homepage.html')

@main_blp.route("/students")
def students():
    return render_template('homepage/students.html')

@main_blp.route("/teachers")
def teachers():
    return render_template('homepage/teachers.html')

@main_blp.route("/student/page")
def studentspage():
    return render_template('homepage/studentspage.html')

@main_blp.route("/teacher/page")
def teacherspage():
    return render_template('homepage/teacherspage.html')

@main_blp.route("/cratecourse")
def cratecourse():
    return render_template('homepage/addcourse.html')

@main_blp.route("/coursepage/c")
def coursepage():
    return render_template('homepage/coursepage.html')

@main_blp.route("/subjects/a")
def lessonpage():
    return render_template('homepage/lessonpage.html')

@main_blp.route("/login")
def login():
    return render_template('authorization/sign_in/signin.html')
