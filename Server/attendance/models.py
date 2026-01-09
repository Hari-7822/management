from django.db import models
from students.models import Student

from datetime import date



class AttendanceRecord(models.Model):
    student_name = models.ForeignKey(Student, max_length=100, on_delete=models.CASCADE)
    date = models.DateField(datefault=date.today)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late'), ('half a day', 'half a day')])

    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.status}"