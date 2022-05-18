
from dataclasses import fields
from django.forms import ModelForm, Form
from django import forms
from .models import Cart

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['amount', 'product', 'user']

class deleteCartForm(Form):
    delete_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        fields = ['delete_id']
    

