from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Comment Input Form
    """
    class Meta:
        """
        Meta class
        """
        model = Comment
        fields = ('body',)
