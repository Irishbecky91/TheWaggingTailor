"""
bag tools templatetag
"""
from django import template


register = template.Library()


@register.filter(name='calculate_subtotal')
def calculate_subtotal(price, quantity):
    """
    calculates sub-total
    """
    return price * quantity
