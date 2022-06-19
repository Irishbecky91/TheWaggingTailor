"""
Products Views
"""
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm, CommentForm


# Create your views here.
def products_list(request):
    """
    The Products List view displays the list of products, as well as
    sorting and search queries
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sort_key == 'category':
                sort_key = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = (
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_info(request, product_id):
    """
    The Product Info view displays the information for individual products.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.user:
        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.product = product
                comment.save()

                return redirect(reverse('product_info', args=[product.id]))
        else:
            form = CommentForm()

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'products/product_info.html', context)


@login_required
def add_product(request):
    """
    Used to add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            messages.success(request, 'You have successfully added a new \
                product')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request,
                           ("I'm sorry, that product was not added. "
                            "Please check your form and try again."))
    else:
        product_form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Used to add a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES,
                                   instance=product)
        if product_form.is_valid():
            product_form.save()
            messages.success(request,
                             (f'You sucessfully edited {product.name}!'))
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request,
                           (f"I'm sorry, you were unable to edit {product.name}. \
                            Please check your form and try again."))
    else:
        product_form = ProductForm(instance=product)
        messages.info(request, f'You are editing the product {product.name}.')

    template = 'products/edit_product.html'
    context = {
        'product_form': product_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Remove the the product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'You deleted {product.name} from the store.')
    return redirect(reverse('products'))
