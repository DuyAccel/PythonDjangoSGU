from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sign-up', views.signup, name = 'signup'),
    path('sign-in', views.signin, name = 'signin'),
    path('sign-out', views.signout, name = 'signout'),
]