from django.shortcuts import render


# Create your views here.
def home(request):
    """
    Home View
    """
    render(request, 'home/index.html')
