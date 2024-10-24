from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Student, user, grade

class SignupForm(UserCreationForm):
    ROLE_CHOICES = [
        (False, 'Staff'),
        (True, 'Superuser'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect, initial=False)

    class Meta:
        model = user
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create User'))


class LoginForm(AuthenticationForm):
    class Meta:
        model = user
        # fields = ['username', 'password']

class StudentForm(forms.Form):
    name=forms.CharField(max_length=255)
    age = forms.IntegerField()
    grade=forms.ChoiceField(choices=grade, widget=forms.Select())  

    class Meta:
        model = Student
        fields=["name","age", "grade"]

