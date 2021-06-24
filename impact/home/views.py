
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import SignUpForm, UpdateUserForm, UpdateVolunteerForm


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
            user = form.save()
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

    auth.logout(request)
    return render(request, 'index.html')


@login_required
def updateProfile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateVolunteerForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'You profile as been updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateVolunteerForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
    

