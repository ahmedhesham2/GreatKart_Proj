from django.shortcuts import render, get_object_or_404
from store.models import product
from category.models import Category

# Create your views here.
def store(request , category_slug=None):
    products = product.objects.filter(is_available=True)

    if category_slug != None :
        categories = get_object_or_404(Category , slug = category_slug)
        products = products.filter(category=categories)

    context = { 'products' : products }
    return render(request , 'store/store.html' , context)

def product_detail(request, category_slug = None, product_slug = None) :
    try :
        single_product = product.objects.get(category__slug=category_slug , slug = product_slug)
        context = {
            'single_product' : single_product
        }

    except Exception as e :
        raise e

    return render(request , 'store/product_detail.html',context)