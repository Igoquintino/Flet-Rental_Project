from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .services import (
    get_all_customers, get_customer_by_nick, create_customer, delete_customer,
    get_all_carts, get_cart_by_id, create_cart, update_cart_status, delete_cart,
    get_all_rentals, get_rental_by_id, create_rental, finalize_rental
)

########################################################
##############       CLIENTES        ###################
########################################################
@api_view(['GET'])
def getCustomers(request: Request) -> Response:
    return get_all_customers()

@api_view(['GET'])
def get_by_nick(request: Request, nick: str) -> Response:
    return get_customer_by_nick(nick)

@api_view(['POST'])
def createCustomer(request: Request) -> Response:
    return create_customer(request.data)

@api_view(['DELETE'])
def deleteCustomer(request: Request, customer_id: int) -> Response:
    return delete_customer(customer_id)


########################################################
##############      CARRINHOS        ###################
########################################################
@api_view(['GET'])
def getCarts(request: Request) -> Response:
    return get_all_carts()

@api_view(['GET'])
def getCartById(request: Request, cart_id: int) -> Response:
    return get_cart_by_id(cart_id)

@api_view(['POST'])
def createCart(request: Request) -> Response:
    return create_cart(request.data)

@api_view(['PATCH'])
def updateCartStatus(request: Request, cart_id: int) -> Response:
    status_value = request.data.get("estado")
    return update_cart_status(cart_id, status_value)

@api_view(['DELETE'])
def deleteCart(request: Request, cart_id: int) -> Response:
    return delete_cart(cart_id)


########################################################
##############        ALUGUEIS       ###################
########################################################
@api_view(['GET'])
def getRentals(request: Request) -> Response:
    return get_all_rentals()

@api_view(['GET'])
def getRentalById(request: Request, rental_id: int) -> Response:
    return get_rental_by_id(rental_id)

@api_view(['POST'])
def createRental(request: Request) -> Response:
    return create_rental(request.data)

@api_view(['PATCH'])
def finalizeRental(request: Request, rental_id: int) -> Response:
    return finalize_rental(rental_id)
