from flask import Blueprint

user_blp= Blueprint('users', __name__, template_folder="templates")

from .routes import *