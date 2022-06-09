from django.contrib import admin
from .models import Order, OrderLineItem


# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline Order LineItem Admin
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Order Admin
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number',
        'date',
        'shipping_cost',
        'order_total',
        'grand_total',
        )
    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'county',
        'postcode',
        'country',
        'shipping_cost',
        'order_total',
        'grand_total',
    )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'shipping_cost',
        'order_total',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
