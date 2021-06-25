from django.contrib.auth import backends
from django.contrib.auth import models
from django.core.exceptions import ValidationError
from home.forms import SignInForm, SignUpForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from backend.models import UserDetails
from django.contrib.auth import logout

# Create your views here.

import logging
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def signup(request):
    if(request.method == 'POST'):

        form = SignUpForm(request.POST)

        if form.is_valid():
            username = request.POST['username']

            try:
                user = User.objects.get(username=username)
                return render(request, 'signup.html', {
                    'error': 'Username not available',
                    'form': SignUpForm
                })
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    password=request.POST['password'],)

                UserDetails.objects.create(
                    middle_name=request.POST['middle_name'],
                    gender=request.POST['gender'],
                    street_address=request.POST['street_address'],
                    city=request.POST['city'],
                    state=request.POST['state'],
                    zipcode=request.POST['zipcode'],
                    cell=request.POST['cell'],
                    country=request.POST['country'],
                    dob=request.POST['dob'],
                    member_organization=request.POST['member_organization'],
                    user=user
                )

                auth.login(request, user)

                return redirect('dashboard')
        else:
            return render(request, 'signup.html', {"form": form})

    else:
        return render(request, 'signup.html', {
            'form': SignUpForm
        })


def signin(request):
    if(request.method == 'POST'):
        # see if it's an actual user
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'signin.html', {
                'error': 'Incorrect username or password',
                'form': SignInForm})
    else:
        return render(request, 'signin.html', {
            "form": SignInForm
        })


def signout(request):
    logout(request,)
    return render(request, 'index.html',  {
        "message": "You have successfully logged out!"
    })


def users(request, user_id, operation):
    if(request.method == 'GET'):

        if(operation == 'read'):
            data = getUserDetails(user_id)
            return render(request, 'get_user_result.html', data)

        elif(operation == 'update'):

            data = getUserDetails(user_id)
            form = UserUpdateForm(initial=data)

            return render(request, 'user_update.html', {"form": form})

        elif(operation == 'delete'):
            User.objects.filter(id=user_id).delete()
            data = {
                'message': "Your account has been deleted!"
            }
            logout(request)
            return render(request, 'index.html', data)

        else:
            return redirect('home')

    elif(request.method == 'POST'):
        form = UserUpdateForm(request.POST)

        if form.is_valid():

            user = User.objects.get(id=user_id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()

            userDetails = UserDetails.objects.get(user_id=user_id)
            userDetails.middle_name = request.POST['middle_name']
            userDetails.gender = request.POST['gender']
            userDetails.street_address = request.POST['street_address']
            userDetails.city = request.POST['city']
            userDetails.state = request.POST['state']
            userDetails.zipcode = request.POST['zipcode']
            userDetails.cell = request.POST['cell']
            userDetails.country = request.POST['country']
            userDetails.dob = request.POST['dob']
            userDetails.member_organization = request.POST['member_organization']
            userDetails.save()

            data = getUserDetails(user_id)
            data['message'] = "User updated successfully!"

            return render(request, 'get_user_result.html', data)
        else:
            return render(request, 'signup.html', {"form": form})

    else:
        return redirect('home')


def getUserDetails(user_id):
    user = User.objects.filter(id=user_id).values().first()
    userDetails = UserDetails.objects.filter(
        user_id=user_id).values().first()

    data = {
        'username': user['username'],
        'first_name': user['first_name'],
        'last_name': user['last_name'],
        'email': user['email'],
        'middle_name': userDetails['middle_name'],
        'gender': userDetails['gender'],
        'street_address': userDetails['street_address'],
        'city': userDetails['city'],
        'state': userDetails['state'],
        'zipcode': userDetails['zipcode'],
        'cell': userDetails['cell'],
        'country': userDetails['country'],
        'dob': userDetails['dob'],
        'member_organization': userDetails['member_organization'],
    }

    return data
