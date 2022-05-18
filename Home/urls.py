from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('home-page', views.home, name = 'home'),
    path('ProductID=<int:id>', views.details, name = 'details'),
    path('cart-page', views.cart, name = 'cart'),
]