from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from students.models import user, Student
from students.forms import UserCreationForm, LoginForm 

def signup(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            name=form.cleaned_data['username']
            if form.is_valid():
                if not user.objects.filter(username=name):
                    form.save()
                elif user.objects.filter(username=name):
                    messages.error(request, f'Username ${name} already Exists! \nTry Again with new Username')
                return redirect('list')  # Change to your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'forms/signup.j2', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, './forms/login.j2', {'form': form})



    # if request.method == "POST":
    #     form=UserCreationForm()
    #     name=form.cleaned_data['username']
    #     if form.is_valid:
    #         if not user.objects.filter(username=name):
    #             messages.error(request, f'Username ${name} already Exists! \nTry Again with new Username')
    #         form.save()
    # else:
    #     form = UserCreationForm()

    # return render(request, 'forms/signup.j2', {form:'form'})
 



