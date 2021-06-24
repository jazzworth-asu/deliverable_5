from django.db import models
from django.db.models.base import ModelState
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Volunteer(models.Model):
    username = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
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
        return str(self.user.username)

    

# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Volunteer.objects.create(user=instance)
#     instance.volunteer.save()