from django.contrib import admin
from .models import Student
from Users.models import user
from django.contrib.auth.admin import UserAdmin

admin.site.register(user, UserAdmin) 
admin.site.register(Student)
