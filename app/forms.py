from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Student

class SignupForm(UserCreationForm):
    options = (
        ("Admin", "Admin"),
        ("Staff","Staff")
    )
    role=forms.ChoiceField(widget=forms.RadioSelect, choices=options)
    class Meta(UserCreationForm.Meta):
        model=User
        fields=["username","role"]



class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username', 'password']

class mod(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        