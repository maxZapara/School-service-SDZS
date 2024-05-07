from flask import Blueprint

main_blp= Blueprint('main', __name__)


from .routes import *