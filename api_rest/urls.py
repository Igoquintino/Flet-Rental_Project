from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    # Clientes
    path('customers', views.getCustomers, name="get_all_customers"),
    path('customers/<str:nick>', views.get_by_nick, name="get_by_nick"),
    path('customers/create', views.createCustomer, name="create_customer"),
    path('customers/<int:customer_id>/delete', views.deleteCustomer, name="delete_customer"),

    # Carrinhos
    path('carts', views.getCarts, name="get_all_carts"),
    path('carts/<int:cart_id>', views.getCartById, name="get_cart_by_id"),
    path('carts/create', views.createCart, name="create_cart"),
    path('carts/<int:cart_id>/delete', views.deleteCart, name="delete_cart"),

    # Aluguéis
    path('rentals', views.getRentals, name="get_all_rentals"),
    path('rentals/<int:rental_id>', views.getRentalById, name="get_rental_by_id"),
    path('rentals/create', views.createRental, name="create_rental"),
    path('rentals/<int:rental_id>/finalize', views.finalizeRental, name="finalize_rental"),
]
