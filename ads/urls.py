from django.urls import path
from . import views

#routing
urlpatterns = [
    path('', views.index),
    path('favourites/<int:pk>/', views.add_to_favourites, name='favourites')
]