"""
Products Views
"""
from django.shortcuts import render
from .models import Product


# Create your views here.
def products_list(request):
    """
    The Products List view displays the list of products, as well as
    sorting and search queries
    """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
