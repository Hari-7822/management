from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash 
from django.http import HttpResponseNotAllowed
from django.contrib import messages

from Users.models import user
from Users.forms import LoginForm, SignupForm, ChangePasswordForm

def UserSignup(request):
    if request.method == 'POST':
            form = SignupForm(request.POST) 
            if form.is_valid():
                form.save()
                return redirect('UserLogin')
    else:
        form = SignupForm()
    return render(request, 'forms/signup.j2', {'form': form})


def UserLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  
        if form.is_valid():
            name = form.cleaned_data['username']
            print(name)
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('')
    else:
        form = LoginForm()

    return render(request, './forms/login.j2', {'form': form})


def DeleteUser(request, target_user):
    if request.method == "DELETE":
        if target_user == request.user:
            target=user.objects.get(username=request.user.username)
            target.delete()
        elif target_user:
            target=user.objects.delete(usernme=target_user)
            target.delete()
    else:
        return HttpResponseNotAllowed(f"{request.method} method not allowed")
    


def ChangePassword(request):
    if request.method == "PATCH":
        form = ChangePasswordForm()
        if form.is_valid():
            inst= form.save()
            update_session_auth_hash(request, inst)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')