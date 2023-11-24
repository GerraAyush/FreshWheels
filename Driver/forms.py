from django.forms import ModelForm
from .models import DriverProfile

class DriverInfoForm(ModelForm):
    class Meta:
        model = DriverProfile
        fields = "__all__"