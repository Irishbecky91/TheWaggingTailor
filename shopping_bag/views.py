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
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(redirect_url)
