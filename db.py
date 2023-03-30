from flask_sqlalchemy import SQLAlchemy
from app import app
from config import *


db = SQLAlchemy(app)


class student(db.model):
    name = db.column("Student Name", db.String(150), nullable = False)
    age = db.column("Age", db.Integer(2), nullable = False)
    std = db.column("Class", db.String(3), nullable = False)
    roll = db.column("Roll number", db.Integer(4), nullable = False)
    register_number = db.column("register number", db.string(6), primary_key = True, nullable = False)
