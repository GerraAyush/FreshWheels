from django.db import models

# Create your models here.
class FarmerProfile(models.Model):
    full_name = models.CharField(null=False, max_length=100)
    phone = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=200)
    description = models.CharField(null=False, max_length=200)
    profile_img = models.ImageField(upload_to='pictures')
    license_number = models.IntegerField(null=False)
    district = models.CharField(null=False, max_length=50)
