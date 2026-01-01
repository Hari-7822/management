from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

class FormInputMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            existing_classes = self.fields[field_name].widget.attrs.get('class', '')
            
            self.fields[field_name].widget.attrs.update({
                'class': f'{existing_classes} google-input-field'.strip(),
                'value': '',
                'onkeyup': "this.setAttribute('value', this.value);"
            })
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        
        layout_fields = []
        for field_name in self.fields.keys():
            layout_fields.append(
                Field(
                    field_name, 
                    wrapper_class='google-input',css_class='google-input-field'
                )
            )
        
        self.helper.layout = Layout(*layout_fields)
