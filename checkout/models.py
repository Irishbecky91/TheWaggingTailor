"""
Checkout Views
"""
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from products.models import Product
from my_profile.models import UsersProfile


# Create your models here.
class Order(models.Model):
    """
    Order view displays the information required in the checkout
    which will also display in the order confirmation and history.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UsersProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    shipping_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _create_order_number(self):
        """
        Creates a unique order number at random for the user and site owner to
        track a purchase
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Updates the grand total of the shopping bag each time a line item is
        added, taking shipping costs into account.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        )
        if self.order_total < settings.FREE_SHIPPING_THRESHOLD:
            self.shipping_cost = (
                self.order_total * settings.STANDARD_SHIPPING_PERCENTAGE / 100
            )
        else:
            self.shipping_cost = 0
        self.grand_total = self.order_total + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Overrides the initial save method to set the order number in case
        it has not already been set.
        """
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    This generates a unique id for each order placed.
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Overrides the initial save method to set the lineitem_total in case
        and also update the order_total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order.order_number
