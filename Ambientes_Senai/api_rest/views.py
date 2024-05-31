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

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ambientes(request):
    if request.method == 'GET':
        try:
            ambiente = Ambiente.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AmbienteSerializer(ambiente, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AmbienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    
    return Response(status=status.HTTP_400_BAD_REQUEST)