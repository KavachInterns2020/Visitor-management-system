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


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'

class EventVisitorForm(ModelForm):
    class Meta:
        model = EventVisitor
        fields = '__all__'