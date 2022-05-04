from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('favourites/<int:pk>/', views.add_to_favourites, name='favourites')
]