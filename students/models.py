from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime


TITLE = [
    "Mr", 'Mr.'
    "Mrs", 'Mrs.'
    "Ms", 'Ms.'
]
grade = [
    ("Pre-KG",'Pre-KG'),
    ("UKG",'UKG'),
    ("LKG",'LKG'),
    ("I",'I'),
    ("II",'II'),
    ("III",'III'),
    ("IV",'IV'),
    ("V",'V'),
    ("VI",'VI'),
    ("VII",'VII'),
    ("VIII",'VIII'),
    ("IX",'IX'),
    ("X",'X'),
    ("XI",'XI'),
    ("XII",'XII'),

]

class user(AbstractUser):
    pass

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    grade= models.CharField(max_length=6, choices=grade)
    CreatedAt = models.DateTimeField(datetime.now, default=datetime.now)
