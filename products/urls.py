from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='products'),
    path('<product_id>', views.product_info, name='product_info'),
]
