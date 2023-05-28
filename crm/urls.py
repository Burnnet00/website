from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('thx/', views.thx, name='thx'),
]