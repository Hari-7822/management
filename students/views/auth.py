from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, views

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
                    user.is_staff=False
                elif option=='staff':
                    user.is_superuser=False
                    user.is_staff=True
                if not user.objects.filter(username=name):
                    user.save()
                else:
                    messages.error(request, f'Username ${name} already Exists! \nTry Again with new Username')
                return redirect('list')  # Change to your desired redirect URL
    else:
        form = SignupForm()
    return render(request, 'forms/signup.j2', {'form': form})

class LoginView(views.LoginView):
    pass


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            print

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
 



