"""
Shopping Bag Views
"""
from django.shortcuts import render, redirect, reverse, \
                             HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Create your views here.
def view_shopping_bag(request):
    """
    This renders the bag contents to be inspected
    """
    return render(request, 'shopping_bag/bag.html')


def add_to_shopping_bag(request, item_id):
    """
    Add a number of the specific product to the shopping bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if item_id in list(shopping_bag.keys()):
            if size in shopping_bag[item_id]['items_by_size'].keys():
                shopping_bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, (
                    f'You updated the number of {size.upper()} {product.name} \
                        in your shopping bag to \
                            {shopping_bag[item_id]["items_by_size"][size]}'
                            ))
            else:
                shopping_bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, (
                    f'You added {size.upper()} {product.name} to your \
                        shopping bag'
                ))
        else:
            shopping_bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, (
                f'You added {size.upper()} {product.name} to your shopping bag'
            ))
    else:
        if item_id in list(shopping_bag.keys()):
            shopping_bag[item_id] += quantity
            messages.success(request, (
                f'You updated the number of {product.name} in your shopping \
                    bag to {shopping_bag[item_id]}'
            ))
        else:
            shopping_bag[item_id] = quantity
            messages.success(request, (
                f'You added {product.name} to your shopping bag'
            ))

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def adjust_shopping_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if quantity > 0:
            shopping_bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, (
                f'You updated the number of {size.upper()} {product.name} \
                    in your shopping bag to \
                        {shopping_bag[item_id]["items_by_size"][size]}'
            ))
        else:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
                messages.success(request, (
                    f'You removed {size.upper()} {product.name} from your \
                        shopping bag'
                ))
    else:
        if quantity > 0:
            shopping_bag[item_id] = quantity
            messages.success(request, (
                f'You updated the number of {product.name} in your shopping \
                    bag to {shopping_bag[item_id]}'
            ))
        else:
            shopping_bag.pop(item_id)
            messages.success(request, (
                f'You removed {product.name} from your shopping bag'
            ))

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_shopping_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopping_bag = request.session.get('shopping_bag', {})

        if size:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
            messages.success(request, (
                f'You removed {size.upper()} {product.name} from your \
                    shopping bag'
            ))
        else:
            shopping_bag.pop(item_id)
            messages.success(request, (
                f'You removed {product.name} from your shopping bag'
            ))

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error when removing item: {e}')
        return HttpResponse(status=500)
