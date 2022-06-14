"""
Checkout URLs
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.query_request, name='query_request'),
]
