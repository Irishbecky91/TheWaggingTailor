"""
Profile Views
"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UsersProfile
from .forms import UsersProfileForm


# Create your views here.
def profile(request):
    """
    Renders the profile page
    """
    profile = get_object_or_404(UsersProfile, user=request.user)

    if request.method == 'POST':
        form = UsersProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has updated successfully')

    form = UsersProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'my_profile/my_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile-page': True
    }

    return render(request, template, context)
