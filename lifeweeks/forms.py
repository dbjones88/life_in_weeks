from django import forms
from django.forms import widgets

class AgeExpect(forms.Form):
    currentAge = forms.IntegerField(label='Enter your age in years', min_value=1, max_value=150)
    retireAge = forms.IntegerField(label='Age you want to retire at', initial=65, min_value=30, max_value=100)
    lifeExpentancy = forms.IntegerField(label='How long do you expect to live in years?', initial=90, min_value=40, max_value=150)
    def __init__(self, *args, **kwargs):
        super(AgeExpect, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

### https://stackoverflow.com/questions/29716023/add-class-to-form-field-django-modelform
