from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from students.forms import LoginForm, SignupForm

def user_signup(request):
    if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                # name=form.cleaned_data['username'] 
                form.save()
                return redirect('user_login')
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
                return redirect('')
    else:
        form = LoginForm()

    return render(request, './forms/login.j2', {'form': form})