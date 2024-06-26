from app.extensions import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from subjects.models import Subject

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    is_teacher = db.Column(db.Boolean, default=False)
    is_student = db.Column(db.Boolean, default=True)
    is_chief_teacher = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=func.now())
    subjects = db.relationship("Subject", backref="subjects")