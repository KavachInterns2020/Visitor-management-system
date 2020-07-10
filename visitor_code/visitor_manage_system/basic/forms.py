from django.forms import ModelForm
from .models import *


class HostForm(ModelForm):
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