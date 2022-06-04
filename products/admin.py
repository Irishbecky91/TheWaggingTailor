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
        'name',
        'category',
        'description',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Defines how the Category is used and displayed in Admin
    """
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

