from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

class Student(models.Model):
    name=models.CharField(max_length=120)
    age=models.IntegerField(validators=[MaxValueValidator(18), MinValueValidator(4)])


class mod(models.Model):
    name=models.CharField(max_length=120)
    