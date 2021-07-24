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