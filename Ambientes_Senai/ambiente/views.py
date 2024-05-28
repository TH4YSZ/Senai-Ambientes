from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login

# Create your views here.
def homepage(request):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai

    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            var_username = form.cleaned_data['username']
            var_password = form.cleaned_data['password']

            user = authenticate(username=var_username, password=var_password)

            if user is not None:
                return redirect("ambientes")
            else:
                return redirect("homepage")
    else:
        form = FormLogin()

    context.update({"form": form})
    return render(request, 'homepage.html', context)

def cadastro(request):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai

    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_username = form.cleaned_data['username']
            var_senha = form.cleaned_data['senha']
            var_cargo = form.cleaned_data['cargo']


            user = User.objects.create_user(username=var_username, password=var_senha)
            user.first_name = var_nome
            user.last_name = var_sobrenome
            user.cargo = var_cargo
            user.save()

            return redirect("homepage")
        else:
            return redirect("cadastro")
    else:
        form = FormCadastro()

    context.update({"form": form})
    return render(request, 'cadastro.html', context)

def ambientes(request):
    context = {}
    dados_senai = Senai.objects.all()
    dados_ambiente = Ambiente.objects.all()
    context["dados_senai"] = dados_senai
    context["dados_ambiente"] = dados_ambiente

    return render(request, 'ambientes.html', context)

def reservas(request, id):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai
    id_ambiente = Ambiente.objects.filter(id = id)
    
    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            var_username = request.user.username
            var_data = form.cleaned_data['data']
            var_hora = form.cleaned_data['horario']

            user = Reserva(username= var_username, data= var_data, horario= var_hora, sala = id_ambiente)
            user.save()

            return redirect("ambientes")
        else:
            return redirect("reservas")
    else:
        form = FormReserva()

    context.update({"form": form})
    return render(request, 'reservas.html', context)