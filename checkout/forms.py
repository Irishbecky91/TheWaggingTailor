from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Checkout form
    """
    model = Order
    fields = (
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'country',
    )

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholders = f'{placeholders[field]} *'
            else:
                placeholders = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholders
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
