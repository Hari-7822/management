import os
from app import app

dir = os.path.abspath(os.path.dirname("db"))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(dir, "database.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
