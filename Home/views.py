
import re
from unicodedata import name
from django.shortcuts import render
from numpy import number
from . models import Cart, Product
from .forms import CartForm, deleteCartForm
from Account.models import *
from . filters import ProductFilter
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render



# App Home (Quản lý home page)



def home (request):
    cart = 0
    if request.user.is_authenticated:
        cart = len(getData(request))
    
    context = {'number_cart': cart}
    
    if request.GET:
        filtered_products = ProductFilter(
            request.GET,
            queryset = Product.objects.filter(ProductNewPrice__range=(request.GET.get('ProductPriceMin'), request.GET.get('ProductPriceMax')))
        )
        context['filtered_products'] = filtered_products
        paginated_filtered_products = Paginator(filtered_products.qs, 9)
        page_number = request.GET.get('page')
        product_page_obj = paginated_filtered_products.get_page(page_number)
        context['product_page_obj'] = product_page_obj
        context['product_page_obj2'] = Product.objects.all()[5:8]
        context['product_page_obj3'] = Product.objects.all()[8:12]
        
        return render(request, 'home-page.html', context = context)
    else:
        list_product = Product.objects.all()
        context['filtered_products'] = list_product
        paginated_lits_products = Paginator(list_product, 9)
        page_number = request.GET.get('page')
        product_page_obj = paginated_lits_products.get_page(page_number)
        context['product_page_obj'] = product_page_obj
        context['product_page_obj2'] = Product.objects.all()[5:8]
        context['product_page_obj3'] = Product.objects.all()[8:12]
        
        return render(request, 'home-page.html', context =   context)


def details (request, id):
    product_obj = get_object_or_404(Product, pk = id)
    product_obj_filtered = Product.objects.filter(ProductBrand = product_obj.ProductBrand).values()
    context = {'product_obj': product_obj, 'product_obj_filtered': product_obj_filtered, 'Product_ID' : id}
    
    if request.user.is_authenticated:
        cart = len(getData(request))
        user = request.user.get_username()
        context = {'product_obj': product_obj, 'product_obj_filtered': product_obj_filtered,
                 'Product_ID' : id, 'UserName':user, 'number_cart':cart}

        if request.method == 'POST':

            form = CartForm(request.POST)
            if form.is_valid():
                try:
                    old_cart = Cart.objects.get(user = user, product = product_obj)
                    old_cart.amount += form.save(commit=False).amount
                    old_cart.save()
                    
                except:
                    context = {'product_obj': product_obj, 'product_obj_filtered': product_obj_filtered,
                    'Product_ID' : id, 'UserName':user, 'number_cart':cart+1}
                    form.save()
    return render(request, 'details-page.html', context)

def getData(request):
    cart_list = Cart.objects.filter(user=request.user).values()
    data=[]
    for cart in cart_list:
        product = Product.objects.get(id=cart.get('product_id'))
        dict = {'name':product.ProductName, 'brand':product.ProductBrand, 'new_price':product.ProductNewPrice,
                    'old_price':product.ProductOldPrice, 'amount':cart.get('amount'), 'ram':product.ProductRam,
                    'rom':product.ProductRom, 'img':product.ProductImage3, 'id':product.id}
        data.append(dict)
    return data


def cart (request):
    data = {}
    form = deleteCartForm()
    number_cart = 0
    if request.user.is_authenticated:
        if request.method=='POST':
            form = deleteCartForm(request.POST)
            if form.is_valid():
                delete_id = form.cleaned_data.get('delete_id')
                beDelete = Cart.objects.get(user = request.user, product = delete_id)
                beDelete.delete()
            else:
                print(form)
        data=getData(request)
        number_cart = len(data)
    return render(request, 'cart-page.html', {'data':data, 'form':form, 'number_cart':number_cart})

 