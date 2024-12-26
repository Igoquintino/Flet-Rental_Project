from .models import Cliente, Carrinho, Aluguel
from .serializers import ClienteSerializer, CarrinhoSerializer, AluguelSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import DatabaseError
import logging

logger = logging.getLogger(__name__)

# Mensagens padrão para reutilização
ERROR_MESSAGES = {
    "not_found": "{} não encontrado.",
    "deleted": "{} removido com sucesso.",
    "db_error": "Erro interno no banco de dados.",
    "invalid_status": "Estado inválido. Estados permitidos são: {}.",
}

VALID_CART_STATES = ["disponível", "indisponível", "em manutenção"]

# Função utilitária para resposta de erro
def error_response(message, status_code=status.HTTP_400_BAD_REQUEST):
    return Response({"error": message}, status=status_code)

# Função genérica para criação de objetos
def create_object(serializer_class, data):
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Função genérica para exclusão de objetos
def delete_object(model, object_id):
    try:
        obj = model.objects.get(id=object_id)
        obj.delete()
        return Response({"message": ERROR_MESSAGES["deleted"].format(model.__name__)}, status=status.HTTP_204_NO_CONTENT)
    except model.DoesNotExist:
        return error_response(ERROR_MESSAGES["not_found"].format(model.__name__), status.HTTP_404_NOT_FOUND)

# Função utilitária para buscar objetos ou retornar 404
def get_object_or_error(model, **kwargs):
    return get_object_or_404(model, **kwargs)


# Serviços relacionados a Clientes
def get_all_customers():
    customers = Cliente.objects.all()
    serializer = ClienteSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_customer_by_nick(nick):
    customer = get_object_or_error(Cliente, nome=nick)
    serializer = ClienteSerializer(customer)
    return Response(serializer.data, status=status.HTTP_200_OK)

def create_customer(data):
    logger.info("Criando novo cliente...")
    return create_object(ClienteSerializer, data)

def delete_customer(customer_id):
    logger.warning(f"Excluindo cliente com ID {customer_id}...")
    return delete_object(Cliente, customer_id)


# Serviços relacionados a Carrinhos
def get_all_carts():
    
    carts = Carrinho.objects.all()
    serializer = CarrinhoSerializer(carts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_cart_by_id(cart_id):
    
    cart = get_object_or_error(Carrinho, id=cart_id)
    serializer = CarrinhoSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)

def create_cart(data):
    logger.info("Criando novo carrinho...")
    return create_object(CarrinhoSerializer, data)

def update_cart_status(cart_id, status_value):
    if status_value not in VALID_CART_STATES:
        return error_response(
            ERROR_MESSAGES["invalid_status"].format(", ".join(VALID_CART_STATES)),
            status.HTTP_400_BAD_REQUEST
        )
    try:
        cart = Carrinho.objects.get(id=cart_id)
        cart.estado = status_value
        cart.save()
        serializer = CarrinhoSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Carrinho.DoesNotExist:
        return error_response(ERROR_MESSAGES["not_found"].format("Carrinho"), status.HTTP_404_NOT_FOUND)
    
    except DatabaseError as e:
        logger.error(f"Erro no banco de dados ao atualizar o carrinho {cart_id}: {e}")
        return error_response(ERROR_MESSAGES["db_error"], status.HTTP_500_INTERNAL_SERVER_ERROR)

def delete_cart(cart_id):
    logger.warning(f"Excluindo carrinho com ID {cart_id}...")
    return delete_object(Carrinho, cart_id)


# Serviços relacionados a Aluguéis
def get_all_rentals():
    
    rentals = Aluguel.objects.all()
    serializer = AluguelSerializer(rentals, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_rental_by_id(rental_id):
    
    rental = get_object_or_error(Aluguel, id=rental_id)
    serializer = AluguelSerializer(rental)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

def create_rental(data):
    
    logger.info("Criando novo aluguel...")
    return create_object(AluguelSerializer, data)

def finalize_rental(rental_id):
    
    try:
        rental = Aluguel.objects.get(id=rental_id)
        rental.status = "finalizado"
        rental.save()
        serializer = AluguelSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Aluguel.DoesNotExist:
        return error_response(ERROR_MESSAGES["not_found"].format("Aluguel"), status.HTTP_404_NOT_FOUND)
    
    except DatabaseError as e:
        logger.error(f"Erro no banco de dados ao finalizar o aluguel {rental_id}: {e}")
        return error_response(ERROR_MESSAGES["db_error"], status.HTTP_500_INTERNAL_SERVER_ERROR)
