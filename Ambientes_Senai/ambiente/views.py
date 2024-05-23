from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai

    return render(request, 'homepage.html', context)

def cadastro(request):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai
    return render(request, 'cadastro.html', context)

def ambientes(request):
    context = {}
    dados_senai = Senai.objects.all()
    dados_ambiente = Ambiente.objects.all()
    context["dados_senai"] = dados_senai
    context["dados_ambiente"] = dados_ambiente

    return render(request, 'ambientes.html', context)

def reservas(request):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai
    return render(request, 'reservas.html', context)