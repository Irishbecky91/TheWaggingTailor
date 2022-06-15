"""
Query Views
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import QueryForm


def query(request):
    """
    This view shows and submits the query form and shows the success/error
    messages.
    """
    if request.method == 'POST':
        form = QueryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,
                             ('You successfuly submitted a query! '
                              'We aim to respond within 2-3 business days. '
                              'If your query is urgent, please email us \
                                  directly on info@thewaggingtailor.com'))
            return redirect(reverse('query'))
        else:
            messages.error(request,
                           ('Failed to submit your query. '
                            'Please ensure the form is valid.'))
    else:
        form = QueryForm()

    template = 'queries/query.html/'

    context = {
        'form': form,
        'bag_details_not_required': True
    }

    return render(request, template, context)
