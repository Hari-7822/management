from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate 
from django.core.validators import RegexValidator

from .forms import LoginForm, SignupForm


#validators
def validator():
    roll_number= RegexValidator('[]')

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.j2')

def login(request):
    if request.method=="POST":
        form= LoginForm(request, data=request.POST)
        if form.is_valid():
            name=form.cleaned_data.GET['username']
            passkey=form.cleaned_data.GET['password']
            user= authenticate(request, username=name, password=passkey)

            if user is not None:
                return redirect('index')
            else:
                return "Auth_Error"
            
        else:
            return "Form is not valid"
    else:
        form = LoginForm()

    return render(request, 'forms/login.j2', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = SignupForm()

    return render(request, 'forms/signup.j2', {'form': form})
