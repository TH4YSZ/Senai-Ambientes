from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('senai', views.senai, name='senai'),
    path('ambiente', views.ambientes, name='ambiente')
] 