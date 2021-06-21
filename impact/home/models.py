from django.db import models, reset_queries
from django.db.models.base import ModelState

# Create your models here.
class Volunteer(models.Model):
    slug = models.SlugField(null=True)
    username = models.CharField(max_length=24)
    email = models.EmailField()
    password= models.CharField(max_length=255)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
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
        return self.username, self.firstName, self.lastName
       


    def get_absolute_url(self):
        return reverse("dashboard", kwargs={"slug": self.slug}) #need to check this and make sure it should go to the dashboard page
    