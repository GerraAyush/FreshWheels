from django.db import models

class DriverProfile(models.Model):
    full_name = models.CharField(null=False, max_length=100)
    phone = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=200)
    license_number = models.IntegerField(null=False)
    license_image = models.ImageField(upload_to='pictures', null=False)
    vehicle = models.CharField(null=False, default='Car', max_length=5)
    experience = models.IntegerField(null=False, default=0)