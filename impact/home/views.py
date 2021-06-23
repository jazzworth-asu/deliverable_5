from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
from .models import *
from .forms import SignUpForm


import logging
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    form = SignUpForm()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'You have been successfully signed up, ' + user + '!')
            return redirect('signin')

    context = {'form':form}
    return render(request, 'signup.html', context)
    
   
def signin(request):
    if(request.method == 'POST'):
        #see if it's an actual user
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'signin.html', { 'error' : 'Incorrect username or password'})
    else:
        return render(request, 'signin.html')


def signout(request):
    return render(request, 'signout.html')