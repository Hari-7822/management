from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class FormInputMixin:
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'value': '',
                'onkeyup': "this.setAttribute('value', this.value);"
            })
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        
        layout_fields = []
        for field_name in self.fields.keys():
            layout_fields.append(
                Field(field_name, wrapper_class='google-input')
            )
        
        self.helper.layout = Layout(*layout_fields)
        
