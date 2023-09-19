from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('add_event', views.add_event, name='add_event'),
    path('check_event', views.check_event, name='check_event'),
    path('profile', views.profile, name='profile'),
    path('check_true', views.check_true)
]
