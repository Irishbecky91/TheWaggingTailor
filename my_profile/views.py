"""
Profile Views
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order

from .models import UsersProfile, PetProfile
from .forms import PetProfileForm


# Create your views here.
@login_required
def profile(request):
    """
    Renders the profile page
    """
    profile = get_object_or_404(UsersProfile, user=request.user)
    pets = PetProfile.objects.all()
    orders = profile.orders.all()
    if not profile:
        messages.error(request,
                       "I'm sorry, you need to log in first")
        return redirect(reverse('home'))

    template = 'my_profile/my_profile.html'
    context = {
        'pets': pets,
        'orders': orders,
        'bag_details_not_required': True
    }

    return render(request, template, context)


@login_required
def add_pet(request):
    """
    Renders the add pet form
    """
    if request.method == 'POST':
        add_pet_form = PetProfileForm(request.POST, request.FILES)
        if add_pet_form.is_valid():
            pet = add_pet_form.save(commit=False)
            pet.pet_owner = request.user.userprofile
            pet.save()
            messages.success(request,
                             'You successfuly added a pet to your profile!')
            return redirect(reverse('profile'))
        else:
            messages.error(request,
                           ('Failed to add a pet to your profile. '
                            'Please ensure the form is valid.'))
    else:
        add_pet_form = PetProfileForm()

    template = 'my_profile/add_pet_form.html'
    context = {
        'add_pet_form': add_pet_form,
    }

    return render(request, template, context)


@login_required
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