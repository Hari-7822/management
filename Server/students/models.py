from django.db import models
from django.conf.global_settings import MEDIA_ROOT, STATIC_ROOT, STATIC_URL, MEDIA_URL

from Users.models import user

import os
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

def directory(instance, file):
    if not file:
        file = 'default.jpg'
    return os.path.join(f'{instance.id}/{dir}', file)


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Student Name")
    age = models.IntegerField(verbose_name="Student Age")
    grade = models.CharField(max_length=6, choices=grade, verbose_name="Class")
    image = models.ImageField(upload_to=directory, verbose_name="Student Picture")
    roll_number = models.CharField(max_length=7, unique=True, null=True, blank=True, verbose_name="Student Roll number")
    registration_number = models.CharField(max_length=8, unique=True, null=True, blank=True, verbose_name="Student register number")

    father_name = models.CharField(max_length=255)
    father_age = models.IntegerField()
    father_occupation = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother_age = models.IntegerField()
    mother_occupation = models.CharField(max_length=255)
    
    mode_of_transport = models.CharField(max_length=255, default="own", db_default='own')
    reason = models.CharField(max_length=255, default='NA', db_default='NA')
    
    siblings = models.ManyToManyField(
        'self',
        symmetrical=True,
        blank=True,
        related_name='sibling_set',
        verbose_name="Siblings"
    )

    Created_At = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(user, related_name="created_students", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['grade', 'roll_number']

    def get_siblings(self):
        return Student.objects.filter(
            father_name=self.father_name,
            mother_name=self.mother_name
        ).exclude(id=self.id)

    def has_siblings(self):
        return self.get_siblings().exists()

    def sibling_count(self):
        return self.get_siblings().count()

    def get_sibling_names(self):
        return list(self.get_siblings().values_list('name', flat=True))

    def __str__(self):
        return f"{self.name} - {self.roll_number}"

    def __repr__(self):
        return f'Student - {self.name} of class {self.grade}'


class Fee(models.Model):
    Student_name= models.ForeignKey(Student, on_delete= models.CASCADE, related_name='fees_holder')
    transport_fee= models.DecimalField(decimal_places=2, max_digits=25, default='100', db_default='100')
    book_fee=models.IntegerField(default='10')


class StudentBin(Student):
    pass