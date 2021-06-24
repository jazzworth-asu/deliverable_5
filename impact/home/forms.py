from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateUserForm(ModelForm):
    email = forms.EmailField()

    class Meta:
       model = User
       fields = ['username', 'email', 'first_name', 'last_name']


class UpdateVolunteerForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'streetAddress', 'city', 'state', 'zipcode', 'country', 'dob', 'memberOrganization']
    