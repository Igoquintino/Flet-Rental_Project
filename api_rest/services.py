from .models import Cliente, Carrinho, Aluguel
from .serializers import ClienteSerializer, CarrinhoSerializer, AluguelSerializer
from rest_framework.response import Response
from rest_framework import status



## SERVIÇOS RELACIADOS AO CLIENTE
def get_all_customers():
    customers = Cliente.objects.all()
    serializer = ClienteSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_customer_by_nick(nick):
    try:
        customer = Cliente.objects.get(nome=nick)
        serializer = ClienteSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente não encontrado."}, status=status.HTTP_404_NOT_FOUND)

def create_customer(data):
    from .serializers import ClienteSerializer
    serializer = ClienteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def delete_customer(customer_id):
    try:
        customer = Cliente.objects.get(id=customer_id)
        customer.delete()
        return Response({"message": "Cliente removido com sucesso."}, status=status.HTTP_204_NO_CONTENT)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente não encontrado."}, status=status.HTTP_404_NOT_FOUND)






## SERVIÇOS RELACIADOS A CARRINHO
def get_all_carts():
    carts = Carrinho.objects.all()
    serializer = CarrinhoSerializer(carts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_cart_by_id(cart_id):
    try:
        cart = Carrinho.objects.get(id=cart_id)
        serializer = CarrinhoSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Carrinho.DoesNotExist:
        return Response({"error": "Carrinho não encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
def create_cart(data):
    from .serializers import CarrinhoSerializer
    serializer = CarrinhoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_cart_status(cart_id, status_value):
    try:
        cart = Carrinho.objects.get(id=cart_id)
        cart.estado = status_value
        cart.save()
        serializer = CarrinhoSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Carrinho.DoesNotExist:
        return Response({"error": "Carrinho não encontrado."}, status=status.HTTP_404_NOT_FOUND)

def delete_cart(cart_id):
    try:
        cart = Carrinho.objects.get(id=cart_id)
        cart.delete()
        return Response({"message": "Carrinho removido com sucesso."}, status=status.HTTP_204_NO_CONTENT)
    except Carrinho.DoesNotExist:
        return Response({"error": "Carrinho não encontrado."}, status=status.HTTP_404_NOT_FOUND)






## SERVIÇOS RELACIADOS A ALUGUEL
def get_all_rentals():
    rentals = Aluguel.objects.all()
    serializer = AluguelSerializer(rentals, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_rental_by_id(rental_id):
    try:
        rental = Aluguel.objects.get(id=rental_id)
        serializer = AluguelSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Aluguel.DoesNotExist:
        return Response({"error": "Aluguel não encontrado."}, status=status.HTTP_404_NOT_FOUND)

def create_rental(data):
    serializer = AluguelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def finalize_rental(rental_id):
    try:
        rental = Aluguel.objects.get(id=rental_id)
        rental.status = "finalizado"
        rental.save()
        serializer = AluguelSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Aluguel.DoesNotExist:
        return Response({"error": "Aluguel não encontrado."}, status=status.HTTP_404_NOT_FOUND)
