from django.forms import forms
from django.contrib.auth.forms import PasswordChangeForm

models = [
    ("user", "User"),
    ("student", "Student"), 
    ]
class AddFieldForm(forms.Form):
    model = forms.CharField(max_length=100, choices= Models,required=True)
    additional_field = forms.JsonField(required=True)

    def save():
        model.add_field(**additional_field)