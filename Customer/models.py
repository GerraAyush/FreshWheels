from django.db import models

class CustomerProfile(models.Model):
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    phone = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=200)