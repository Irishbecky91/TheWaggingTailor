"""
Shopping bag contexts
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Contents of shopping bag and delivery charge calculation
    """
    bag_items = []
    total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, item_data in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        for size, quantity in item_data['items_by_size'].items():
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'size': size,
            })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = total + Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
