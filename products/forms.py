"""
Product Forms
"""
from django import forms
from .models import Product, Category, Comment


class ProductForm(forms.ModelForm):
    """
    The Product form allows the user to add a product to the store.
    """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-navy rounded-0'

    
class CommentForm(forms.ModelForm):
    """
    The Comment Form allows users to add comments to the site.
    """
    class Meta:
        model = Comment
        fields = ['title', 'body']
