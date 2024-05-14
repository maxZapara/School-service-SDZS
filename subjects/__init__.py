from flask import Blueprint

subjects_blp = Blueprint('subjects', __name__)

from .routes import *