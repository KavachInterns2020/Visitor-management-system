from django.forms import ModelForm
from django import forms
from .models import *
from django.core import validators

def checkforz(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("please check")


class HostForm(forms.ModelForm):
    name=forms.CharField(validators=[checkforz])
    class Meta:
        model = Host
        fields = '__all__'
         
  
  
class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'
        
        
  

class VisitDetailsForm(ModelForm):
    class Meta:
        model = VisitDetails
        fields = '__all__'
