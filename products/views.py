"""
Products Views
"""
from django.shortcuts import render, get_object_or_404
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


def product_info(request, product_id):
    """
    The Product Info view displays the information for individual products.
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
