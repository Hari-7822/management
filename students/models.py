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
    ROLE_CHOICES = [
        (True, 'SuperUser'),
        (False, 'Staff'),
    ]
    
    Role = models.BooleanField(choices=ROLE_CHOICES, default=False)

    def __str__(self):
        return f'User - {self.username}'

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    grade= models.CharField(max_length=6, choices=grade)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class preferences(models.Model):
    user=models.ForeignKey