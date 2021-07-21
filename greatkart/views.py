from django.shortcuts import render
from category.models import Category
from store.models import product

def homePage(request):
    products = product.objects.filter(is_available = True)
    context = {
        'products' : products ,
    }
    return  render(request , 'home.html' , context)