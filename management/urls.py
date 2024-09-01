"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from students.views.auth import signup, login
from students.views.students import *

urlpatterns = []

admin_urls = [
    path('admin/', admin.site.urls),
]

index=[
    path('/', list, name='index'),
    # path('student/', list )
]

forms = [
    path("signup/", signup, name='user_registration'),
    path("login/", LoginView.as_view(template_name="./forms/login.j2"), name='user_login'),
    # path("user/change_username/",),
    # path("user/change_password/",),
]

students = [
    path("student/add",Add_Student, name='add_student'),
    path("student/Edit/",Add_Student, name='add_student'),
    path('list/', list, name='list')
]
temp = [
    path('list/', list, name='list')
]

urlpatterns.extend(admin_urls)
urlpatterns.extend(forms)
urlpatterns.extend(students)
urlpatterns.extend(temp)