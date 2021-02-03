from django.urls import path

from places import views

urlpatterns = [
    path('', views.index, name='index'),
    path('places/<int:pk>/', views.get_point, name='place'),
]
