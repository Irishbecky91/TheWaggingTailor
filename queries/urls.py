"""
Checkout URLs
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.query, name='query'),
]
