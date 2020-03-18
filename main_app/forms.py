from django.forms import ModelForm
from .models import LastWorn

class LastWornForm(ModelForm):
  class Meta:
    model = LastWorn
    fields = ['date', 'activity']