from django.shortcuts import render


def page_not_found_view(request, exception):
    """
    Handles 404 page not found error
    """
    return render(request, '404.html', status=404)
