from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, default=None)
    middle_name = models.CharField(null=True, max_length=50)
    gender = models.CharField(max_length=1)
    street_address = models.CharField(max_length=75)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    cell = models.CharField(max_length=20)
    country = models.CharField(max_length=25)
    dob = models.CharField(max_length=50)
    member_organization = models.CharField(null=True, max_length=75)
