from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, views, decorators
from .students import index
from students.models import user, Student
from students.forms import UserCreationForm, LoginForm, SignupForm

def user_signup(request):
    if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                name=form.cleaned_data['username']  
                option=form.cleaned_data['role']
                if option == 'superuser':
                    user.is_superuser=True
                    user.is_staff=True
                elif option=='staff':
                    user.is_superuser=False
                    user.is_staff=False
                if not user.objects.filter(username=name):
                    user.save()
                else:
                    messages.error(request, f'Username ${name} already Exists! \nTry Again with new Username')
                return redirect('user/login/')  
    else:
        form = SignupForm()
    return render(request, 'forms/signup.j2', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            print(name)
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, './forms/login.j2', {'form': form})