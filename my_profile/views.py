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
    pets = PetProfile.objects.filter(pet_owner=profile)
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
        pet_form = PetProfileForm(request.POST, request.FILES)
        if pet_form.is_valid():
            pet = pet_form.save(commit=False)
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
        pet_form = PetProfileForm()

    template = 'my_profile/pet_form.html'
    context = {
        'pet_form': pet_form,
    }

    return render(request, template, context)


@login_required
def edit_pet(request, pet_id):
    """
    Used to add a product in the store
    """
    if not request.user:
        messages.error(request, "Sorry, you don't have permission to do that.")
        return redirect(reverse('home'))

    pet = get_object_or_404(PetProfile, pk=pet_id)
    if request.method == 'POST':
        pet_form = PetProfileForm(request.POST, request.FILES,
                                  instance=pet)
        if pet_form.is_valid():
            pet_form.save()
            messages.success(request,
                             (f"You sucessfully edited {pet.pet_name}'s \
                                profile!"))
            return redirect(reverse('profile'))
        else:
            messages.error(request,
                           (f"I'm sorry, you were unable to edit \
                            {pet.pet_name}'s profile. "
                            "Please check your form and try again."))
    else:
        pet_form = PetProfileForm(instance=pet)
        messages.info(request, f'You are editing the product {pet.pet_name}.')

    template = 'my_profile/edit_pet.html'
    context = {
        'pet_form': pet_form,
        'pet': pet,
    }

    return render(request, template, context)


@login_required
def delete_pet(request, pet_id):
    """
    Remove the the product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to do that.")
        return redirect(reverse('home'))

    pet = get_object_or_404(PetProfile, pk=pet_id)
    pet.delete()
    messages.success(request, f'You deleted {pet.pet_name} from the store.')
    return redirect(reverse('profile'))



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
