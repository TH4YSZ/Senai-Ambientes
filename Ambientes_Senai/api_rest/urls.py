from django.urls import path
from . import views

urlpatterns = [
    path('senai/', views.senai, name='senai'),
    path('ambiente/', views.ambientes_list_create, name='ambientes_list_create'),
    path('ambiente/<int:id>', views.ambientes_detail, name='ambiente_detail'),
    path('usuario/', views.usuario_create, name='usuario_create'),
    path('reserva/', views.reservas_list_create, name='reservas_list_create'),
    path('reserva/<int:id>', views.reservas_detail, name='reserva_detail'),
    path('token/verify/', views.verify_token, name='verify_token'), 
]