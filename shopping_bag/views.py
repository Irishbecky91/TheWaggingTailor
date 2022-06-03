from django.shortcuts import render


# Create your views here.
def view_bag(request):
    """
    This renders the bag contents to be inspected
    """
    return render(request, 'shopping_bag/bag.html')