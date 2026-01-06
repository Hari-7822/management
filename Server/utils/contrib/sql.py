from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.functional import lazy
from django.apps import apps 

def check(obj:dict, field_name):
    try:
        if ["name", "type", "null", "blank", "default", "unique", "db_index", "editable"] in obj.keys():
            return True
    except:
        return False

def get_model():
    return [(
        f"{model._meta.app_label}.{model.__name__}",
        f"{model._meta.app_label} › {model.__name__}"
        )for model in apps.get_models()
    ]

models = lazy(get_model())

class AddFieldForm(forms.Form):
    model = forms.ChoiceField(choices= models,required=True)
    field = forms.JSONField(required=True)
    config = forms.JSONField(required=False)

    def is_valid():

        valid = super(AddFieldForm, self).is_valid()
        if not valid:
            return False
        return True

    def save(self):
        self.model.add_field(*self.field, **self.config)