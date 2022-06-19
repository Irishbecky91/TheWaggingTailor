"""
Product Admin
"""
from django.contrib import admin
from .models import Product, Category, Comment


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


class CommentAdmin(admin.ModelAdmin):
    """
    This class defines the appearance and control over the comments in
    the admin.
    """
    list_display = ('author', 'title', 'product', 'date_created')
    list_filter = ('product', 'date_created')
    search_fields = ['author', 'title']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
