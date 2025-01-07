from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Student, user, grade

class SignupForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_superuser','is_staff']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create User'))



class LoginForm(AuthenticationForm):
    class Meta:
        model = user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create User'))

class StudentForm(forms.ModelForm):
    name=forms.CharField(max_length=255)
    age = forms.IntegerField()
    grade=forms.ChoiceField(choices=grade, widget=forms.Select())
    father_name= forms.CharField(max_length=255)
    father_age=forms.IntegerField()
    father_occupation= forms.CharField(max_length=255)
    mother_name= forms.CharField(max_length=255)
    mother_age=forms.IntegerField()
    mother_occupation= forms.CharField(max_length=255)

    # siblings = forms.InlineForeignKeyField(name)


    class Meta:
        model = Student
        fields=('__all__')
        exclude=['Created_By', 'Created_At']

    def save(self, commit=True, user=None):
        inst =super().save(commit=False)
        if user:
            inst.Created_By = user
        if commit:
            inst.save()
        return inst
