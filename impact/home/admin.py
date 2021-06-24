from django.contrib import admin
from .models import Profile, Volunteer

# Register your models here.
# class VolunteerAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'password', 'firstName', 'middleName', 'lastName', 'gender', 'streetAddress', 'city', 'state', 'zipcode', 'tel', 'country', 'dob', 'memberOrganization')

admin.site.register(Profile)