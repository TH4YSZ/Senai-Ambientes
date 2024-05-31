from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('ambientes', views.ambientes, name='ambientes'),
    path('reservas/<int:id>', views.reservas, name='reservas'),
    path('minhas_reservas', views.minhas_reservas, name='minhas_reservas'),
]