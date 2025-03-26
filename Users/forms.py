from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

from .models import user, UserDeleteLog, preferences
from API.modelSerializer import UserSerializer

class SignupForm(UserCreationForm):
    username=forms.CharField(max_length=50)
    Image=forms.ImageField(allow_empty_file=True, required=False)
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_superuser','is_staff']
        exclude = ['image', 'groups', 'user_permissions', 'date_joined', 'last_login']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Fieldset('password').css_class('fa fa-eye')   
        )


class LoginForm(AuthenticationForm):
    class Meta:
        model = user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Create User'))
    
    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        if not valid:
            return False

        serializer = UserSerializer(data=self.cleaned_data)
        return serializer.is_valid() 


class UserDeletionForm(forms.Form):
    confirmation = forms.BooleanField(label="Remove User")
        
    class Meta:
        model= UserDeleteLog

    def __str__(self):
        print(f"{self.user.username} has been deleted")

class PreferenceForm(forms.Form):

    class Meta:
        model=preferences
        fields=('__all__')


class ChangePasswordForm(forms.Form):
    
    current_password=forms.CharField(label='current_password',widget=forms.PasswordInput(attrs={'placeholder':'Your Current Password'}))
    new_password=forms.CharField(label='new_password',widget=forms.PasswordInput(attrs={'placeholder':'Your New Password'}))
    new_password_confirmation=forms.CharField(label='new_password_confirmation',widget=forms.PasswordInput(attrs={'placeholder':'Your New Password Again'}))

    class Meta:
        model=user
        fields=('username', 'password')

    def is_valid(self, request, instance):
        Current= True if make_password(self.current_password) == instance.user.password else False
        New= True if self.new_password == self.new_password_confirmation else False

        return True