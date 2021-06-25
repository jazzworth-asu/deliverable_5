from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('users/<user_id>/<operation>', views.users, name='users'),
]