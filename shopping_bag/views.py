"""
Shopping Bag Views
"""
from django.shortcuts import render, redirect


# Create your views here.
def view_bag(request):
    """
    This renders the bag contents to be inspected
    """
    return render(request, 'shopping_bag/bag.html')


def add_to_shopping_bag(request, item_id):
    """
    Add a number of the specific product to the shopping bag
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if item_id in list(shopping_bag.keys()):
            if size in shopping_bag[item_id]['items_by_size'].keys():
                shopping_bag[item_id]['items_by_size'][size] += quantity
            else:
                shopping_bag[item_id]['items_by_size']= quantity
        else:
            shopping_bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(shopping_bag.keys()):
            shopping_bag[item_id] += quantity
        else:
            shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)
