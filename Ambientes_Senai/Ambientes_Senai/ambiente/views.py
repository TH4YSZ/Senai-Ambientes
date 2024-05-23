from django.shortcuts import render
from .models import Senai  
# Create your views here.
def login(request):
    context = {}
    dados_senai = Senai.objects.all() #consulta no banco de dados trazendo todas as informações do hotel por meio de um objeto
    context["dados_senai"] = dados_senai
    return render(request, 'login.html', context)

def cadastro(request):
    pass
