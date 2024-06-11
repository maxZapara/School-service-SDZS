from app.extensions import db
from sqlalchemy.sql import func

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    day_of_week = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    repeat_weekly = db.Column(db.Boolean, default=True)
    materials = db.relationship("Material", backref="materials")

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    material_files = db.relationship("MaterialFile", backref="material_files")
    
class MaterialFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)
    