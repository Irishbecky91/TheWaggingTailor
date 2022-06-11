"""
Profile Views
"""
from django.shortcuts import render


# Create your views here.
def profile(request):
    """
    Renders the profile page
    """
    template = 'my_profile/my_profile.html'
    context = {}

    return render(request, template, context)
