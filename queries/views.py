from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import QueryForm


# Create your views here.
def query_request(request):
    submitted = False
    if request.method == 'POST':
        form = QueryForm(request.POST, request.FILES)
        if form.is_valid():
            query = form.save(commit=False)
            query.username = request.user.username
            query.save()
            messages.success(request,
                             'You successfuly added a pet to your profile!')
            return HttpResponseRedirect('/query/?submitted=True')
    else:
        form = QueryForm()
        if 'submitted' in request.GET:
            submitted = True

    template = 'queries/query.html/'

    context = {
        'form': form,
        'submitted': submitted,
    }

    return render(request, template, context)
