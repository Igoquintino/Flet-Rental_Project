from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    #path('', views.getCarrinhos, name="get_all_carrinhos"),
    #path('alugueis', views.getAlugueis, name="alugueis"),
    path('customers', views.getCustomers, name="get_all_customers"),
    path('customers/<str:nick>', views.get_by_nick)
]
