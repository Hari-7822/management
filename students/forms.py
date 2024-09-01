from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import Student, user, grade

class AddUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

class PasswordResetForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : "Enter your old password"}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : "Enter your new password"}))
    new_password_verify = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : "Enter your new password again"}))

    class meta():
        model = user
        fields = ['old_password', 
                  'new_password',
                  'new_password_verify'
                  ]


class ChangeUsernameForm(forms.Form):
    old_username=forms.CharField(widget=forms.TextInput(attrs={}))
    new_username=forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Your New Username'}))

    class Meta():
        model=user


class StudentForm(ModelForm):

    name=forms.CharField(max_length=255, widget=forms.TextInput())
    age = forms.IntegerField(max_value=18, widget=forms.NumberInput())
    grade=forms.ChoiceField(choices=grade, widget=forms.CheckboxInput())  

    class Meta():
        model = Student
        fields=["name","age","grade"]