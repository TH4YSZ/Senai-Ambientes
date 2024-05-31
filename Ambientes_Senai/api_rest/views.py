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
        senai = Senai.objects.all()
        serializer = SenaiSerializer(senai, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)