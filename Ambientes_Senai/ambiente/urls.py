from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('ambientes', views.ambientes, name='ambientes'),
    path('reservas/<int:id>', views.reservas, name='reservas'),
    path('minhas_reservas', views.minhas_reservas, name='minhas_reservas'),
    path('excluir_reserva/<int:id>/', views.excluir_reserva, name='excluir_reserva'),
    path('excluir_ambiente/<int:id>/', views.excluir_ambiente, name='excluir_ambiente'),
    path('cad_ambiente', views.cad_ambiente, name='cad_ambiente'),
    path('todas_reservas/', views.todas_reservas, name='todas_reservas'),
]