from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import *

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db import IntegrityError

from django.shortcuts import redirect, get_object_or_404

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

    if not request.user.groups.filter(name='Coordenação').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect("homepage")

    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_username = form.cleaned_data['username']
            var_senha = form.cleaned_data['senha']

            try:
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
                messages.success(request, "Usuário cadastrado.")
                return redirect("cadastro")
            except IntegrityError:
                messages.error(request, "Nome de usuário já existe. Por favor, escolha outro nome de usuário.")
                # Renderizar o formulário com dados existentes
                context.update({"form": form})
                return render(request, 'cadastro.html', context)
        else:
            # Se o formulário não for válido, renderize a página com erros do formulário
            context.update({"form": form})
            return render(request, 'cadastro.html', context)
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
    
    # Inicialize a pesquisa com GET
    search_query = request.GET.get('search', '')
    if search_query:
        dados_ambiente = Ambiente.objects.filter(titulo__icontains=search_query)
    else:
        dados_ambiente = Ambiente.objects.all()
    
    context["dados_senai"] = dados_senai
    context["dados_ambiente"] = dados_ambiente
    context["form"] = FormPesquisa()

    if request.user.is_authenticated:
        context['is_coordenacao'] = request.user.groups.filter(name='Coordenação').exists()
        context['is_professores'] = request.user.groups.filter(name='Professores').exists()
    else:
        context['is_coordenacao'] = False
        context['is_professores'] = False

    return render(request, 'ambientes.html', context)


@login_required
def excluir_ambiente(request, id):
    if not request.user.groups.filter(name='Coordenação').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect("homepage")

    ambiente = get_object_or_404(Ambiente, id=id)
    if request.method == 'POST':
        ambiente.delete()
        return redirect('ambientes')
    return redirect('ambientes')    

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
            var_horafinal = form.cleaned_data['hora_final']

            # Verificar se já existe uma reserva para o mesmo ambiente e horário
            reserva_existente = Reserva.objects.filter(
                sala=id_ambiente,
                data=var_data,
                horario__lt=var_horafinal,
                hora_final__gt=var_hora
            ).exists()

            if reserva_existente:
                messages.error(request, "Já existe uma reserva para este ambiente no horário selecionado.")
                return redirect(reverse('ambientes', args=[id]))

            reserva = Reserva(username=var_username, data=var_data, horario=var_hora, hora_final=var_horafinal, sala=id_ambiente)
            reserva.save()
            messages.success(request, "Ambiente reservado com sucesso.")
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

@login_required
def excluir_reserva(request, id):
    if not request.user.groups.filter(name='Coordenação').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect("homepage")

    reserva = get_object_or_404(Reserva, id=id)
    
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, "Reserva excluída com sucesso.")
        return redirect('ambientes')
    
    # Exibe uma página de confirmação antes de excluir a reserva
    return render(request, 'confirmar_exclusao.html', {'reserva': reserva})


@login_required
def todas_reservas(request):
    context = {}
    dados_senai = Senai.objects.all()
    reservas = Reserva.objects.all()
    context["dados_senai"] = dados_senai
    context["reservas"] = reservas

    # Verifica se o usuário pertence ao grupo Coordenação
    if not request.user.groups.filter(name='Coordenação').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect("homepage")

    if request.user.is_authenticated:
        context['is_coordenacao'] = request.user.groups.filter(name='Coordenação').exists()
        context['is_professores'] = request.user.groups.filter(name='Professores').exists()
    else:
        context['is_coordenacao'] = False
        context['is_professores'] = False

    return render(request, 'todas_reservas.html', context)


@login_required
def cad_ambiente(request):
    context = {}
    dados_senai = Senai.objects.all()
    context["dados_senai"] = dados_senai

    # Verifica se o usuário pertence ao grupo Coordenação
    if not request.user.groups.filter(name='Coordenação').exists():
        messages.error(request, "Você não tem permissão para acessar esta página.")
        return redirect("homepage")

    if request.method == "POST":
        form = FormAmbiente(request.POST)
        if form.is_valid():
            var_titulo = form.cleaned_data['titulo']
            var_descricao = form.cleaned_data['descricao']
            var_sala = form.cleaned_data['sala']
        

            # Cria o novo ambiente 
            Ambiente.objects.create(
                titulo=var_titulo,
                descricao=var_descricao,
                sala=var_sala
            )

            messages.success(request, "Ambiente criado!")
            return redirect("ambientes")
        
    else:
        form = FormAmbiente()

    # Definindo as variáveis de permissão no contexto
    if request.user.is_authenticated:
        context['is_coordenacao'] = request.user.groups.filter(name='Coordenação').exists()
        context['is_professores'] = request.user.groups.filter(name='Professores').exists()
    else:
        context['is_coordenacao'] = False
        context['is_professores'] = False

    context.update({"form": form})
    return render(request, 'New_Ambiente.html', context)



