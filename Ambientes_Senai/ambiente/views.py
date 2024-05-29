from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Senai, Usuario, Ambiente, Reserva
from .forms import FormLogin, FormCadastro, FormReserva
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


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
                auth_login(request, user)
                return redirect("ambientes")
            else:
                messages.error(request, "Nome de usuário ou senha incorretos")
    else:
        form = FormLogin()

    context.update({"form": form})
    return render(request, 'homepage.html', context)

@login_required
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

            user = User.objects.create_user(username=var_username, password=var_senha)
            user.first_name = var_nome
            user.last_name = var_sobrenome
            user.save()

            # Adiciona o usuário ao grupo de professores
            professor_group = Group.objects.get(name='Professores')
            user.groups.add(professor_group)

            # Cria o perfil do usuário personalizado
            Usuario.objects.create(
                nome=var_nome,
                sobrenome=var_sobrenome,
                username=var_username,
                senha=var_senha,
                cargo="PROFESSOR"
            )

            return redirect("cadastro")
    else:
        form = FormCadastro()

    # Definindo as variáveis de permissão no contexto
    if request.user.is_authenticated:
        context['is_coordenacao'] = request.user.groups.filter(name='Coordenação').exists()
        context['is_professores'] = request.user.groups.filter(name='Professores').exists()
    else:
        context['is_coordenacao'] = False
        context['is_professores'] = False

    context.update({"form": form})
    return render(request, 'cadastro.html', context)


@login_required
def ambientes(request):
    context = {}
    dados_senai = Senai.objects.all()
    dados_ambiente = Ambiente.objects.all()
    context["dados_senai"] = dados_senai
    context["dados_ambiente"] = dados_ambiente

    if request.user.is_authenticated:
        context['is_coordenacao'] = request.user.groups.filter(name='Coordenação').exists()
        context['is_professores'] = request.user.groups.filter(name='Professores').exists()
    else:
        context['is_coordenacao'] = False
        context['is_professores'] = False

    return render(request, 'ambientes.html', context)

@login_required
def reservas(request, id):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai
    id_ambiente = Ambiente.objects.filter(id=id).first()

    if request.user.is_authenticated:
        context['is_coordenacao'] = request.user.groups.filter(name='Coordenação').exists()
        context['is_professores'] = request.user.groups.filter(name='Professores').exists()
    else:
        context['is_coordenacao'] = False
        context['is_professores'] = False

    if request.method == "POST":
        form = FormReserva(request.POST)
        if form.is_valid():
            var_username = request.user.username  
            var_data = form.cleaned_data['data']
            var_hora = form.cleaned_data['horario']

            reserva = Reserva(username=var_username, data=var_data, horario=var_hora, sala=id_ambiente)
            reserva.save()

            return redirect("ambientes")
        else:
            return redirect(reverse('reservas', args=[id]))
    else:
        form = FormReserva()

    context.update({"form": form})
    return render(request, 'reservas.html', context)

@login_required
def minhas_reservas(request):
    context = {}
    dados_senai = Senai.objects.all()
    reservas = Reserva.objects.filter(username=request.user.username)
    context["dados_senai"] = dados_senai
    context["reservas"] = reservas

    if request.user.is_authenticated:
        context['is_coordenacao'] = request.user.groups.filter(name='Coordenação').exists()
        context['is_professores'] = request.user.groups.filter(name='Professores').exists()
    else:
        context['is_coordenacao'] = False
        context['is_professores'] = False

    return render(request, 'minhas_reservas.html', context)
