from . import views
from django.urls import path

#routing
urlpatterns = [
    path('', views.news),
    path('<int:pk>', views.NewsDetailView.as_view(), name='views-detail')
]