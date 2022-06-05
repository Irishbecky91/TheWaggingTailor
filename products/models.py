"""
Products Models
"""
from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Defines the Category Model used to filter products by category
    """
    class Meta:
        """
        This class changes the admin from the default display 'Categorys'
        to 'Categories
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """
        Get's the friendly name
        """
        return self.friendly_name


class Product(models.Model):
    """
    Defines the Product Model used to show each product in the shop and in
    the product details pages.
    """
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    description = models.TextField()
    sizes_available = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    """
    Comment class
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.CharField(max_length=75)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Ordering comments in order of when they were created
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the user's name
        and the content of the comment.
        """
        return f"Comment {self.body} by {self.name}"
