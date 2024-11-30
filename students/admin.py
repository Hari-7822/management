from django.contrib import admin
from .models import user, Student
from django.contrib.auth.admin import UserAdmin

admin.site.register(user, UserAdmin) 
admin.site.register(Student)
