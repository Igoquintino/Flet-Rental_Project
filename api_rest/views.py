# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CarrinhoSerializer, AluguelSerializer, ClienteSerializer
from .models import Carrinho, Aluguel, Cliente

import json
# Create your views here.

@api_view(['GET'])
def getCustomers(request):

    if request.method == 'GET':
        
        customers = Cliente.objects.all()

        serializer = ClienteSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick):
    
    try:
        customer = Cliente.objects.get(nome=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        
        serializer = ClienteSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
