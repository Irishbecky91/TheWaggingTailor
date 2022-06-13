"""
Profile Forms
"""
from django import forms
from .models import PetProfile


class PetProfileForm(forms.ModelForm):
    """
    Order form used to enter shipping and user details when
    placing an order
    """
    class Meta:
        """
        Meta
        """
        model = PetProfile
        fields = (
            'pet_name',
            'breed',
            'measurement_a',
            'measurement_b',
            'measurement_c',
            'pet_image',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'pet_name': "Pet's Name",
            'breed': "Pet's Breed",
            'measurement_a': 'Back Measurement (cm)',
            'measurement_b': 'Chest Measurement (cm)',
            'measurement_c': 'Neck Measurement (cm)',
            'pet_image': "Pet's Picture",
        }

        self.fields['pet_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
