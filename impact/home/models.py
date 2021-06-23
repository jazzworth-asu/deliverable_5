from django.db import models, reset_queries
from django.db.models.base import ModelState
from django.contrib.auth.models import User


# Create your models here.
class Volunteer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    streetAddress = models.CharField(max_length=75)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)
    country = models.CharField(max_length=25)
    dob = models.DateField()
    memberOrganization = models.CharField(max_length=75)
    
    def __str__(self):
        return self.username
       


    def get_absolute_url(self):
        return reverse("dashboard", kwargs={"slug": self.slug}) #need to check this and make sure it should go to the dashboard page
    