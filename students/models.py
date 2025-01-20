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
    def __str__(self):
        return f'{self.username}'
    def __repr__(self):    
        return f'User - {self.username}'

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    grade= models.CharField(max_length=6, choices=grade)
    roll_number = models.CharField(max_length=7, unique=True, null=True,blank=True)

    father_name= models.CharField(max_length=255)
    father_age= models.IntegerField()
    father_occupation=models.CharField(max_length=255)
    mother_name= models.CharField(max_length=255)
    mother_age= models.IntegerField()
    mother_occupation=models.CharField(max_length=255)

    # siblings = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    Created_At = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(user, related_name= "user", on_delete= models.CASCADE)

    
    def __str__(self):
        return f'Student - {self.name} of class {self.grade}'


class preferences(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    theme=models.CharField(max_length=122)



class UserBin(user):
    pass

class StudentBin(Student):
    pass

class UserDeleteLog(user):
    pass