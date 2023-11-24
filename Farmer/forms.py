from django.forms import ModelForm
from .models import FarmerProfile

class FarmerInfoForm(ModelForm):
    class Meta:
        model = FarmerProfile
        fields = "__all__"