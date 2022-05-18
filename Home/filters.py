
from dataclasses import fields
import django_filters
from . models import Product, Cart

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
           'ProductName',
           'ProductBrand',
           'ProductNewPrice',
           'ProductRam',
           'ProductRom',
        }
class CartFilter(django_filters.FilterSet):
    class Meta:
        model = Cart
        fields = {
            'user',
            'product',
            'amount',
        }
