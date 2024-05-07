from . import main_blp
from flask import render_template

@main_blp.route("/")
def hello_world():
    return render_template('homepage/homepage.html')