from django.forms import ModelForm
from .models import CustomerProfile

class CustomerInfoForm(ModelForm):
    class Meta:
        model = CustomerProfile
        fields = "__all__"