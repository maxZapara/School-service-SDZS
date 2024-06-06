from flask import Blueprint

subjects_blp = Blueprint('subjects', __name__, template_folder='templates')

from .routes import *