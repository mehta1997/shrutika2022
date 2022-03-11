
from .models import bottle
from django.forms import ModelForm
    
class customerform(ModelForm):
    class Meta:
        model = bottle
        fields = '__all__'