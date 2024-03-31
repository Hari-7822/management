from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student

@login_required(login_url='/login/')
def index(request):
    stu=Student.objects.all()
    return render(request, 'index.j2', {'stu':stu})