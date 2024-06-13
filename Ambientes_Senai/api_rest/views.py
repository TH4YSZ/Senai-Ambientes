from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ambiente.models import *
from .serializers import *
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

# SENAI
@api_view(['GET'])
def senai(request):
    if request.method == 'GET':
        try:
            senai = Senai.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SenaiSerializer(senai, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# AMBIENTE
@api_view(['GET', 'POST'])
def ambientes_list_create(request):
    if request.method == 'GET':
        try:
            ambiente = Ambiente.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AmbienteSerializer(ambiente, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        new_ambiente = request.data 
        serializer = AmbienteSerializer(data=new_ambiente)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def ambientes_detail(request, id):
    try:
        id_ambiente = Ambiente.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        try:
            ambiente = Ambiente.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AmbienteSerializer(ambiente, many=True)
        return Response(serializer.data)

    
    if request.method == 'DELETE':

        try:
            id_ambiente.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    return Response(status=status.HTTP_400_BAD_REQUEST)


# USUÁRIO
@api_view(['POST'])
def usuario_create(request):
    if request.method == 'POST':
        new_usuario = request.data
        serializer = UsuarioSerializer(data=new_usuario)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# RESERVA
@api_view(['GET', 'POST'])
def reservas_list_create(request):
    if request.method == 'GET':
        try:
            reservas = Reserva.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        new_reserva = request.data
        serializer = ReservaSerializer(data=new_reserva)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def reservas_detail(request, id):
    try:
        reserva = Reserva.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        try:
            reserva.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)