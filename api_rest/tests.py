from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Cliente, Carrinho

class ClienteTests(APITestCase):

    def setUp(self):
        Cliente.objects.create(nome="João", email="joaozinho@gmail.com")
        Cliente.objects.create(nome="Maria", email="mariazinha@gmail.com")

    def test_get_all_customers(self):
        url = reverse('get_all_customers')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_customer_by_nick(self):
        url = reverse('get_by_nick', args=["joaozinho"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], "João")

    def test_create_customer(self):
        url = reverse('create_customer')
        data = {"nome": "Pedro", "email": "pedrinho@gmail.com"}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], "Pedro")
        self.assertEqual(Cliente.objects.count(), 3)

    def test_delete_customer(self):
        cliente = Cliente.objects.get(nome="João")
        url = reverse('delete_customer', args=[cliente.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 1)


class CarrinhoTests(APITestCase):

    def setUp(self):
        Carrinho.objects.create(id=1, estado="disponível")
        Carrinho.objects.create(id=2, estado="ocupado")

    def test_get_all_carts(self):
        url = reverse('get_all_carts')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_cart_status(self):
        url = reverse('update_cart_status', args=[1])
        data = {"estado": "manutenção"}
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['estado'], "manutenção")
