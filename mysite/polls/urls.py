from django.urls import path

from ..mysite import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('segunda', views.second, name='segunda'),
]