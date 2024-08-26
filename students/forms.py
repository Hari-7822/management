from django import forms
from django.forms import ModelForm
from .models import Student, user, grade
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class AddUserForm(UserCreationForm):
    ROLE_CHOICES = [('superuser', 'Superuser'),('staff', 'Staff')]
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.CheckboxInput)  

    class Meta:
        model = user
        fields = ['username', 'password', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data['role']
        if role == 'superuser':
            user.is_superuser = True
            user.is_staff = True
        elif role == 'staff':
            user.is_staff = True
            user.is_superuser = False
        elif role == 'superuser' and role == 'staff':
            user.is_superuser = True
            user.is_staff = True
        if commit:
            user.save()
        return user



class LoginForm(AuthenticationForm):
    class Meta():
        model = user
        # fields = ['username', 'password']

class StudentForm(forms.Form):
   
    grade=forms.ChoiceField(choices=grade, widget=forms.CheckboxInput)

    class Meta():
        model = Student
        fields='__all__' 