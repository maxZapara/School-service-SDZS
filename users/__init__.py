from flask import Blueprint

user_blp= Blueprint('users', __name__)

from .routes import *