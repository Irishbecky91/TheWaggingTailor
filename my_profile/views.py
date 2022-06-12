"""
Profile Views
"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout.models import Order

from .models import UsersProfile
from .forms import PetProfileForm


# Create your views here.
def profile(request):
    """
    Renders the profile page
    """
    profile = get_object_or_404(UsersProfile, user=request.user)

    if request.method == 'POST':
        form = PetProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has updated successfully')

    form = PetProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'my_profile/my_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def my_order_history(request, order_number):
    """
    Renders the order history
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past order confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
