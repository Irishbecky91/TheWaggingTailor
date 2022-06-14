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
def profile(request):
    """
    Renders the profile page
    """
    profile = get_object_or_404(UsersProfile, user=request.user)
    pets = PetProfile.objects.all()
    orders = profile.orders.all()

    template = 'my_profile/my_profile.html'
    context = {
        'pets': pets,
        'orders': orders,
        'on_profile_page': True
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
                            'Please ensure th form is valid.'))
    else:
        add_pet_form = PetProfileForm()

    template = 'my_profile/add_pet_form.html'
    context = {
        'add_pet_form': add_pet_form,
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


def coments(self, request, slug, *args, **kwargs):
    """
    Submits form content to the database
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.filter(approved=True).order_by('created_on')
    liked = False
    if recipe.likes.filter(id=self.request.user.id).exists():
        liked = True

    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.recipe = recipe
        comment.save()

    else:
        comment_form = CommentForm()

    return render(
        request,
        "recipe.html",
        {
            "recipe": recipe,
            "comments": comments,
            "commented": True,
            "liked": liked,
            "comment_form": CommentForm(),
        }
    )
