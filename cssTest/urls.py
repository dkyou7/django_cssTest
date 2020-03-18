from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.init,name='main'),
    path('sub/',views.sub,name='sub'),
]