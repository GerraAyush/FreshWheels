from django.contrib.auth.models import User
from Farmer.models import FarmerProfile
from Driver.models import DriverProfile
from Customer.models import CustomerProfile
from django.db import models

# Create your models here.
class ExtendedUser(User):
    choice = models.CharField(null=False, default="Customer", max_length=8)
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, null=True)
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username