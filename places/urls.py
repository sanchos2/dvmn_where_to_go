"""Urls."""
from django.urls import path

from places import get_places, views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:pk>/', get_places.point, name='place'),
]
