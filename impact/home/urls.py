from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('update_profile', views.updateProfile, name='update_profile'),
]