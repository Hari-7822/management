from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from students.models import user

#user views
def user_view(request, username):
    data = get_object_or_404(user, username=username)
    return render(request, 'user_view.j2', {'user': data})

def delete_self(request):
    data = user.objects.delete(username=request.user.username)
    print(request.path)
    return render(request, 'user_delete.j2', {'name': data})

#Settings
@login_required(login_url="user/login")
def info(request):
    return "Info"

@login_required(login_url="user/login")
def perms(request):
    return "Info"

@login_required(login_url="user/login")
def settings(request):
    return "Info"