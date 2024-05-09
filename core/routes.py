from . import main_blp
from flask import render_template

@main_blp.route("/")
def hello_world():
    return render_template('homepage/homepage.html')

@main_blp.route("/login")
def login():
    return render_template('authorization/sign_in/signin.html')

@main_blp.route("/register")
def register():
    return render_template('authorization/sign_up/signup.html')

