from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('cadastro', views.cadastro, name='cadastro'),
    path('ambientes', views.ambientes, name = 'ambientes'),
    path('reservas', views.reservas, name='reservas')
]