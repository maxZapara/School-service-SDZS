from app.extensions import db
from users.models import User

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    teacher = db.relationship("User", backref="subjects")