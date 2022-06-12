"""
Checkout URLs
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('my_order_history/<order_number>', views.my_order_history,
         name='my_order_history'),
]
