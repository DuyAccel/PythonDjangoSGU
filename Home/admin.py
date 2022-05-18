from django.contrib import admin
from .models import Cart, Product

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    model = Product
    list_display = ['id', 'ProductName', 'ProductStar', 'ProductBrand', 'ProductNumber',
    'ProductNewPrice', 'ProductOldPrice', 'ProductImage1', 'ProductImage2', 'ProductImage3',
    'ProductRam', 'ProductRom']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ['ID', 'user', 'product', 'amount']
