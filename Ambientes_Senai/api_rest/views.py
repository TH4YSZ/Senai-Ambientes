from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ambiente.models import *
from .serializers import *

import json

# Create your views here.
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


@api_view(['GET', 'PUT', 'DELETE'])
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

    if request.method == 'PUT':

        serializer = AmbienteSerializer(id_ambiente, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            id_ambiente.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    return Response(status=status.HTTP_400_BAD_REQUEST)