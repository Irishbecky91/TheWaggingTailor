"""
Product Admin
"""
from django.contrib import admin
from .models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    """
    Defines how the Product is used and displayed in Admin
    """
    list_display = (
        'pk',
        'product_name',
        'category',
        'description',
        'price',
        'rating',
        'has_sizes',
        'image',
    )

    ordering = ('product_name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Defines how the Category is used and displayed in Admin
    """
    list_display = (
        'category_name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)