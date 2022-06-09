"""
Checkout Views
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    """
    Renders the secure checkout page where user's details can
    be entered to complete an order.
    """
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request,
                       "There's nothing in your shopping bag right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
