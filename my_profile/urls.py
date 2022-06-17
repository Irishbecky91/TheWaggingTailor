"""
Checkout URLs
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('my_order_history/<order_number>', views.my_order_history,
         name='my_order_history'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('edit_pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('delete_pet/<int:pet_id>/', views.delete_pet,
         name='delete_pet'),
]
