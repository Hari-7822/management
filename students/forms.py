from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

from .models import Student, grade
from Users.models import user
from API.modelSerializer import StudentSerializer, UserSerializer

class SignupForm(UserCreationForm):
    Image=forms.ImageField()
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_superuser','is_staff']
        exclude=["image", "groups", "user_permissions", "date_joined", "last_login"]

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
    image= forms.ImageField()

    # siblings = forms.InlineForeignKeyField(name)


    class Meta:
        model = Student
        fields=('__all__')
        exclude=['Created_By', 'Created_At']

    def __init__(self, request, *args, **kwargs):
        user = kwargs.pop('Created_By', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['Created_By'].initial = request.user
            self.fields['Created_By'].widget = forms.HiddenInput()
            self.fields['Created_By'].widget = forms.HiddenInput()

    def save(self, commit=True, user=None):
        inst =super().save(commit=False)
        if user:
            inst.Created_By = user
        if commit:
            inst.save()
        return inst
    
    def is_valid(self):
        valid = super(StudentForm, self).is_valid()
        if not valid:
            return False

        serializer = StudentSerializer(data=self.cleaned_data)
        return serializer.is_valid() 


class Add_Column(forms.Form):
    q=forms.CharField(max_length=255)
    query = f'ALTER TABLE {q}'  