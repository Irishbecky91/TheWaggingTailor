"""
Profile Forms
"""
from django.forms import ModelForm
from .models import Query


class QueryForm(ModelForm):
    """
    Query submission form
    """
    class Meta:
        model = Query
        fields = [
            'name',
            'email',
            'phone_number',
            'query_type',
            'description',
            'query_image',
        ]
