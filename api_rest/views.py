from rest_framework.decorators import api_view
from .services import (
    get_all_customers, get_customer_by_nick, create_customer, delete_customer,
    get_all_carts, get_cart_by_id, create_cart, update_cart_status, delete_cart,
    get_all_rentals, get_rental_by_id, create_rental, finalize_rental
)
########################################################
# CLIENTES
@api_view(['GET'])
def getCustomers(request):
    return get_all_customers()

@api_view(['GET'])
def get_by_nick(request, nick):
    return get_customer_by_nick(nick)

@api_view(['POST'])
def createCustomer(request):
    from .services import create_customer
    return create_customer(request.data)

@api_view(['DELETE'])
def deleteCustomer(request, customer_id):
    from .services import delete_customer
    return delete_customer(customer_id)



########################################################
# CARRINHOS
@api_view(['GET'])
def getCarts(request):
    return get_all_carts()

@api_view(['GET'])
def getCartById(request, cart_id):
    return get_cart_by_id(cart_id)

@api_view(['POST'])
def createCart(request):
    from .services import create_cart
    return create_cart(request.data)

@api_view(['PATCH'])
def updateCartStatus(request, cart_id):
    status_value = request.data.get("estado")
    return update_cart_status(cart_id, status_value)

@api_view(['DELETE'])
def deleteCart(request, cart_id):
    from .services import delete_cart
    return delete_cart(cart_id)



########################################################
# ALUGUEIS
@api_view(['GET'])
def getRentals(request):
    return get_all_rentals()

@api_view(['GET'])
def getRentalById(request, rental_id):
    return get_rental_by_id(rental_id)

@api_view(['POST'])
def createRental(request):
    return create_rental(request.data)

@api_view(['PATCH'])
def finalizeRental(request, rental_id):
    return finalize_rental(rental_id)
