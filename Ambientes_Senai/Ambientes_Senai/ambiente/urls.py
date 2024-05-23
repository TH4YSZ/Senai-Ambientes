from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('cadastro', views.cadastro, name='cadastro'),
    path('ambientes', views.ambientes, name = 'ambientes'),
    path('reservas', views.reservas, name='reservas')
]