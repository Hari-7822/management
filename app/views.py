from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student

@login_required(login_url='/login/')
def index(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        print('ajax')
    stu=Student.objects.all()
    return render(request, 'index.j2', {'stu':stu})